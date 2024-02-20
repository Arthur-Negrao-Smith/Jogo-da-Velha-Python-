from random import randint

class Jogo:
    def __init__(self) -> list:
        self.opcoes = {1:'O', 2:'X'}
        self.tabuleiro = [
            ['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0']
            ]
        self.glamour = '='

    def ganhou(self, opcao='O') -> bool:
        """Serve para saber se ganhou"""
        for linha in range(0, 2):
            itens = ''
            for coluna in range(0, 2):
                itens += self.tabuleiro[linha][coluna] # Vai checar todas as linhas para saber se ganhou
            if itens.count(opcao, 0, 2) == 3:
                print('ganhou')

    def player_comeca(self) -> bool:
        """Define quem começa a jogar"""
        comeca = randint(0, 1)
        if comeca == 0:
            print('player começa')
            self.opcao_player = self.opcoes[1]
            self.opcao_pc = self.opcoes[2]
            return True
        else:
            print('Máquina começa')
            self.opcao_player = self.opcoes[2]
            self.opcao_pc = self.opcoes[1]
            return False

    def printar_tabuleiro(self) -> None:
        """Vai printar cada termo do tabuleiro"""
        for linha in self.tabuleiro:
                print(f'{linha[0]}  {linha[1]}  {linha[2]} ')
        print(f"{self.glamour:=^7}")
    
    def escolha_pessoa(self) -> int:
        """Onde a pessoa vai escolher"""
        try:
            self.jogada_pes_linha = int(input('Escolha sua linha: [1, 2, 3]: '))
            self.jogada_pes_linha -= 1
            self.jogada_pes_coluna = int(input('Escolha uma coluna [1, 2, 3]: '))
            self.jogada_pes_coluna -= 1
            self.tabuleiro[self.jogada_pes_linha][self.jogada_pes_coluna] = self.opcao_player
            return False
        except:
            print('Valor inválido')
            return True
        
    def jogar_pc(self) -> list:
        """Define a jogada do PC"""
        self.jogada_pc_tipo = self.opcao_pc
        self.jogada_pc_linha = randint(0, 2)
        self.jogada_pc_coluna = randint(0, 2)
        self.tabuleiro[self.jogada_pc_linha][self.jogada_pc_coluna] = self.jogada_pc_tipo

jogo = Jogo()
jogo.player_comeca()
jogo.printar_tabuleiro()
jogo.jogar_pc()
jogo.printar_tabuleiro()
a = jogo.escolha_pessoa()
jogo.printar_tabuleiro()
jogo.ganhou(opcao='O')