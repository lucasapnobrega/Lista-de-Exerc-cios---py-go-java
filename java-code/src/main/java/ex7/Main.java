package ex7;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Escola escola1 = new Escola("Escola A");
        Escola escola2 = new Escola("Escola B");

        Professor professor1 = new Professor("Lucas");
        Professor professor2 = new Professor("Pedro");

        professor1.adicionarEscola(escola1);
        professor1.adicionarEscola(escola2);
        professor2.adicionarEscola(escola1);

        System.out.println(professor1 + " leciona em: " + Arrays.toString(professor1.getEscolas().toArray()));
        System.out.println(professor2 + " leciona em: " + Arrays.toString(professor2.getEscolas().toArray()));
        System.out.println("Professores da " + escola1 + ": " +  Arrays.toString(escola1.getProfessores().toArray()));
        System.out.println("Professores da " + escola2 + ": " +  Arrays.toString(escola2.getProfessores().toArray()));
    }
}

