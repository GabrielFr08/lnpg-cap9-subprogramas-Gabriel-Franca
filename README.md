# Atividade Prática - Capítulo 9: Subprogramas

**Nome Completo:** Gabriel França Bento Catunda
**Turma:** Linguagem de Programação (2º Período)

## Tarefa 1 e 2: Comparação Monolítico vs Modularizado
Nas versões monolíticas, o código fica extenso e difícil de ler, pois todas as regras de negócio e entradas/saídas estão amontoadas em um único bloco. Nas versões modularizadas, a **legibilidade** e a **clareza do fluxo** melhoram imensamente. O método `main` passa a apenas coordenar o fluxo, chamando métodos menores. O **tamanho dos métodos** reduz bastante, garantindo **alta coesão** (cada função faz apenas uma coisa) e facilitando a **manutenção** e a **reutilização**. No Python (Tarefa 2), as partes de cálculo de desconto e formatação de cupom eram altamente repetitivas, e ao virarem funções, ficaram reaproveitáveis.

## Tarefa 3: Passagem de Parâmetros por Valor (Java)
**Por que o valor original não mudou?** Porque a variável `x` dentro do método é apenas uma cópia local da variável original. 
**O que significa "passagem por valor"?** Significa que o valor primitivo armazenado na variável é copiado e enviado para o método, não a variável original em si.
**Qual valor foi copiado?** O valor numérico '10' foi copiado para o espaço de memória do método `alterarNumero`.

## Tarefa 4: Objetos e Referência em Java
**1. Java possui passagem por referência verdadeira?** Não, o Java utiliza estritamente passagem por valor para tudo.
**2. O que exatamente é copiado na chamada?** Quando passamos um objeto, o que é copiado (passado por valor) é o **endereço de memória** (a referência) que aponta para aquele objeto.
**3. Por que alterações no objeto permanecem?** Porque a cópia da referência ainda aponta para o mesmo objeto original na memória Heap. Modificar os atributos através dessa cópia afeta o objeto real.

## Tarefa 5: Projeto Livre - Sistema Bancário
**Justificativa:** O sistema foi dividido para separar a interface (menu) das regras de negócio (saque, depósito).
**Dificuldades:** Manter o saldo atualizado entre as diferentes funções sem utilizar variáveis globais.
**Vantagens percebidas:** É muito mais fácil adicionar novas funcionalidades (como transferência) criando um novo subprograma, sem risco de quebrar o que já funciona.

**Diagrama de Chamadas:**
`iniciar_sistema()` 
  ├── `mostrar_menu()`
  ├── `ler_opcao()`
  ├── `realizar_deposito(saldo)` -> retorna novo saldo
  ├── `realizar_saque(saldo)` -> retorna novo saldo
  └── `exibir_extrato(historico)`
