package ex8;

import java.util.ArrayList;
import java.util.List;

public class Empresa {
    private String nome;
    private List<Empregado> empregados;

    public Empresa(String nome) {
        this.nome = nome;
        this.empregados = new ArrayList<>();
    }

    public void adicionarEmpregado(Empregado empregado) {
        empregados.add(empregado);
    }


    public void listarEmpregados() {
        for (Empregado empregado : empregados) {
            System.out.println(empregado);
        }
    }

    public String getNome() {
        return nome;
    }
}
