package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
)

type City struct {
	Id        int64
	Name      string
	Pop       int64
	Latitude  float64
	Longitude float64
}

type Centroid struct {
	Latitude  float64
	Longitude float64
}

func Parser(k int) ([]City, []Centroid) {
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

		id, _ := strconv.ParseInt(line[0], 10, 64)
		name := line[1]
		pop, _ := strconv.ParseInt(line[2], 10, 64)
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
			biggest, pos := findMax(kMaxCity)
			if city.Pop > biggest.Pop {
				kMaxCity[pos] = city
			}
		}
	}

	fmt.Println(kMaxCity)

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

func findMax(kMaxs []City) (*City, int) {
	if len(kMaxs) == 0 {
		return nil, 0
	}

	maxPop := kMaxs[0].Pop
	maxPosition := 0

	for i := 1; i < len(kMaxs); i++ {
		if kMaxs[i].Pop > maxPop {
			maxPop = kMaxs[i].Pop
			maxPosition = i
		}
	}
	return &(kMaxs[maxPosition]), maxPosition

}
