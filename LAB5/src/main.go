package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Main lanciato")
	k := 50
	q := 1000
	cities, centroids := Parser(k)
	//fmt.Println(len(centroids))

	start := time.Now()
	cluster, MU := KMeansClustering(cities, centroids, k, q)
	elapsed := time.Since(start)

	fmt.Printf("kmeans took %s\n", elapsed)

	fmt.Println(len(cluster))
	fmt.Println(len(MU))

}
