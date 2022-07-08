class JogoDaVelha:

    class Jogador:
        def __init__(self, nome, simbolo=None):
            self.nome = nome
            self.simbolo = simbolo

    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
    
    def tabuleiros(self):
        self.tabuleiroBack = [[0,0,0],[0,0,0],[0,0,0]]
        self.tabuleiroFront = [["        ", "Coluna 1", "Coluna 2", "Coluna 3"],
                               ["Linha 1 ", "   -    ", "   -    ", "   -    "],
                               ["Linha 2 ", "   -    ", "   -    ", "   -    "],
                               ["Linha 3 ", "   -    ", "   -    ", "   -    "]]
        
        return self.tabuleiroBack, self.tabuleiroFront

    def joga(self, jogador):
        self.jogador = jogador
        linha = coluna = 0
        print(jogador.nome+", agora você deverá indicar linha e coluna do tabuleiro, para sua jogada.")
        while linha < 1 or linha > 3 or coluna < 1 or coluna >3:
            try:
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
                if linha < 1 or linha > 3 or coluna < 1 or coluna >3:
                    print("Um ou ambos os valores estão fora da faixa de valores válida.\nAperte a tecla ENTER para tentar novamente:")
                    input()
            except:
                print("Um ou ambos os valores são inválidos.\nAperte a tecla ENTER para tentar novamente:")
                input()

        return linha, coluna
    
    def validar(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

        if self.tabuleiroBack[self.linha-1][self.coluna-1] == 0:
            return True
        else:
            print("Este local do tabuleiro já esta preenchido. Aperte ENTER para jogar novamente.")
            input()
            return False
    
    def preencher(self, linha, coluna, n_jogada, Jogo):
        self.linha = linha
        self.coluna = coluna
        self.Jogo = Jogo
        
        if (n_jogada%2) + 1 == 1:
            self.tabuleiroBack[linha-1][coluna-1] = 1
            self.tabuleiroFront[linha][coluna] = "   "+self.Jogo.jogador1.simbolo+"    "
            return self.tabuleiroFront
        
        else:
            self.tabuleiroBack[linha-1][coluna-1] = -1
            self.tabuleiroFront[linha][coluna] = "   "+self.Jogo.jogador2.simbolo+"    "
            return self.tabuleiroFront
    
    def verificar(self):
        #Verificando linhas
        somaL1 = 0
        somaL2 = 0 
        somaL3 = 0
        for k in range(3):
            somaL1 = somaL1 + self.tabuleiroBack[0][k]
            somaL2 = somaL2 + self.tabuleiroBack[1][k]
            somaL3 = somaL3 + self.tabuleiroBack[2][k]

        #Verificando colunas
        somaC1 = 0 
        somaC2 = 0
        somaC3 = 0
        for l in range(3):
            somaC1 = somaC1 + self.tabuleiroBack[l][0]
            somaC2 = somaC2 + self.tabuleiroBack[l][1]
            somaC3 = somaC3 + self.tabuleiroBack[l][2]
        
        #Verificando diagonais
        somaD1 = self.tabuleiroBack[0][0] + self.tabuleiroBack[1][1] + self.tabuleiroBack[2][2]
        somaD2 = self.tabuleiroBack[2][0] + self.tabuleiroBack[1][1] + self.tabuleiroBack[0][2]

        paraJogo = 0
        for i in range(3):
            for j in range(3):
                if self.tabuleiroBack[i][j] == 0:
                    paraJogo = 1
                    break

        if somaL1 == 3 or somaL2 == 3 or somaL3 == 3 or somaC1 == 3 or somaC2 == 3 or somaC3 == 3 or somaD1 == 3 or somaD2 == 3:
            print("O jogo acabou. "+self.Jogo.jogador1.nome+" venceu!")
            return True
        elif somaL1 == -3 or somaL2 == -3 or somaL3 == -3 or somaC1 == -3 or somaC2 == -3 or somaC3 == -3 or somaD1 == -3 or somaD2 == -3:
            print("O jogo acabou. "+self.Jogo.jogador2.nome+" venceu!")
            return True
        elif paraJogo == 0:
            print("O jogo acabou empatado!")
            return True    
        else:
            print("O jogo continua!")
            return False
