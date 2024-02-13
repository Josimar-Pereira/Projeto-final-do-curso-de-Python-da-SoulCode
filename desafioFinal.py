"""
Neste exemplo, as cinco funções (somar, subtrair, dividir, multiplicar e listar)
são definidas no início do script. Em seguida, é exibido um menu com as opções
disponíveis. Dependendo da escolha do usuário, o programa solicita os parâmetros
necessários para realizar a operação selecionada e exibe o resultado.
A função listar cria uma lista de vantagens do Python e as imprime uma a uma
utilizando um loop for.
"""
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"
def multiplicar(a, b):
    return a * b

def listar():
    vantagens = [
        "Sintaxe simples e legível",
        "Ampla biblioteca padrão",
        "Portabilidade entre plataformas",
        "Suporte a programação orientada a objetos",
        "Grande comunidade de desenvolvedores",
    ]
    for vantagem in vantagens:
        print(vantagem)
print("Bem-vindo ao Menu de Operações!")
print("1. Somar")
print("2. Subtrair")
print("3. Dividir")
print("4. Multiplicar")
print("5. Listar vantagens do Python")
escolha = input("Escolha uma opção (1-5): ")
if escolha == "1":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = somar(num1, num2)
    print("Resultado: ", resultado)
elif escolha == "2":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = subtrair(num1, num2)
    print("Resultado: ", resultado)
elif escolha == "3":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = dividir(num1, num2)
    print("Resultado: ", resultado)
elif escolha == "4":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = multiplicar(num1, num2)
    print("Resultado: ", resultado)
elif escolha == "5":
    print("\nVantagens do Python:")
    listar()
else:
    print("Opção inválida.")