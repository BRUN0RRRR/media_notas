while True:
    nota1 = int(input("Entre com a sua primeira nota: "))
    nota2 = int(input("Entre com a sua segunda nota: "))
    nota3 = int(input("Entre com a sua terceira nota: "))
    soma = nota1 + nota2 + nota3

    if soma >= 180:
        print("Sua nota é", soma)
        print("Aprovado!")
    else:
        print("Sua nota é", soma)
        print("Reprovado!")

    resposta = input("Deseja continuar? [S/N]: ")
    if resposta.upper() == "N":
        break
