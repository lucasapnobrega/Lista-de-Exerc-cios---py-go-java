package main

import "fmt"

type Relatorio struct {
  Conteudo string
}

func (r Relatorio) Imprimir() {
  fmt.Println("Relatório: ", r.Conteudo)
}