package main

import "fmt"

type ContaBancaria struct {
	titular string
	saldo   float64
}

func (c *ContaBancaria) Depositar(valor float64) {
	if valor > 0 {
		c.saldo += valor
		fmt.Printf("Depositado: R$ %.2f. Saldo atual: R$ %.2f\n", valor, c.saldo)
	} else {
		fmt.Println("Valor do depósito deve ser positivo.")
	}
}

func (c *ContaBancaria) Sacar(valor float64) {
	if valor > 0 {
		if valor <= c.saldo {
			c.saldo -= valor
			fmt.Printf("Sacado: R$ %.2f. Saldo atual: R$ %.2f\n", valor, c.saldo)
		} else {
			fmt.Println("Saldo insuficiente.")
		}
	} else {
		fmt.Println("Valor do saque deve ser positivo.")
	}
}

func (c ContaBancaria) ExibirSaldo() {
  fmt.Printf("Saldo atual: R$ %.2f\n", c.saldo)
}

func main() {
	conta := ContaBancaria{titular: "Lucas", saldo: 2000}
	conta.Depositar(500)
	conta.Sacar(250)
	conta.ExibirSaldo()
}