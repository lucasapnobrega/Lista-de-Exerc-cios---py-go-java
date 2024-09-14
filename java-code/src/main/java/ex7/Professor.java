package ex7;

import java.util.ArrayList;
import java.util.List;

public class Professor {
    private String nome;
    private List<Escola> escolas;

    public Professor(String nome) {
        this.nome = nome;
        this.escolas = new ArrayList<>();
    }

    public void adicionarEscola(Escola escola) {
        if (!escolas.contains(escola)) {
            escolas.add(escola);
            escola.adicionarProfessor(this);
        }
    }

    public List<Escola> getEscolas() {
        return escolas;
    }

    @Override
    public String toString() {
        return nome;
    }
}
