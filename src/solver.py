def eliminacao_gaussiana(matriz_coeficientes, termos_independentes):
    quantidade_variaveis = len(matriz_coeficientes)
    
    # Eliminação para transformar a matriz em triangular superior
    for linha_pivo in range(quantidade_variaveis):
        for linha_atual in range(linha_pivo + 1, quantidade_variaveis):
            if matriz_coeficientes[linha_atual][linha_pivo] != 0:
                multiplicador = matriz_coeficientes[linha_atual][linha_pivo] / matriz_coeficientes[linha_pivo][linha_pivo]
                for coluna in range(linha_pivo, quantidade_variaveis):
                    matriz_coeficientes[linha_atual][coluna] -= multiplicador * matriz_coeficientes[linha_pivo][coluna]
                termos_independentes[linha_atual] -= multiplicador * termos_independentes[linha_pivo]

    # Substituição regressiva para encontrar as soluções
    solucoes = [0] * quantidade_variaveis
    for linha in range(quantidade_variaveis - 1, -1, -1):
        valor = termos_independentes[linha]
        for coluna in range(linha + 1, quantidade_variaveis):
            valor -= matriz_coeficientes[linha][coluna] * solucoes[coluna]
        solucoes[linha] = valor / matriz_coeficientes[linha][linha]

    return solucoes

def resolver_sistema_linear(matriz_coeficientes, termos_independentes):
    # Função principal chamada pela interface
    return eliminacao_gaussiana(matriz_coeficientes, termos_independentes)