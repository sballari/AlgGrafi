package main

import (
	"math"
)

func SlowClosestPair(P []City) (float64, City, City) {
	var minDist = math.MaxFloat64
	var city1 City
	var city2 City

	for u := 0; u < len(P); u++ {
		for v := u + 1; v < len(P); v++ {
			var distUV = eucDistance(P[u], P[v])
			if distUV < minDist {
				minDist = distUV
				city1 = P[u]
				city2 = P[v]
			}
		}
	}
	return minDist, city1, city2
}

func eucDistance(c1 City, c2 City) float64 {
	var deltaX = c1.Latitude - c2.Latitude
	var deltaY = c1.Longitude - c2.Longitude
	return math.Sqrt(math.Pow(deltaX, 2) + math.Pow(deltaY, 2))
}
