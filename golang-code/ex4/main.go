package main

import "fmt"

type Animal interface {
  Som() string
}

type Cachorro struct{}

func (c Cachorro) Som() string {
  return "Au Au"
}

type Gato struct{}

func (g Gato) Som() string {
  return "Miau"
}

func exibirSom(a Animal) {
  fmt.Println(a.Som())
}

func main() {
	cachorro := Cachorro{}
	gato := Gato{}

	exibirSom(cachorro)  
	exibirSom(gato) 
}