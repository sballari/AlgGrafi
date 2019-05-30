package main

import (
	"image/color"
	"log"
	"os"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/palette/moreland"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
	"gonum.org/v1/plot/vg/draw"
	"gonum.org/v1/plot/vg/vgimg"
)

func mainP(cities []City, cluster []int, MU []Centroid, k int, name string) {
	//make data

	p, err := plot.New()
	if err != nil {
		panic(err)
	}

	p.HideAxes()
	p.Title.Text = "kmeans plotx"
	p.X.Label.Text = "Latitude"
	p.Y.Label.Text = "Longitude"

	//p.Add(plotter.NewGrid())

	citiesData := citiesXYZs(cities, cluster)

	colors := moreland.Kindlmann() // Initialize a color map.
	colors.SetMax(float64(k - 1))
	colors.SetMin(0)

	sc, err := plotter.NewScatter(citiesData)
	if err != nil {
		panic(err)
	}

	centroidsData := centroidXYs(MU)
	cs, err := plotter.NewScatter(centroidsData)
	if err != nil {
		panic(err)
	}
	cs.GlyphStyle = draw.GlyphStyle{Color: color.Black, Radius: vg.Points(3), Shape: draw.BoxGlyph{}}

	sc.GlyphStyleFunc = func(i int) draw.GlyphStyle {
		_, _, z := citiesData.XYZ(i)
		d := z / float64(k-1)
		rng := float64(k - 1)
		k := d * rng
		c, err := colors.At(k)
		if err != nil {
			log.Panic(err)
		}
		return draw.GlyphStyle{Color: c, Radius: vg.Points(1), Shape: draw.BoxGlyph{}}
	}

	p.Add(sc)
	p.Add(cs)
	p.X.Scale = plot.LinearScale{}
	p.Y.Scale = plot.LinearScale{}
	// Save the plot to a PNG file.

	img := vgimg.New(1000, 634)
	dc := draw.New(img)
	//dc = draw.Crop(dc, 0, -legendWidth, 0, 0) // Make space for the legend.
	p.Draw(dc)

	w, err := os.Create(name)
	defer w.Close()
	if err != nil {
		log.Panic(err)
	}
	png := vgimg.PngCanvas{Canvas: img}
	if _, err = png.WriteTo(w); err != nil {
		log.Panic(err)
	}
	if err = w.Close(); err != nil {
		log.Panic(err)
	}

}

func citiesXYZs(cities []City, cluster []int) plotter.XYZs {
	pts := make(plotter.XYZs, len(cities))
	for i := range cities {
		pts[i].X = cities[i].Latitude
		pts[i].Y = cities[i].Longitude
		pts[i].Z = float64(cluster[i])
	}
	return pts
}

func centroidXYs(MU []Centroid) plotter.XYs {
	pts := make(plotter.XYs, len(MU))
	for i := range MU {
		pts[i].X = MU[i].Latitude
		pts[i].Y = MU[i].Longitude
	}
	return pts
}
