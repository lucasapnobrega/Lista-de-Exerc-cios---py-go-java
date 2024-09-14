package ex3;

public class ContaBancaria {
    private double saldo;
    private String titular;

    public ContaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
            System.out.printf("Depositado: R$ %.2f. Saldo atual: R$ %.2f%n", valor, saldo);
        } else {
            System.out.println("Valor do depósito deve ser positivo.");
        }
    }

    public void sacar(double valor) {
        if (valor > 0) {
            if (valor <= saldo) {
                saldo -= valor;
                System.out.printf("Sacado: R$ %.2f. Saldo atual: R$ %.2f%n", valor, saldo);
            } else {
                System.out.println("Saldo insuficiente.");
            }
        } else {
            System.out.println("Valor do saque deve ser positivo.");
        }
    }

    public void exibirSaldo() {
        System.out.printf("Saldo atual: R$ %.2f%n", saldo);
    }
}
