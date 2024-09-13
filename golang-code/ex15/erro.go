package main

type SaldoInsuficienteError struct {
	Mensagem string
}

func (e *SaldoInsuficienteError) Error() string {
	return e.Mensagem
}

type ContaBancaria struct {
	saldo float64
}

func (c *ContaBancaria) Depositar(valor float64) {
	c.saldo += valor
}

func (c *ContaBancaria) Sacar(valor float64) error {
	if valor > c.saldo {
		return &SaldoInsuficienteError{"Saldo insuficiente para a operação"}
	}

	c.saldo -= valor
	return nil
}

func (c *ContaBancaria) ObterSaldo() float64 {
	return c.saldo
}