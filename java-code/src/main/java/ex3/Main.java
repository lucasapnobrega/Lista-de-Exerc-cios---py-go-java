package ex3;

public class Main {
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria("Lucas", 1500);
        conta.depositar(500);
        conta.sacar(200);
        conta.exibirSaldo();
    }
}

