nome = input("Nome do produto: ")
qtd = int(input("Quantidade: "))
preco = float(input("Preço unitário: R$ "))

subtotal = qtd * preco
desconto = 0.0

if subtotal > 500:
    desconto = subtotal * 0.10
elif subtotal > 200:
    desconto = subtotal * 0.05

total = subtotal - desconto

print("\n" + "="*30)
print(f"CUPOM FISCAL - {nome.upper()}")
print("="*30)
print(f"Qtd: {qtd} un x R$ {preco:.2f}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print("-" * 30)
print(f"TOTAL FINAL: R$ {total:.2f}")
print("="*30 + "\n")
