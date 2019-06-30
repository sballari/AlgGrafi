package main

import (
	"math"
	// "sync"
	"time"
	//"fmt"
)

/*
	Seq parallelo
	M : lista di k centroidi []Centroid
	P : lista di n Citta' 	 []City
	k : len(M)
	q : numero di iterazioni di raffinamento
*/
func KMeansClustering(P []City, MU []Centroid, k int, q int, cutoff int) ([]int, []Centroid, []time.Duration) {
	var n = len(P)
	var cluster = make([]int, n) //cluster[i] = cluster a cui il punto i viene assegnato
	wgChannel := make(chan int)
	t := make([]time.Duration, q)
	var t_1 time.Duration
	t_1 = 0

	for i := 0; i < q; i++ { //iterazioni di raffinamento (no punto fisso)

		//ASSEGNAMENTO per ogni nodo in P
		// var wg sync.WaitGroup

		// wg.Add(n)

		start := time.Now()
		/*
			for j := 0; j < n; j++ { //it should be a parallel for
				go func(j int,wgChannel chan int) {
					l := nearestCentroidIndex(&P[j], MU)
					cluster[j] = l //assegno a P[j] il cluster l
					wgChannel <- 1
					// wg.Done()
					return
				}(j,wgChannel)
			}
			// wg.Wait()

			for i:= 0; i < n; i++ {
				 <- wgChannel
			}
		*/
		cluster := make([]int, n)
		nearestCentroid(P, MU, 0, n-1, cutoff, cluster)

		//AGGIORNAMENTO per ogni centroide f in MU
		// wg.Add(k)

		for f := 0; f < k; f++ { //parallel for
			go func(f int, wgChannel chan int) {

				myChannel := make(chan pReduceResult)
				go pReduceCluster(P, cluster, 0, n-1, f, myChannel, cutoff)
				pRedResult := <-myChannel

				MU[f].Latitude = pRedResult.sumX / (float64)(pRedResult.size)
				MU[f].Longitude = pRedResult.sumY / (float64)(pRedResult.size)
				// wg.Done()
				wgChannel <- 1
				return
			}(f, wgChannel)
		}
		// wg.Wait()

		for i := 0; i < k; i++ {
			<-wgChannel
		}

		end := time.Since(start)
		t[i] = end + t_1
		t_1 = t[i]
	}
	//fmt.Print("Fase 2: ")
	//	fmt.Println(t2)
	//fmt.Print("Fase 3: ")
	//	fmt.Println(t3)
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
		go nearestCentroid(P, MU, i, mid, cutoff, cluster)
		go nearestCentroid(P, MU, mid+1, j, cutoff, cluster)
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
	//fmt.Println(j-i)
	if j-i <= cutoff {
		var x float64 = 0
		var y float64 = 0
		var count int = 0
		for z := i; z <= j; z++ {
			if cluster[z] == h {
				x = x + P[i].Latitude
				y = y + P[i].Longitude
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
		go pReduceCluster(P, cluster, mid+1, j, h, myChannel, cutoff)
		//result2 := pReduceClusterReturn(P, cluster, mid+1, j, h)
		result2 := <-myChannel
		result1 := <-myChannel

		result := pReduceResult{
			sumX: result1.sumX + result2.sumX,
			sumY: result1.sumY + result2.sumY,
			size: result1.size + result2.size,
		}
		fatherChan <- result
	}
}

// func eucDistance(c1 *City, c2 *Centroid) float64 {
// 	deltaX := c1.Latitude - c2.Latitude
// 	deltaY := c1.Longitude - c2.Longitude
// 	dist := math.Sqrt(math.Pow(deltaX, 2) + math.Pow(deltaY, 2))
// 	return dist

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
/*
func pReduceClusterReturn(P []City, cluster []int, i int, j int, h int) pReduceResult {
	myChannel := make(chan pReduceResult)

	if i == j {
		if cluster[i] == h {
			result := pReduceResult{
				sumX: P[i].Latitude,
				sumY: P[i].Longitude,
				size: 1,
			}
			return result
		} else {
			result := pReduceResult{sumX: 0, sumY: 0, size: 0}
			return result
		}
	} else {
		mid := (i + j) / 2

		go pReduceCluster(P, cluster, i, mid, h, myChannel)
		result2 := pReduceClusterReturn(P, cluster, mid+1, j, h)
		result1 := <-myChannel // mi metto in attesa di pReduceCluster sul canale myChannel

		result := pReduceResult{
			sumX: result1.sumX + result2.sumX,
			sumY: result1.sumY + result2.sumY,
			size: result1.size + result2.size,
		}
		return result
	}
}
*/
// func parallelFor(op func(int), i int, j int, wg sync.WaitGroup) {
// 	if i == j {
// 		op(i)
// 		wg.Done()
// 	}
// 	mid := (i + j) / 2
// 	parallelFor(op, i, mid, wg)
// 	parallelFor(op, mid+1, j, wg)
// }

func KMeansClusteringSeq(P []City, MU []Centroid, k int, q int) ([]([]City), []Centroid, []time.Duration) {

	var n = len(P)

	var clusters []([]City)

	t := make([]time.Duration, q)
	var t_1 time.Duration
	t_1 = 0

	for i := 0; i < q; i++ { //iterazioni di raffinamento (no punto fisso)
		//fmt.Printf("iterazione %d\n", i)
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

		end := time.Since(start)
		t[i] = end + t_1
		t_1 = t[i]
	}
	return clusters, MU, t
}

func center(f int, clusters []([]City), MU []Centroid) {
	var sumX float64
	var sumY float64
	for i := 0; i < len(clusters[f]); i++ {
		sumX := sumX + clusters[f][i].Latitude
		sumY := sumY + clusters[f][i].Longitude
		MU[f].Latitude = sumX / (float64)(len(clusters[f]))
		MU[f].Longitude = sumY / (float64)(len(clusters[f]))
	}

}
