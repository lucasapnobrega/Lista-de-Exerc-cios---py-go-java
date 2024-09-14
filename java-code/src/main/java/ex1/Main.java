package ex1;

public class Main {
    public static void main(String[] args) {
        Carro carro1 = new Carro("Volskwagen", "Gol", 2020);
        Carro carro2 = new Carro("Renault", "Sandero", 2017);

        carro1.exibirDetalhes();
        carro2.exibirDetalhes();
    }
}
