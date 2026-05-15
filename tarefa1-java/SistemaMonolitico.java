import java.util.Scanner;

public class SistemaMonolitico {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        for (int i = 0; i < 5; i++) {
            System.out.print("\nNome do " + (i + 1) + "º aluno: ");
            String nome = sc.nextLine();
            
            double soma = 0;
            for (int j = 0; j < 3; j++) {
                System.out.print("Digite a " + (j + 1) + "ª nota: ");
                soma += Double.parseDouble(sc.nextLine());
            }
            
            double media = soma / 3.0;
            String situacao = "";
            
            if (media >= 7.0) situacao = "Aprovado";
            else if (media >= 4.0) situacao = "Recuperacao";
            else situacao = "Reprovado";

            System.out.printf("--- RELATORIO ---\nAluno: %s\nMedia: %.2f\nSituacao: %s\n-----------------\n", nome, media, situacao);
        }
        sc.close();
    }
}
