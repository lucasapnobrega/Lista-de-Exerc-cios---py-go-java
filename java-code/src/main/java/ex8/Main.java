package ex8;

public class Main {
    public static void main(String[] args) {
        Empresa empresa = new Empresa("Tech");

        Empregado empregado1 = new Empregado("João", "Desenvolvedor", 3000);
        Empregado empregado2 = new Empregado("Marcos", "Engenheiro", 4000);

        empresa.adicionarEmpregado(empregado1);
        empresa.adicionarEmpregado(empregado2);

        System.out.println("Empregados da " + empresa.getNome() + ":");
        empresa.listarEmpregados();
    }
}

