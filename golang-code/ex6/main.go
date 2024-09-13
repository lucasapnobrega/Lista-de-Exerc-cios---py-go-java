package main

import "fmt"

type Motor struct {
  Tipo string
}

func (m Motor) ExibirTipo() string {
  return "Tipo de motor: " + m.Tipo
}

type Carro struct {
	Marca string
	Modelo string
	Motor Motor
}

func (c Carro) ExibirDetalhes() string {
	return "Marca: " + c.Marca + ", Modelo: " + c.Modelo + ", " + c.Motor.ExibirTipo()
}

func main() {
	motor := Motor{Tipo: "V8"}
	carro := Carro{Marca: "Volswagen", Modelo: "Golf", Motor: motor}

	fmt.Println(carro.ExibirDetalhes())
}