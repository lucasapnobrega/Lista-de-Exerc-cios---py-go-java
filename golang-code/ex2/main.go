package main

import "fmt"

type Carro struct {
	Marca      string
	Modelo     string
	Ano        int
	Velocidade int
}

func (c *Carro) Acelerar(incremento int) {
	c.Velocidade += incremento
	fmt.Printf("O carro acelerou. Velocidade atual: %d km/h\n", c.Velocidade)
}

func (c *Carro) Frear(decremento int) {
	c.Velocidade -= decremento
	if c.Velocidade < 0 {
			c.Velocidade = 0
	}
	fmt.Printf("O carro freou. Velocidade atual: %d km/h\n", c.Velocidade)
}

func (c Carro) ExibirVelocidade() {
  fmt.Printf("Velocidade atual: %d km/h\n", c.Velocidade)
}

func main() {
	carro := Carro{Marca: "BMW", Modelo: "M4", Ano: 2022, Velocidade: 0}

	carro.Acelerar(60)   
	carro.Acelerar(150)
	carro.Frear(20)  
	carro.ExibirVelocidade() 
	carro.Frear(30)
	carro.Acelerar(50)
	carro.ExibirVelocidade()
}