package main

import (
	"bufio"
	"encoding/csv"
	"io"
	"log"
	"os"
	"strconv"
)

type City struct {
	Id        int
	Name      string
	Pop       int
	Latitude  float64
	Longitude float64
}

type Centroid struct {
	Latitude  float64
	Longitude float64
}

func Parser(k int, minPopulation int) ([]City, []Centroid) {
	/*
		k := numero dei centroidi da prendere
	*/
	csvFile, _ := os.Open("../data/cities-and-towns-of-usa.csv")
	reader := csv.NewReader(bufio.NewReader(csvFile))
	var cities []City
	var kMaxCity []City

	reader.Read() //leggo a vuoto il primo valore (i titoli)

	for {
		line, error := reader.Read()
		if error == io.EOF {
			break
		} else if error != nil {
			log.Fatal(error)
		}
		var city City

		pop, _ := strconv.Atoi(line[2])

		if pop >= minPopulation {
			id, _ := strconv.Atoi(line[0])
			name := line[1]
			latitude, _ := strconv.ParseFloat(line[3], 64)
			longitude, _ := strconv.ParseFloat(line[4], 64)

			city = City{
				Id:        id,
				Name:      name,
				Pop:       pop,
				Latitude:  latitude,
				Longitude: longitude,
			}
			cities = append(cities, city)

			if len(kMaxCity) < k {
				kMaxCity = append(kMaxCity, city)
			} else {
				//TODO si potrebbe fare con lista ordinata
				smallest, pos := findMin(kMaxCity)
				if city.Pop > smallest.Pop {
					kMaxCity[pos] = city
				}
			}
		}
	}
	//converto le k citta' piu' grandi in centroidi
	var centroids []Centroid
	for c := range kMaxCity {
		centroid := Centroid{
			Latitude:  kMaxCity[c].Latitude,
			Longitude: kMaxCity[c].Longitude,
		}
		centroids = append(centroids, centroid)
	}
	return cities, centroids
}

func findMin(cs []City) (*City, int) {
	if len(cs) == 0 {
		return nil, 0
	}

	minPop := cs[0].Pop
	minPosition := 0

	for i := 1; i < len(cs); i++ {
		if cs[i].Pop < minPop {
			minPop = cs[i].Pop
			minPosition = i
		}
	}
	return &(cs[minPosition]), minPosition

}
