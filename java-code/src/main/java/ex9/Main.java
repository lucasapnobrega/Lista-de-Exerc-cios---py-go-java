package ex9;

public class Main {
    public static void main(String[] args) {
        Imprimivel relatorio = new Relatorio("Relatório X");
        Imprimivel contrato = new Contrato("Contrato Y");

        relatorio.imprimir();
        contrato.imprimir();
    }
}

