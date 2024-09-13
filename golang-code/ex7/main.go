package main

import "fmt"

func main() {
	escola1 := &Escola{Nome: "Escola X"}
	escola2 := &Escola{Nome: "Escola Y"}

	professor1 := &Professor{Nome: "Lucas"}
	professor2 := &Professor{Nome: "Pedro"}

	professor1.AdicionarEscola(escola1)
	professor1.AdicionarEscola(escola2)
	professor2.AdicionarEscola(escola1)

	fmt.Printf("%s leciona em: ", professor1.Nome)
	for e := range professor1.Escolas {
		fmt.Printf("%s ", e.Nome)
	}
	fmt.Println()

	fmt.Printf("%s leciona em: ", professor2.Nome)
	for e := range professor2.Escolas {
		fmt.Printf("%s ", e.Nome)
	}
	fmt.Println()

	fmt.Printf("Professores da %s: ", escola1.Nome)
	for p := range escola1.Professores {
		fmt.Printf("%s ", p.Nome)
	}
	fmt.Println()

	fmt.Printf("Professores da %s: ", escola2.Nome)
	for p := range escola2.Professores {
		fmt.Printf("%s ", p.Nome)
	}
	fmt.Println()
}