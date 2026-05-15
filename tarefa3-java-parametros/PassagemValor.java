public class PassagemValor {

    public static void alterarNumero(int x) {
        System.out.println("Dentro do metodo (antes de alterar): " + x);
        x = x + 50;
        System.out.println("Dentro do metodo (depois de alterar): " + x);
    }

    public static void main(String[] args) {
        int meuNumero = 10;
        
        System.out.println("No main (antes da chamada): " + meuNumero);
        alterarNumero(meuNumero);
        System.out.println("No main (depois da chamada): " + meuNumero);
    }
}
