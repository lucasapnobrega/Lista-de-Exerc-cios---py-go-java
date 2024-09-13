package main

func main() {
	empresa := &Empresa{Nome: "Tech"}

	empregado1 := &Empregado{Nome: "João", Cargo: "Desenvolvedor", Salario: 70000}
	empregado2 := &Empregado{Nome: "Mario", Cargo: "Analista", Salario: 60000}

	empresa.AdicionarEmpregado(empregado1)
	empresa.AdicionarEmpregado(empregado2)

	println("Empregados da", empresa.Nome+":")
	empresa.ListarEmpregados()
}