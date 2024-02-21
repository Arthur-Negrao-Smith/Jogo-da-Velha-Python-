from jogo_func import *

loop = True
while loop:
    jogo = Jogo()
    comeca_jogando = jogo.player_comeca()
    volta = 0
    if comeca_jogando: # Se o player começar
        partida = False
        while not partida:
            volta += 1
            jogo.printar_tabuleiro()
            jogo.escolha_pessoa()
            if volta >= 4:
                partida = jogo.ganhou()
            jogo.jogar_pc()
            if volta >= 4:
                partida = jogo.ganhou()
    else:
        partida = False
        while not partida:
            volta += 1
            jogo.printar_tabuleiro()
            jogo.jogar_pc()
            if volta >= 4:
                partida = jogo.ganhou()
            jogo.escolha_pessoa()
            if volta >= 4:
                jogo.ganhou()
    break