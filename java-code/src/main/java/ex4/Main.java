package ex4;

public class Main {
    public static void main(String[] args) {
        Animal cachorro = new Cachorro();
        Animal gato = new Gato();

        System.out.println(cachorro.som());
        System.out.println(gato.som());
    }
}

