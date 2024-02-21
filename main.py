from jogo_func import *

loop = True
while loop:
    jogo = Jogo()
    comeca_jogando = jogo.player_comeca()
    if comeca_jogando:
        print('Player: O\nMáquina: X')
    else:
        print('Player: X\nMáquina: O')
    volta = 0
    if comeca_jogando: # Se o player começar
        partida = False
        while not partida:
            volta += 1
            jogo.printar_tabuleiro()
            continuar = True
            while continuar:
                continuar = jogo.escolha_pessoa()
            if volta >= 4:
                partida = jogo.ganhou()
            jogo.jogar_pc()
            if volta >= 4:
                partida = jogo.ganhou()
    else:
        partida = False
        while not partida:
            volta += 1
            jogo.jogar_pc()
            jogo.printar_tabuleiro()
            if volta >= 4:
                partida = jogo.ganhou()
            continuar = True
            while continuar:
                continuar = jogo.escolha_pessoa()
            if volta >= 4:
                partida = jogo.ganhou()
    break