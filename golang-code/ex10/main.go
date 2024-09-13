package main

import "fmt"

func somarDois(a int, b int) int {
  return a + b
}

func somarTres(a int, b int, c int) int {
  return a + b + c
}

func main() {
  fmt.Println("Soma de 2 e 3:", somarDois(2, 3))
  fmt.Println("Soma de 1, 2 e 3:", somarTres(1, 2, 3))
}