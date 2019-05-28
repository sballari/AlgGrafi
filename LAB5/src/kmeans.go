package main

import (
	"math"
)

func KMeansClustering(P []City, MU []Centroid, k int, q int) ([]int, []Centroid) {
	/*
		M : lista di k centroidi []Centroid
		P : lista di n Citta' 	 []City
		k : len(M)
		q : numero di iterazioni di raffinamento
	*/
	var n = len(P)
	var cluster []int //cluster[i] = cluster a cui il punto i viene assegnato

	for i := 1; i <= q; i++ { //iterazioni di raffinamento (no punto fisso)

		//ASSEGNAMENTO per ogni nodo in P
		for j := 0; j < n; j++ { //it should be a parallel for
			l := nearestCentroidIndex(&P[j], MU)
			cluster[j] = l //assegno a P[j] il cluster l
		}
		//AGGIORNAMENTO per ogni centroide f in MU
		for f := 0; f < k; f++ { //parallel for
			fakeChannel := make(chan pReduceResult) //NON USATO solo per compilare e non avere errori RT
			pRedResult := pReduceCluster(P, cluster, 0, n-1, f, fakeChannel)
			MU[f].Latitude = pRedResult.sumX / (float64)(pRedResult.size)
			MU[f].Longitude = pRedResult.sumY / (float64)(pRedResult.size)
		}
	}
	return cluster, MU
}

func nearestCentroidIndex(city *City, centroids []Centroid) int {
	/*
		descr: scorre tutti i centroidi in centroids e ritorna l'indice del centroide piu'
		vicino alla citta' city
	*/
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

func pReduceCluster(P []City, cluster []int, i int, j int, h int, fatherChan chan pReduceResult) pReduceResult {
	myChannel := make(chan pReduceResult)

	if i == j {
		if cluster[i] == h {
			result := pReduceResult{
				sumX: P[i].Latitude,
				sumY: P[i].Longitude,
				size: 1,
			}
			fatherChan <- result
			return result
		} else {
			result := pReduceResult{sumX: 0, sumY: 0, size: 0}
			fatherChan <- result
			return result
		}
	} else {
		mid := (i + j) / 2

		go pReduceCluster(P, cluster, i, mid, h, myChannel)
		result2 := pReduceCluster(P, cluster, mid+1, j, h, myChannel)
		result1 := <-myChannel

		result := pReduceResult{
			sumX: result1.sumX + result2.sumX,
			sumY: result1.sumY + result2.sumY,
			size: result1.size + result2.size,
		}
		fatherChan <- result
		return result
	}

}

func eucDistance(c1 *City, c2 *Centroid) float64 {
	deltaX := c1.Latitude - c2.Latitude
	deltaY := c1.Longitude - c2.Longitude
	dist := math.Sqrt(math.Pow(deltaX, 2) + math.Pow(deltaY, 2))
	return dist
}
