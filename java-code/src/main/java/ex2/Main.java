package ex2;

public class Main {
    public static void main(String[] args) {
        Carro carro = new Carro("Honda", "Civic", 2022);

        carro.acelerar(40);
        carro.acelerar(60);
        carro.frear(70);
        carro.exibirVelocidade();
        carro.frear(50);
    }
}
