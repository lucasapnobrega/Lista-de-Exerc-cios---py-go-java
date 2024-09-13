package main

type FuncionarioHorista struct {
	Nome             string
	HorasTrabalhadas float64
	ValorHora        float64
}

func (f FuncionarioHorista) CalcularSalario() float64 {
	return f.HorasTrabalhadas * f.ValorHora
}