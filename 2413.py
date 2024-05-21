def calcular_cliques_primeiro_link(t):
    return 4 * t
t = int(input().strip())

if 1 <= t <=1000:
    resultado = calcular_cliques_primeiro_link(t)
    print(resultado)
