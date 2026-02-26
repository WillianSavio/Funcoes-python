def soma(n1, n2):
    return n1 + n2

resultado_soma = soma(12, 13)
print(f"Soma: {resultado_soma}")

def subtrair(n1, n2):
    return n1 - n2

resultado_subtrair = subtrair(8, 3)
print(f"Subtração: {resultado_subtrair}")


def divisao (n1, n2):
    return n1 / n2

resultado_divisao = divisao(450, 3)
print(f"Divisão: {resultado_divisao}")

def multiplicacao(n1, n2):
    return n1 * n2

resultado_multiplicacao = multiplicacao(2, 1)
print(f"Multiplicação: {resultado_multiplicacao}")

def porcentagem(valor, percentual):
    return (valor * percentual) / 100

resultado_porcentual = porcentagem(1000, 10)
print(f"Porcentagem: {resultado_porcentual}")
print(f"10% de 100 é {resultado_porcentual}")
