package main

import "fmt"

type Carro struct {
	Marca  string
	Modelo string
	Ano    int
}

func (c Carro) ExibirDetalhes() {
	fmt.Printf("Marca: %s, Modelo: %s, Ano: %d\n", c.Marca, c.Modelo, c.Ano)
}

func main() {
	carro1 := Carro{"Renault", "Sandero", 2018}
	carro2 := Carro{"volkswagen ", "Gol", 2015}
	carro3 := Carro{"Jeep", "Compass", 2023}

	carro1.ExibirDetalhes()
	carro2.ExibirDetalhes()
	carro3.ExibirDetalhes()
}