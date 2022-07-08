from JogoDaVelha import JogoDaVelha

v = 1 
while v == 1:
    print("JOGO DA VELHA!!!!!!")
    print("Começando o Jogo")

    nome1 = input("Nome do Jogador 1: ")
    nome2 = input("Nome do Jogador 2: ")

    jogador1 = JogoDaVelha.Jogador(nome1)
    jogador2 = JogoDaVelha.Jogador(nome2)

    jogador1.simbolo = input(jogador1.nome+", escolha um símbolo (um caracter) para marcação no tabuleiro: ")
    jogador2.simbolo = input(jogador2.nome+", escolha um símbolo (um caracter) para marcação no tabuleiro: ")
    while jogador2.simbolo == jogador1.simbolo:
        jogador2.simbolo = input(jogador2.nome+", você escolheu o mesmo simbolo que "+jogador1.nome+".\nEscolha outro: ")
    print("\n")

    Jogo = JogoDaVelha(jogador1, jogador2)

    tabuleiroBack = list(Jogo.tabuleiros()[0])
    tabuleiroFront = list(Jogo.tabuleiros()[1])

    print("Apresentamos O TABULEIRO que será mostrado a cada jogada, para guiar os jogadores.\n")

    for i in range(4):
        print(tabuleiroFront[i])
    print("\n")

    a = False
    b = False
    n = 0
    while a == False:
        while b == False:
            if (n%2 + 1) == 1:
                jogadaJ1 = Jogo.joga(jogador1)
                linha = jogadaJ1[0]
                coluna = jogadaJ1[1]
            else:
                jogadaJ2 = Jogo.joga(jogador2)
                linha = jogadaJ2[0]
                coluna = jogadaJ2[1]

            b = Jogo.validar(linha, coluna)

        preenchido = Jogo.preencher(linha, coluna, n, Jogo)
        for j in range(4):
            print(preenchido[j])
        print("\n")
        b = not b
        a = Jogo.verificar()
        n+=1

    v = int(input("""
                Digite:
                1 - Jogar Novamente;
                0 - Sair do Jogo.
                                """))




