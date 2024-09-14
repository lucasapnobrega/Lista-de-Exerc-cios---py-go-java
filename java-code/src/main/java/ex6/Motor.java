package ex6;

public class Motor {
    private String tipo;

    public Motor(String tipo) {
        this.tipo = tipo;
    }

    public String exibirTipo() {
        return "Tipo de motor: " + tipo;
    }
}
