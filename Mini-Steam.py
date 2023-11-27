class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos  

class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

class ArvoreJogos:
    def __init__(self):
        self.raiz = None

    def inserir(self, jogo):
        if not self.raiz:
            self.raiz = NoJogo(jogo)
        else:
            self._inserir_recursivo(self.raiz, jogo)

    def _inserir_recursivo(self, no_atual, jogo):
        if jogo.preco < no_atual.jogo.preco:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoJogo(jogo)
            else:
                self._inserir_recursivo(no_atual.esquerda, jogo)
        else:
            if no_atual.direita is None:
                no_atual.direita = NoJogo(jogo)
            else:
                self._inserir_recursivo(no_atual.direita, jogo)

    def _buscar_por_preco_recursivo(self, no_atual, preco, resultados):
        if no_atual:
            if no_atual.jogo.preco == preco:
                resultados.append(no_atual.jogo)
            if preco < no_atual.jogo.preco:
                self._buscar_por_preco_recursivo(no_atual.esquerda, preco, resultados)
            else:
                self._buscar_por_preco_recursivo(no_atual.direita, preco, resultados)

    def buscar_por_preco(self, preco):
        resultados = []
        self._buscar_por_preco_recursivo(self.raiz, preco, resultados)
        return resultados

    def _busca_por_faixa_preco_recursivo(self, no_atual, preco_minimo, preco_maximo, resultados):
        if no_atual:
            if preco_minimo <= no_atual.jogo.preco <= preco_maximo:
                resultados.append(no_atual.jogo)
            if preco_minimo < no_atual.jogo.preco:
                self._busca_por_faixa_preco_recursivo(no_atual.esquerda, preco_minimo, preco_maximo, resultados)
            if preco_maximo > no_atual.jogo.preco:
                self._busca_por_faixa_preco_recursivo(no_atual.direita, preco_minimo, preco_maximo, resultados)

    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
        resultados = []
        self._busca_por_faixa_preco_recursivo(self.raiz, preco_minimo, preco_maximo, resultados)
        return resultados

class HashGeneros:
    def __init__(self):
        self.genero_para_jogos = {}

    def adicionar_jogo(self, jogo):
        for genero in jogo.generos:
            if genero not in self.genero_para_jogos:
                self.genero_para_jogos[genero] = [jogo.jogo_id]
            else:
                self.genero_para_jogos[genero].append(jogo.jogo_id)

    def obter_jogos(self, genero):
        if genero in self.genero_para_jogos:
            return self.genero_para_jogos[genero]
        else:
            return []

class MotorBuscaJogos:
    def __init__(self):
        self.catalogo_jogos = ArvoreJogos()
        self.generos = HashGeneros()


# Função para adicionar jogos ao MotorBuscaJogos
def adicionar_jogos(motor_busca, *jogos):
    for jogo in jogos:
        motor_busca.catalogo_jogos.inserir(jogo)
        motor_busca.generos.adicionar_jogo(jogo)

# Função para realizar buscas por preço
def buscar_jogos_por_preco(motor_busca, preco):
    resultados = motor_busca.catalogo_jogos.buscar_por_preco(preco)
    for jogo in resultados:
        print(f"Jogo encontrado: {jogo.titulo} - Preço: R${jogo.preco}")

# Função para realizar buscas por faixa de preço
def buscar_jogos_por_faixa_preco(motor_busca, preco_min, preco_max):
    resultados = motor_busca.catalogo_jogos.busca_por_faixa_preco(preco_min, preco_max)
    for jogo in resultados:
        print(f"Jogo encontrado: {jogo.titulo} - Preço: R${jogo.preco}")

# Criando os jogos
jogo1 = Jogo(1, "The Witcher 3", "CD Projekt Red", 60, ["RPG", "Ação"])
jogo2 = Jogo(2, "Hades", "Supergiant Games", 25, ["Roguelike", "Ação"])
jogo3 = Jogo(3, "Stardew Valley", "ConcernedApe", 15, ["Simulação", "Indie"])
jogo4 = Jogo(4, "Civilization VI", "Firaxis Games", 40, ["Estratégia"])

# Criando o MotorBuscaJogos
motor_busca = MotorBuscaJogos()

# Adicionando os jogos
adicionar_jogos(motor_busca, jogo1, jogo2, jogo3, jogo4)

# Realizando as buscas
buscar_jogos_por_preco(motor_busca, 25)
buscar_jogos_por_faixa_preco(motor_busca, 20, 50)


def buscar_jogo_por_preco(motor_busca):
    print("Escolha o tipo de busca:")
    print("1. Busca por preço simples")
    print("2. Busca por faixa de preço")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        preco = int(input("Digite o preço que deseja buscar: "))
        resultados = motor_busca.catalogo_jogos.buscar_por_preco(preco)
        if resultados:
            print("Jogos encontrados:")
            for jogo in resultados:
                print(f"{jogo.titulo} - Preço: R${jogo.preco}")
        else:
            print("Nenhum jogo encontrado com esse preço.")
    elif opcao == "2":
        preco_min = int(input("Digite o preço mínimo: "))
        preco_max = int(input("Digite o preço máximo: "))
        resultados = motor_busca.catalogo_jogos.busca_por_faixa_preco(preco_min, preco_max)
        if resultados:
            print("Jogos encontrados na faixa de preço:")
            for jogo in resultados:
                print(f"{jogo.titulo} - Preço: R${jogo.preco}")
        else:
            print("Nenhum jogo encontrado nessa faixa de preço.")
    else:
        print("Opção inválida.")

# Exemplo de uso
buscar_jogo_por_preco(motor_busca)
