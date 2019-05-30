package main

import (
	"fmt"
	"time"
)

func main() {

	fmt.Println("Main lanciato")
	//fmt.Printf("GOMAXPROCS is %d\n", runtime.GOMAXPROCS(-1))
	k := 50
	q := 100
	cities, centroids := Parser(k, 21000)
	//fmt.Println(len(centroids))

	start := time.Now()
	cluster, MU := KMeansClustering(cities, centroids, k, q)
	elapsed := time.Since(start)

	fmt.Printf("kmeans took %s\n", elapsed)

	fmt.Println(len(cluster))
	fmt.Println(len(MU))

}
