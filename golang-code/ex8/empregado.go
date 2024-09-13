package main

import "fmt"

type Empregado struct {
	Nome    string
	Cargo   string
	Salario float64
}

func (e *Empregado) String() string {
  return fmt.Sprintf("%s, %s, %.2f", e.Nome, e.Cargo, e.Salario)
}