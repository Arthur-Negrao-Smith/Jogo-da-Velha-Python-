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
        ganhar = False
        while not ganhar: # vai rodar enquando (ganhar) for igual a False
            for linha in range(0, 3):
                itens = ''
                for coluna in range(0, 3):
                    itens += self.tabuleiro[linha][coluna] # Vai checar todas as linhas para saber se ganhou guardando temporariamente na variável
                if itens == opcao*3:
                    ganhar = True
                    break
            for coluna in range(0, 3):
                itens = ''
                for linha in range(0, 3):
                    itens += self.tabuleiro[linha][coluna] # Vai checar todas as colunas e guarda uma por uma temporariamente na variável
                if itens == opcao*3:
                    ganhar = True
                    break
            if self.tabuleiro[0][0] == opcao and self.tabuleiro[0][0] == self.tabuleiro[1][1] and self.tabuleiro[0][0] == self.tabuleiro[2][2]: # Vai checar a diagonal da esquerda superior até a direita inferior
                ganhar = True
                break
            elif self.tabuleiro[0][2] == opcao and self.tabuleiro[0][2] == self.tabuleiro[1][1] and self.tabuleiro[0][2] == self.tabuleiro[2][0]: # vai checar a diagonal da esquerda inferior até a direita superior
                ganhar = True
                break
            else:
                break # Quebra o laço e (ganhar) ainda é False
        return ganhar

    def player_comeca(self) -> bool:
        """Define quem começa a jogar"""
        comeca = randint(1, 2)
        if comeca == 1:
            print('Player começa')
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
        print(f"{self.glamour:=^7}")
        for linha in self.tabuleiro:
                print(f'{linha[0]}  {linha[1]}  {linha[2]} ')
        print(f"{self.glamour:=^7}")
    
    def escolha_pessoa(self) -> bool:
        """Onde a pessoa vai escolher"""
        try:
            while True:
                self.jogada_pes_linha = int(input('Escolha sua linha: [1, 2, 3]: '))
                self.jogada_pes_linha -= 1
                if self.jogada_pes_linha == 0 or self.jogada_pes_linha == 1 or self.jogada_pes_linha == 2:
                    break
                else:
                    print('Escolha inválida')
            while True:
                self.jogada_pes_coluna = int(input('Escolha uma coluna [1, 2, 3]: '))
                self.jogada_pes_coluna -= 1
                if self.jogada_pes_coluna == 0 or self.jogada_pes_coluna == 1 or self.jogada_pes_coluna == 2:
                    break
                else:
                    print('Escolha inválida')
            if self.tabuleiro[self.jogada_pes_linha][self.jogada_pes_coluna] == '0':
                self.tabuleiro[self.jogada_pes_linha][self.jogada_pes_coluna] = self.opcao_player
                return False
            else:
                print('Espaço já ocupado')
                return True
        except:
            print('Valor inválido')
            return True
        
    def jogar_pc(self) -> None:
        """Define a jogada do PC"""
        while True:
            self.jogada_pc_tipo = self.opcao_pc
            self.jogada_pc_linha = randint(0, 2)
            self.jogada_pc_coluna = randint(0, 2)
            if self.tabuleiro[self.jogada_pc_linha][self.jogada_pc_coluna] == '0':
                self.tabuleiro[self.jogada_pc_linha][self.jogada_pc_coluna] = self.jogada_pc_tipo
                break

    def deve_continuar(self) -> bool:
        """Pergunta se a pessoa deseja continuar"""
        from time import sleep
        while True:
            resposta = str(input('Você deseja jogar novamente? [S/N] ')).strip()
            if resposta == '':
                print('Resposta inválida')
            elif resposta in 'SsSIMSimsim' or resposta in 'NnNÃOnãonaoNAONão':
                while True:
                    if resposta in 'SsSIMSimsim':
                        print('CARREGANDO...')
                        for c in range(0, 4):
                            sleep(0.5)
                            print('')
                        continua = True
                        break
                    elif resposta in 'NnNÃOnãonao':
                        print('FECHANDO JOGO...')
                        sleep(0.5)
                        continua = False
                        break
                    print('Resposta inválida')
                    break
                break
            else:
                print('Resposta inválida')
        return continua