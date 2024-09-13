package main

type FuncionarioAssalariado struct {
	Nome          string
	SalarioMensal float64
}

func (f FuncionarioAssalariado) CalcularSalario() float64 {
	return f.SalarioMensal
}