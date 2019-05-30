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

	citiesDts := make([]([]City), 6)
	centroidDts := make([]([]Centroid), 6)

	citiesDts[0], centroidDts[0] = Parser(k, 250)
	citiesDts[1], centroidDts[1] = Parser(k, 2000)
	citiesDts[2], centroidDts[2] = Parser(k, 5000)
	citiesDts[3], centroidDts[3] = Parser(k, 15000)
	citiesDts[4], centroidDts[4] = Parser(k, 50000)
	citiesDts[5], centroidDts[5] = Parser(k, 100000)

	timesPar := make([]time.Duration, 6)
	timesSeq := make([]time.Duration, 6)

	for i := 1; i < 6; i++ {
		fmt.Println("####################################")
		fmt.Printf("DATASET%d n=%d\n", i, len(citiesDts[i]))

		//parallelo
		start := time.Now()
		cluster, MUpar := KMeansClustering(citiesDts[i], centroidDts[i], k, q)
		timesPar[i] = time.Since(start)
		fmt.Print("time // = ")
		fmt.Println(timesPar[i])

		//sequenziale
		start = time.Now()
		clusters, MUseq := KMeansClusteringSeq(citiesDts[i], centroidDts[i], k, q)
		timesSeq[i] = time.Since(start)
		fmt.Print("time Seq = ")
		fmt.Println(timesSeq[i])

		fmt.Println(len(cluster), len(MUpar), len(clusters), len(MUseq))
		//mainP(citiesDts[i], cluster, MUpar, k, "../data/imgs/"+strconv.Itoa(i)+".png")
	}
	fmt.Println("####################################")

}
