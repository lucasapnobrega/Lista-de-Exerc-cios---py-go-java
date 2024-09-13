package main

import (
	"sync"
)

type Configuracao struct {
	URL string
}

var instancia *Configuracao
var once sync.Once

func GetInstancia() *Configuracao {
	once.Do(func() {
		instancia = &Configuracao{}
	})
	
	return instancia
}