import java.util.Scanner;

public class SistemaModularizado {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 5; i++) {
            String nome = lerAluno(sc, i + 1);
            double[] notas = lerNotas(sc);
            double media = calcularMedia(notas);
            String situacao = determinarSituacao(media);
            imprimirRelatorio(nome, media, situacao);
        }
        sc.close();
    }

    public static String lerAluno(Scanner sc, int indice) {
        System.out.print("\nNome do " + indice + "º aluno: ");
        return sc.nextLine();
    }

    public static double[] lerNotas(Scanner sc) {
        double[] notas = new double[3];
        for (int i = 0; i < 3; i++) {
            System.out.print("Digite a " + (i + 1) + "ª nota: ");
            notas[i] = Double.parseDouble(sc.nextLine());
        }
        return notas;
    }

    public static double calcularMedia(double[] notas) {
        double soma = 0;
        for (double nota : notas) { soma += nota; }
        return soma / notas.length;
    }

    public static String determinarSituacao(double media) {
        if (media >= 7.0) return "Aprovado";
        else if (media >= 4.0) return "Recuperacao";
        else return "Reprovado";
    }

    public static void imprimirRelatorio(String nome, double media, String situacao) {
        System.out.printf("--- RELATORIO ---\nAluno: %s\nMedia: %.2f\nSituacao: %s\n-----------------\n", nome, media, situacao);
    }
}
