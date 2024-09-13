package main

import "fmt"

func main() {
	produto1 := Produto{"Produto A", 120.00}
	produto2 := Produto{"Produto B", 50.00}

	produto3 := produto1.Somar(produto2)

	fmt.Println(produto1) 
	fmt.Println(produto2) 
	fmt.Println(produto3)
}