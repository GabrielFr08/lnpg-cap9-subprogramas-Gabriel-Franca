# Sistema Bancário Simples com Modularização

def mostrar_menu():
    print("\n--- BANCO IFAL ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")
    print("------------------")

def ler_opcao():
    return input("Escolha uma opção: ")

def realizar_deposito(saldo, historico):
    valor = float(input("Digite o valor do depósito: R$ "))
    if valor > 0:
        saldo += valor
        historico.append(f"Depósito: +R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")
    return saldo

def realizar_saque(saldo, historico):
    valor = float(input("Digite o valor do saque: R$ "))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        historico.append(f"Saque: -R$ {valor:.2f}")
        print("Saque realizado com sucesso!")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        print("Valor inválido.")
    return saldo

def exibir_extrato(saldo, historico):
    print("\n--- EXTRATO ---")
    if not historico:
        print("Nenhuma movimentação.")
    else:
        for mov in historico:
            print(mov)
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("---------------")

def iniciar_sistema():
    saldo_atual = 0.0
    extrato_historico = []
    
    while True:
        mostrar_menu()
        opcao = ler_opcao()
        
        if opcao == '1':
            saldo_atual = realizar_deposito(saldo_atual, extrato_historico)
        elif opcao == '2':
            saldo_atual = realizar_saque(saldo_atual, extrato_historico)
        elif opcao == '3':
            exibir_extrato(saldo_atual, extrato_historico)
        elif opcao == '4':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()
