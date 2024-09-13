package main

type Professor struct {
	Nome    string
	Escolas map[*Escola]bool
}

func (p *Professor) AdicionarEscola(e *Escola) {
	if p.Escolas == nil {
		p.Escolas = make(map[*Escola]bool)
	}

	if _, exists := p.Escolas[e]; !exists {
		p.Escolas[e] = true
		e.AdicionarProfessor(p)
	}
}