from jogo_func import *

jogo = Jogo()
jogo.player_comeca()
jogo.printar_tabuleiro()
jogo.jogar_pc()
jogo.printar_tabuleiro()
a = jogo.escolha_pessoa()
jogo.printar_tabuleiro()
jogo.ganhou(opcao='O')