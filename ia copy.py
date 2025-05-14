import heapq
import os

def ler_instancia(ia):
    if not os.path.exists(ia):
        exit(1)
    with open(ia, 'r') as f:
        linhas = f.read().splitlines()
    n = int(linhas[0])
    tabuleiro = [list(linha.upper()) for linha in linhas[1:]]
    return n, tabuleiro

def calcular_dano(tabuleiro, n):
    dano = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if tabuleiro[i][j] == 'T':
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n:
                            if tabuleiro[ni][nj] != 'T':
                                dano[ni][nj] += 10
    return dano

def encontrar_caminho(tabuleiro, dano, n):
    direcoes = {'N': (-1, 0), 'S': (1, 0), 'L': (0,1), 'O': (0, -1)}
    visitado = [[False]*n for _ in range(n)]
    heap = [(dano[0][0], 0, 0, '')]
    while heap:
        dano_atual, x, y, caminho = heapq.heappop(heap)
        if (x, y) == (n-1, n-1):
            return caminho, dano_atual
        if visitado[x][y]:
            continue
        visitado[x][y] = True
        for dir, (dx, dy) in direcoes.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visitado[nx][ny] and tabuleiro[nx][ny] != 'T':
                heapq.heappush(heap, (dano_atual + dano[nx][ny], nx, ny, caminho + dir))
    return None, float('inf')

def resolver_instancia(nome_entrada, nome_saida):
    n, tabuleiro = ler_instancia(nome_entrada)
    dano = calcular_dano(tabuleiro, n)
    caminho, dano_total = encontrar_caminho(tabuleiro, dano, n)

    with open(nome_saida, 'w') as f:
        if caminho is None:
            f.write("SEM CAMINHO\nDano total: INFINITO")
            print("SEM CAMINHO")
            print("Danot toal: INFINITO")
        else:
            f.write(f"{caminho}\nDano total: {dano_total}")
            print(f"Caminho: {caminho}")
            print(f"Dano total: {dano_total}")


entrada = input("Digite o nome do arquivo de entrada (ex: inst01.in ou instg12.in): ").strip()
saida = input("Digite o nome do arquivo de saída (ex: sol01.out ou solg12.out): ").strip()

resolver_instancia(entrada, saida)

