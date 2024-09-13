package main

import "fmt"

func main() {
	conta := ContaBancaria{saldo: 450}

	err := conta.Sacar(500)
	if err != nil {
		fmt.Println(err)
	}
}