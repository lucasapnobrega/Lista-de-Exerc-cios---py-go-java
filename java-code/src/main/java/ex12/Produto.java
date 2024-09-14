package ex12;

public class Produto {
    private String nome;
    private double preco;

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public Produto somar(Produto outro) {
        return new Produto(this.nome + " e " + outro.nome, this.preco + outro.preco);
    }

    @Override
    public String toString() {
        return nome + " - R$" + String.format("%.2f", preco);
    }
}
