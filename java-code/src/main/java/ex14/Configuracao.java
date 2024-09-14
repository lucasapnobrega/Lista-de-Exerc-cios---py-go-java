package ex14;

public class Configuracao {
    private static Configuracao instancia;
    private String url;

    private Configuracao() {

    }

    public static Configuracao getInstancia() {
        if (instancia == null) {
            instancia = new Configuracao();
        }
        return instancia;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getUrl() {
        return url;
    }
}