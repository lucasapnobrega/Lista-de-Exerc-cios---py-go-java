package ex15;

public class Main {
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria(200);

        try {
            conta.sacar(300);
        } catch (SaldoInsuficienteException e) {
            System.out.println(e.getMessage());
        }
    }
}

