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
    volta = 0
    if comeca_jogando: # Se o player começar
        while True: # Roda enquanto a partida tiver valor de False
            volta += 1 # Contador para minimizara computação dos laços desnecessariamente
            jogo.printar_tabuleiro()
            if volta >= 5: # Define se deu velha
                resultado = jogo.ganhou(opcao='X')
                if not resultado:
                    jogo.printar_tabuleiro()
                    print('Deu velha')
                    break
            tratamento_erro = True
            while tratamento_erro:
                tratamento_erro = jogo.escolha_pessoa() # Realiza a jogada do player e trata os erros
            if volta >= 2:
                resultado = jogo.ganhou(opcao='O')
                if resultado:
                    jogo.printar_tabuleiro()
                    print('O player ganhou')
                    break
            jogo.jogar_pc() # Realiza a jogada da máquina
            if volta >= 2:
                resultado = jogo.ganhou(opcao='X')
                if resultado:
                    jogo.printar_tabuleiro()
                    print('A máquina ganhou')
                    break
    else: # A máquina começa
        while True: # Roda enquanto a partida tiver valor de False
            volta += 1 # Contador para minimizara computação dos laços desnecessariamente
            if volta >= 5: # Vai definir se Deu Velha
                resultado = jogo.ganhou(opcao='X')
                if not resultado:
                    jogo.printar_tabuleiro()
                    print('Deu velha')
                    break
            jogo.jogar_pc() # Realiza a jogada da máquina
            jogo.printar_tabuleiro()
            if volta >= 2:
                resultado = jogo.ganhou(opcao='O')
                if resultado:
                    jogo.printar_tabuleiro()
                    print('A máquina ganhou')
                    break
            tratamento_erro = True
            while tratamento_erro:
                tratamento_erro = jogo.escolha_pessoa() # Realiza a jogada do player e trata os erros
            if volta >= 2:
                resultado = jogo.ganhou(opcao='X')
                if resultado:
                    jogo.printar_tabuleiro()
                    print('O player ganhou')
                    break
    loop = jogo.deve_continuar()
print('Obrigado por jogar :)')