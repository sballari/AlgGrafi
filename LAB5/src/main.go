package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	//"time"
)

type Istance struct {
	domanda int
	n       int
	k       int
	it      int
	cutoff  int
	par     int64
	seq     int64
}

func istance() []Istance {
	csvFile, _ := os.Open("data/istance.csv")
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
		currentcutoff, _ := strconv.Atoi(line[4])

		var istance Istance

		istance = Istance{
			domanda: currentdomanda,
			n:       currentn,
			k:       currentk,
			it:      currentit,
			cutoff:  currentcutoff,
		}

		istances = append(istances, istance)

	}
	return istances
}

func main() {
	var istances []Istance
	istances = istance()

	fmt.Println("Main lanciato")

	var str []string

	for i := 0; i < len(istances); i++ {

		citiesDts := make([]City, 38184)
		centroidDts := make([]Centroid, istances[i].k)

		citiesDts, centroidDts = Parser(istances[i].k, istances[i].n)
		istances[i].n = len(citiesDts)

		//parallelo
		_, _, qpar := KMeansClustering(citiesDts, centroidDts, istances[i].k, istances[i].it, istances[i].cutoff)
		istances[i].par = qpar[istances[i].it-1]

		//sequenziale

		_, _, qseq := KMeansClusteringSeq(citiesDts, centroidDts, istances[i].k, istances[i].it)
		istances[i].seq = qseq[istances[i].it-1]

		var stristance string
		stristance = strconv.FormatInt(int64(istances[i].domanda), 10) + " " + strconv.FormatInt(int64(istances[i].n), 10) + " "
		stristance = stristance + strconv.FormatInt(int64(istances[i].k), 10) + " " + strconv.FormatInt(int64(istances[i].it), 10) + " "
		stristance = stristance + strconv.FormatInt(int64(istances[i].cutoff), 10) + " " + strconv.FormatInt(istances[i].par, 10) + " "
		stristance = stristance + strconv.FormatInt(istances[i].seq, 10)
		str = append(str, stristance)
		fmt.Println(stristance)
	}
	fmt.Println("####################################")

	file, err := os.Create("result.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	w := csv.NewWriter(file)

	for _, value := range str {
		var temp []string
		temp = append(temp, value)
		if err := w.Write(temp); err != nil {
			log.Fatalln("Error writing record to csv: ", err)
		}
	}
	w.Flush()

}
