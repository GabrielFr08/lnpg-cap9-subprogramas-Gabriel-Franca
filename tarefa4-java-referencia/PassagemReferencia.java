class Produto {
    String nome;
    double preco;

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }
}

public class PassagemReferencia {

    public static void aplicarDesconto(Produto p) {
        System.out.println("No metodo (antes do desconto): R$ " + p.preco);
        p.preco = p.preco * 0.90; // Aplica 10% de desconto
        System.out.println("No metodo (depois do desconto): R$ " + p.preco);
    }

    public static void main(String[] args) {
        Produto meuProduto = new Produto("Teclado Mecanico", 300.00);
        
        System.out.println("No main (antes da chamada): R$ " + meuProduto.preco);
        aplicarDesconto(meuProduto);
        System.out.println("No main (depois da chamada): R$ " + meuProduto.preco);
    }
}
