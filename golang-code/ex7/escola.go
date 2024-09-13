package main

type Escola struct {
	Nome        string
	Professores map[*Professor]bool
}

func (e *Escola) AdicionarProfessor(p *Professor) {
	if e.Professores == nil {
		e.Professores = make(map[*Professor]bool)
	}

	if _, exists := e.Professores[p]; !exists {
		e.Professores[p] = true
	}
}