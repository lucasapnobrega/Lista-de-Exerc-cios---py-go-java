package ex2;

public class Carro {
    String marca;
    String modelo;
    int ano;
    int velocidade;

    public Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.velocidade = 0;
    }

    void acelerar(int incremento) {
        velocidade += incremento;
        System.out.println("O carro acelerou. Velocidade atual: " + velocidade + " km/h");
    }

    void frear(int decremento) {
        velocidade -= decremento;
        if (velocidade < 0) {
            velocidade = 0;
        }
        System.out.println("O carro freou. Velocidade atual: " + velocidade + " km/h");
    }

    void exibirVelocidade() {
        System.out.println("Velocidade atual: " + velocidade + " km/h");
    }
}
