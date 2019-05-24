package main

import (
	"fmt"
)

func main() {
	fmt.Println("Main lanciato")
	cities := Parser()
	d, c1, c2 := SlowClosestPair(cities)
	fmt.Printf("distanza: %f\tcitta1: %s\tcitta2: %s\n", d, c1.Name, c2.Name)

}
