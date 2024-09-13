package main

import "fmt"

func main() {
	horista := FuncionarioHorista{"Lucas", 170, 20}
	assalariado := FuncionarioAssalariado{"Eduarda", 3000}

	fmt.Printf("Salário do %s: %.2f\n", horista.Nome, horista.CalcularSalario())
	fmt.Printf("Salário da %s: %.2f\n", assalariado.Nome, assalariado.CalcularSalario())
}