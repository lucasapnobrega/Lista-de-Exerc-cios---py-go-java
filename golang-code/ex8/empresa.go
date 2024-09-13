package main

type Empresa struct {
	Nome       string
	Empregados []*Empregado
}

func (e *Empresa) AdicionarEmpregado(empregado *Empregado) {
	e.Empregados = append(e.Empregados, empregado)
}

func (e *Empresa) ListarEmpregados() {
	for _, empregado := range e.Empregados {
		println(empregado.String())
	}
}