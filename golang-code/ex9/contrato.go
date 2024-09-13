package main

import "fmt"

type Contrato struct {
  Detalhes string
}

func (c Contrato) Imprimir() {
  fmt.Println("Contrato: ", c.Detalhes)
}