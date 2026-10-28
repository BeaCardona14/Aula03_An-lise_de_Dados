salarioBruto = float(input("Salário: ").replace(",","."))

if salarioBruto >= 2000:
    desconto = salarioBruto * 0.11
else:
    desconto = salarioBruto * 0.09
    salarioFinal = salarioBruto - desconto 
print(f"Salário:{salarioBruto:.2f}")
print(f"Desconto:{salarioBruto:.2f}")
print(f"Salário Final:{salarioBruto:.2f}")
#ALT+SHIFT+SETA P/BAIXO= COPIA A LINHA ACIMA#
