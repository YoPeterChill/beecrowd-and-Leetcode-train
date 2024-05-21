def contar_respostas_corretas(T, respostas):
    contador = 0
    for resposta in respostas:
        if resposta == T:
            contador += 1
    return contador

T = int(input().strip())
respostas = list(map(int, input().strip().split()))
resultado = contar_respostas_corretas(T, respostas)
print(resultado)
