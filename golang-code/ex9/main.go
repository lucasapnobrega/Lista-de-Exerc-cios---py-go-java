package main

func main() {
	var r Imprimivel = Relatorio{Conteudo: "Relatório Anual"}
	var c Imprimivel = Contrato{Detalhes: "Contrato de Trabalho"}

	r.Imprimir()
	c.Imprimir()
}