def ler_produto():
    nome = input("Nome do produto: ")
    qtd = int(input("Quantidade: "))
    preco = float(input("Preço unitário: R$ "))
    return nome, qtd, preco

def calcular_subtotal(qtd, preco):
    return qtd * preco

def calcular_desconto(subtotal):
    if subtotal > 500:
        return subtotal * 0.10
    elif subtotal > 200:
        return subtotal * 0.05
    return 0.0

def calcular_total(subtotal, desconto):
    return subtotal - desconto

def imprimir_cupom(nome, qtd, preco, subtotal, desconto, total):
    print("\n" + "="*30)
    print(f"CUPOM FISCAL - {nome.upper()}")
    print("="*30)
    print(f"Qtd: {qtd} un x R$ {preco:.2f}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print("-" * 30)
    print(f"TOTAL FINAL: R$ {total:.2f}")
    print("="*30 + "\n")

def main():
    nome, qtd, preco = ler_produto()
    subtotal = calcular_subtotal(qtd, preco)
    desconto = calcular_desconto(subtotal)
    total = calcular_total(subtotal, desconto)
    imprimir_cupom(nome, qtd, preco, subtotal, desconto, total)

if __name__ == "__main__":
    main()
