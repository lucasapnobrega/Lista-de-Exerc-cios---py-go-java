package ex12;

public class Main {
    public static void main(String[] args) {
        Produto produto1 = new Produto("Produto A", 100);
        Produto produto2 = new Produto("Produto B", 50);

        Produto produto3 = produto1.somar(produto2);

        System.out.println(produto1);
        System.out.println(produto2);
        System.out.println(produto3);
    }
}

