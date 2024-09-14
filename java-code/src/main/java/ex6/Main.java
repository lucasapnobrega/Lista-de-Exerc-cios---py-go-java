package ex6;

public class Main {
    public static void main(String[] args) {
        Motor motor = new Motor("V8");
        Carro carro = new Carro("Volswagen", "Golf", motor);

        System.out.println(carro.exibirDetalhes());
    }
}
