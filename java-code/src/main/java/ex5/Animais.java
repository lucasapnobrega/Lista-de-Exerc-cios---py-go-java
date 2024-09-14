package ex5;

class Cachorro extends Animal {
    @Override
    String som() {
        return "Au Au";
    }
}

class Gato extends Animal {
    @Override
    String som() {
        return "Miau";
    }
}
