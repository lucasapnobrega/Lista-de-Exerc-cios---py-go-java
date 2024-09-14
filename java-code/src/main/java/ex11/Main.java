package ex11;

public class Main {
    public static void main(String[] args) {
        Funcionario horista = new FuncionarioHorista("Hiago", 120, 25);
        Funcionario assalariado = new FuncionarioAssalariado("Caio", 2500);

        System.out.println("Salário do " + horista.nome + ": " + horista.calcularSalario());
        System.out.println("Salário da " + assalariado.nome + ": " + assalariado.calcularSalario());
    }
}

