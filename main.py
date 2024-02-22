from jogo_func import *

loop = True
while loop:
    resultado = False # Começa falso, pois ninguém ganhou ainda
    print(f"{' Jogo DA Velha ':.^30}")
    jogo = Jogo()
    print('-='*7)
    comeca_jogando = jogo.player_comeca() # Define quem começa jogando
    print('-='*7)
    if comeca_jogando:
        print('Player: O\nMáquina: X')
    else:
        print('Player: X\nMáquina: O')
    turno = 0 # Contador para minimizará computação dos laços desnecessariamente e identificará se deu velha quando alcançar 9 jogadas
    if comeca_jogando: # Se o player começar
        while True: # Roda enquanto a partida tiver valor de False
            jogo.printar_tabuleiro()
            tratamento_erro = True
            while tratamento_erro:
                tratamento_erro = jogo.escolha_pessoa() # Realiza a jogada do player e trata os erros
            turno += 1 # Contador para minimizará computação dos laços desnecessariamente
            if turno >= 4:
                resultado = jogo.ganhou(opcao='O')
                if resultado:
                    jogo.printar_tabuleiro()
                    print('O player ganhou')
                    break
            if turno == 9: # Define se deu velha
                resultado = jogo.ganhou(opcao='X')
                if not resultado:
                    jogo.printar_tabuleiro()
                    print('Deu velha')
                    break
            jogo.jogar_pc() # Realiza a jogada da máquina
            turno += 1
            if turno >= 4:
                resultado = jogo.ganhou(opcao='X')
                if resultado:
                    jogo.printar_tabuleiro()
                    print('A máquina ganhou')
                    break
    else: # A máquina começa
        while True: # Roda enquanto a partida tiver valor de False
            jogo.jogar_pc() # Realiza a jogada da máquina
            turno += 1 # Contador para minimizara computação dos laços desnecessariamente
            jogo.printar_tabuleiro()
            if turno >= 4:
                resultado = jogo.ganhou(opcao='O')
                if resultado:
                    jogo.printar_tabuleiro()
                    print('A máquina ganhou')
                    break
            tratamento_erro = True
            if turno == 9: # Vai definir se Deu Velha
                resultado = jogo.ganhou(opcao='X')
                if not resultado:
                    jogo.printar_tabuleiro()
                    print('Deu velha')
                    break
            while tratamento_erro:
                tratamento_erro = jogo.escolha_pessoa() # Realiza a jogada do player e trata os erros
            turno += 1
            if turno >= 4:
                resultado = jogo.ganhou(opcao='X')
                if resultado:
                    jogo.printar_tabuleiro()
                    print('O player ganhou')
                    break
    loop = jogo.deve_continuar()
print('Obrigado por jogar :)')