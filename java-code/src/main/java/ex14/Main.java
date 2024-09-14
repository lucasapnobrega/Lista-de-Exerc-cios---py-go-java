package ex14;

public class Main {
    public static void main(String[] args) {
        Configuracao config1 = Configuracao.getInstancia();
        Configuracao config2 = Configuracao.getInstancia();

        config1.setUrl("http://exemplourl.com");
        System.out.println(config2.getUrl());

        System.out.println(config1 == config2);
    }
}

