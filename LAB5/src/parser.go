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
	Id        int64
	Name      string
	Pop       int64
	Latitude  float64
	Longitude float64
}

func Parser() []City {
	csvFile, _ := os.Open("../data/cities-and-towns-of-usa.csv")
	reader := csv.NewReader(bufio.NewReader(csvFile))
	var cities []City

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
	}
	return cities
}
