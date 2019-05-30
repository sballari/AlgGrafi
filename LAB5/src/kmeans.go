package main

import (
	"math"
	"sync"
)

/*
	Seq parallelo
	M : lista di k centroidi []Centroid
	P : lista di n Citta' 	 []City
	k : len(M)
	q : numero di iterazioni di raffinamento
*/
func KMeansClustering(P []City, MU []Centroid, k int, q int) ([]int, []Centroid) {
	var n = len(P)
	var cluster = make([]int, n) //cluster[i] = cluster a cui il punto i viene assegnato

	for i := 1; i <= q; i++ { //iterazioni di raffinamento (no punto fisso)

		//fmt.Printf("iterazione %d\n", i)
		//ASSEGNAMENTO per ogni nodo in P
		var wg sync.WaitGroup

		wg.Add(n)
		for j := 0; j < n; j++ { //it should be a parallel for
			go func(j int) {
				defer wg.Done()
				l := nearestCentroidIndex(&P[j], MU)
				cluster[j] = l //assegno a P[j] il cluster l
			}(j)
		}
		wg.Wait()

		//AGGIORNAMENTO per ogni centroide f in MU
		wg.Add(k)
		for f := 0; f < k; f++ { //parallel for
			go func(f int) {
				defer wg.Done()
				// resultChannel := make(chan pReduceResult)
				// go pReduceCluster(P, cluster, 0, n-1, f, resultChannel)
				// pRedResult := <-resultChannel
				pRedResult := pReduceClusterReturn(P, cluster, 0, n-1, f)

				MU[f].Latitude = pRedResult.sumX / (float64)(pRedResult.size)
				MU[f].Longitude = pRedResult.sumY / (float64)(pRedResult.size)
			}(f)
		}
		wg.Wait()
	}
	return cluster, MU
}

/*	nearestCentroidIndex
	descr: scorre tutti i centroidi in centroids e ritorna l'indice del centroide piu'
	vicino alla citta' city
*/
func nearestCentroidIndex(city *City, centroids []Centroid) int {
	nearestIndex := -1
	minDist := math.MaxFloat64

	for i := 0; i < len(centroids); i++ {
		dist := eucDistance(city, &centroids[i])
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

func pReduceCluster(P []City, cluster []int, i int, j int, h int, fatherChan chan pReduceResult) {
	myChannel := make(chan pReduceResult)

	if i == j {
		if cluster[i] == h {
			result := pReduceResult{
				sumX: P[i].Latitude,
				sumY: P[i].Longitude,
				size: 1,
			}
			fatherChan <- result

		} else {
			result := pReduceResult{sumX: 0, sumY: 0, size: 0}
			fatherChan <- result

		}
	} else {
		mid := (i + j) / 2

		go pReduceCluster(P, cluster, i, mid, h, myChannel)
		result2 := pReduceClusterReturn(P, cluster, mid+1, j, h)
		result1 := <-myChannel

		result := pReduceResult{
			sumX: result1.sumX + result2.sumX,
			sumY: result1.sumY + result2.sumY,
			size: result1.size + result2.size,
		}
		fatherChan <- result
	}

}

func eucDistance(c1 *City, c2 *Centroid) float64 {
	deltaX := c1.Latitude - c2.Latitude
	deltaY := c1.Longitude - c2.Longitude
	dist := math.Sqrt(math.Pow(deltaX, 2) + math.Pow(deltaY, 2))
	return dist
}

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
		result1 := <-myChannel

		result := pReduceResult{
			sumX: result1.sumX + result2.sumX,
			sumY: result1.sumY + result2.sumY,
			size: result1.size + result2.size,
		}
		return result
	}
}

// func parallelFor(op func(int), i int, j int, wg sync.WaitGroup) {
// 	if i == j {
// 		op(i)
// 		wg.Done()
// 	}
// 	mid := (i + j) / 2
// 	parallelFor(op, i, mid, wg)
// 	parallelFor(op, mid+1, j, wg)
// }

func KMeansClusteringSeq(P []City, MU []Centroid, k int, q int) ([]([]City), []Centroid) {
	var n = len(P)

	var clusters []([]City)

	for i := 1; i <= q; i++ { //iterazioni di raffinamento (no punto fisso)
		//fmt.Printf("iterazione %d\n", i)

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
	}
	return clusters, MU
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
