package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"time"
	"io"
	"strconv"
)

type Istance struct {
	domanda int
	n  int
	k  int
	it int
	par int
	seq int
}

func istance()[]Istance{
	csvFile, _ := os.Open("../data/istance.csv")
	reader := csv.NewReader(bufio.NewReader(csvFile))

	var istances []Istance

	for {
		line, error := reader.Read()
		if error == io.EOF {
			break
		} else if error != nil {
			log.Fatal(error)
		}

		currentdomanda, _ := strconv.Atoi(line[0])
		currentn, _ := strconv.Atoi(line[1])
		currentk, _ := strconv.Atoi(line[2])
		currentit, _ := strconv.Atoi(line[3])

		var istance Istance

		istance = Istance{
			domanda : currentdomanda,
			n : currentn,
			k : currentk,
			it : currentit,
		}

		istances = append(istances,istance)

	}
	return istances
}

func main() {
	//var istances []Istance
	//istances = istance()


	fmt.Println("Main lanciato")
	//fmt.Printf("GOMAXPROCS is %d\n", runtime.GOMAXPROCS(-1))

	k := 50
	q := 100
	
	citiesDts := make([]([]City), 6)
	centroidDts := make([]([]Centroid), 6)

	//250, 2.000, 5.000, 15.000, 50.000, e 100.000

	citiesDts[0], centroidDts[0] = Parser(k, 250)
	citiesDts[1], centroidDts[1] = Parser(k, 2000)
	citiesDts[2], centroidDts[2] = Parser(k, 5000)
	citiesDts[3], centroidDts[3] = Parser(k, 15000)
	citiesDts[4], centroidDts[4] = Parser(k, 50000)
	citiesDts[5], centroidDts[5] = Parser(k, 100000)

	timesPar := make([]string, 6)
	timesSeq := make([]string, 6)

	for i := 1; i < 6; i++ {
		fmt.Println("####################################")
		fmt.Printf("DATASET%d n=%d\n", i, len(citiesDts[i]))

		//parallelo
		start := time.Now()
		cluster, MUpar := KMeansClustering(citiesDts[i], centroidDts[i], k, q)
		timesPar[i] = time.Since(start).String()
		fmt.Print("time // = ")
		fmt.Println(timesPar[i])

		//sequenziale
		start = time.Now()
		clusters, MUseq := KMeansClusteringSeq(citiesDts[i], centroidDts[i], k, q)
		timesSeq[i] = time.Since(start).String()
		fmt.Print("time Seq = ")
		fmt.Println(timesSeq[i])

		fmt.Println(len(cluster), len(MUpar), len(clusters), len(MUseq))
		//mainP(citiesDts[i], cluster, MUpar, k, "../data/imgs/"+strconv.Itoa(i)+".png")
	}
	fmt.Println("####################################")

	var data = [][]string{timesPar, timesSeq}

	file, err := os.Create("result.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	w := csv.NewWriter(file)

	for _, value := range data {
		if err := w.Write(value); err != nil {
			log.Fatalln("Error writing record to csv: ", err)
		}
	}
	w.Flush()

}
