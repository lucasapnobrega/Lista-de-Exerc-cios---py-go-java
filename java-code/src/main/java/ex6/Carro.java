package ex6;

public class Carro {
    private String marca;
    private String modelo;
    private Motor motor;

    public Carro(String marca, String modelo, Motor motor) {
        this.marca = marca;
        this.modelo = modelo;
        this.motor = motor;
    }

    public String exibirDetalhes() {
        return "Marca: " + marca + ", Modelo: " + modelo + ", " + motor.exibirTipo();
    }

    public static void main(String[] args) {
        Motor motor = new Motor("V8");
        Carro carro = new Carro("Ford", "Mustang", motor);

        System.out.println(carro.exibirDetalhes());
    }
}
