from jogo_func import *

loop = True
while loop:
    jogo = Jogo()
    comeca_jogando = jogo.player_comeca()
    jogo.printar_tabuleiro()
    jogo.jogar_pc()
    jogo.printar_tabuleiro()
    a = jogo.escolha_pessoa()
    jogo.printar_tabuleiro()
    jogo.ganhou(opcao='O')