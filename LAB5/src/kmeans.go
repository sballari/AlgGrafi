package main

import (
	"math"
	"time"
)

/*
	Seq parallelo
	M : lista di k centroidi []Centroid
	P : lista di n Citta' 	 []City
	k : len(M)
	q : numero di iterazioni di raffinamento
*/
func KMeansClustering(P []City, centroids []Centroid, k int, q int, cutoff int) ([]int, []Centroid, []int64) {
	MU := make([]Centroid, len(centroids))
	copy(MU, centroids)
	var n = len(P)

	var cluster = make([]int, n) //cluster[i] = cluster a cui il punto i viene assegnato
	wgChannel := make(chan int)
	t := make([]int64, q)
	var t1 int64
	t1 = 0

	for i := 0; i < q; i++ { //iterazioni di raffinamento (no punto fisso)

		//ASSEGNAMENTO per ogni nodo in P
		start := time.Now()
		nearestCentroid(P, MU, 0, n-1, cutoff, cluster)

		//AGGIORNAMENTO per ogni centroide f in MU

		for f := 0; f < k; f++ { //parallel for
			go func(f int, wgChannel chan int) {

				pRedResult := pReduceClusterReturn(P, cluster, 0, n-1, f, cutoff)
				if pRedResult.size > 0 {
					MU[f].Latitude = pRedResult.sumX / (float64)(pRedResult.size)
					MU[f].Longitude = pRedResult.sumY / (float64)(pRedResult.size)
				}

				wgChannel <- 1
				return
			}(f, wgChannel)
		}

		for i := 0; i < k; i++ {
			<-wgChannel
		}

		end := time.Since(start).Nanoseconds() / 1000000
		t[i] = end + t1
		t1 = t[i]
	}
	return cluster, MU, t
}

func nearestCentroid(P []City, MU []Centroid, i int, j int, cutoff int, cluster []int) {
	if j-i <= cutoff {
		for z := i; z <= j; z++ {
			l := nearestCentroidIndex(&P[z], MU)
			cluster[z] = l
		}
	} else {
		mid := (i + j) / 2

		c := make(chan struct{})
		go func() {
			nearestCentroid(P, MU, i, mid, cutoff, cluster)
			c <- struct{}{}
		}()
		nearestCentroid(P, MU, mid+1, j, cutoff, cluster)
		<-c
	}
}

/*	nearestCentroidIndex
	descr: scorre tutti i centroidi in centroids e ritorna l'indice del centroide piu'
	vicino alla citta' city
*/
func nearestCentroidIndex(city *City, centroids []Centroid) int {
	nearestIndex := -1
	minDist := int64(math.MaxInt64) //DANGER

	for i := 0; i < len(centroids); i++ {
		dist := GEO_Distance(city, &centroids[i])
		if dist < minDist {
			nearestIndex = i
			minDist = dist
		}
	}
	return nearestIndex
}

type pReduceResult struct {
	sumX float64
	sumY float64
	size int
}

func pReduceCluster(P []City, cluster []int, i int, j int, h int, fatherChan chan pReduceResult, cutoff int) { // T(n) = 2*T(n/2) + O(1)
	myChannel := make(chan pReduceResult)

	if j-i <= cutoff {
		var x float64
		var y float64
		var count int
		for z := i; z <= j; z++ {
			if cluster[z] == h {
				x = x + P[z].Latitude
				y = y + P[z].Longitude
				count = count + 1
			}
		}
		result := pReduceResult{
			sumX: x,
			sumY: y,
			size: count,
		}
		fatherChan <- result
	} else {
		mid := (i + j) / 2

		go pReduceCluster(P, cluster, i, mid, h, myChannel, cutoff)
		result2 := pReduceClusterReturn(P, cluster, mid+1, j, h, cutoff)

		result1 := <-myChannel

		result := pReduceResult{
			sumX: result1.sumX + result2.sumX,
			sumY: result1.sumY + result2.sumY,
			size: result1.size + result2.size,
		}
		fatherChan <- result
	}
}

func GEO_Distance(c1 *City, c2 *Centroid) int64 {
	RRR := 6378.388

	q1 := math.Cos(c1.Longitude - c2.Longitude)
	q2 := math.Cos(c1.Latitude - c2.Latitude)
	q3 := math.Cos(c1.Latitude + c2.Latitude)
	dij := int64(RRR*math.Acos(0.5*((1.0+q1)*q2-(1.0-q1)*q3)) + 1.0)

	return dij
}

// P = punti
// cluster[i] = il punto P[i] appartiene al cluster cluster[i]
// i = bound sx di P
// j = bound dx di P
// h = centroide

func pReduceClusterReturn(P []City, cluster []int, i int, j int, h int, cutoff int) pReduceResult {
	myChannel := make(chan pReduceResult)

	if j-i <= cutoff {
		var x float64 = 0
		var y float64 = 0
		var count int = 0
		for z := i; z <= j; z++ {
			if cluster[z] == h {
				x = x + P[z].Latitude
				y = y + P[z].Longitude
				count = count + 1
			}
		}
		result := pReduceResult{
			sumX: x,
			sumY: y,
			size: count,
		}
		return result
	}

	mid := (i + j) / 2

	go pReduceCluster(P, cluster, i, mid, h, myChannel, cutoff)
	result2 := pReduceClusterReturn(P, cluster, mid+1, j, h, cutoff)
	result1 := <-myChannel // mi metto in attesa di pReduceCluster sul canale myChannel

	result := pReduceResult{
		sumX: result1.sumX + result2.sumX,
		sumY: result1.sumY + result2.sumY,
		size: result1.size + result2.size,
	}
	return result
}

func KMeansClusteringSeq(P []City, MU []Centroid, k int, q int) ([]([]City), []Centroid, []int64) {

	var n = len(P)

	var clusters []([]City)

	t := make([]int64, q)
	var t1 int64
	t1 = 0

	for i := 0; i < q; i++ { //iterazioni di raffinamento (no punto fisso)

		start := time.Now()

		//CLUSTER VUOTI
		clusters = make([]([]City), k)
		//ASSEGNAMENTO per ogni nodo in P

		for j := 0; j < n; j++ {
			l := nearestCentroidIndex(&P[j], MU)

			clusters[l] = append(clusters[l], P[j]) //OK??
		}

		//AGGIORNAMENTO per ogni centroide f in MU
		for f := 0; f < k; f++ {
			center(f, clusters, MU)
		}

		end := time.Since(start).Nanoseconds() / 1000000
		t[i] = end + t1
		t1 = t[i]
	}
	return clusters, MU, t
}

func center(f int, clusters []([]City), MU []Centroid) {
	if len(clusters[f]) > 0 {
		var sumX float64
		var sumY float64
		for i := 0; i < len(clusters[f]); i++ {
			sumX += clusters[f][i].Latitude
			sumY += clusters[f][i].Longitude
		}

		MU[f].Latitude = sumX / (float64)(len(clusters[f]))
		MU[f].Longitude = sumY / (float64)(len(clusters[f]))
	}
}
