package ex10;

public class Main {
    public static void main(String[] args) {
        Calculadora calc = new Calculadora();

        System.out.println("Soma de 10 e 5: " + calc.somar(10, 5));
        System.out.println("Soma de 5, 5 e 10: " + calc.somar(5, 5, 10));
    }
}

