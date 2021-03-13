import chess
from pieces import pieceValue
import random
import evaluation as ev
from jogo import Jogo,Jogador
from minimax import melhor_jogada_agente_poda


class Game(Jogo):
    def __init__(self, board, playerColor):
        self.board = board
        self.playerColor = playerColor

    def turno(self):
        return self.board.turn

    def jogar(self, localizacao):
        aux = self.board.copy()
        aux.push(chess.Move.from_uci(localizacao))
        return Game(chess.Board(aux.fen()), self.playerColor)

    def jogos_validos(self):
        return list(self.board.legal_moves)

    def venceu(self):
        return self.board.is_checkmate()

    def empate(self):
        return self.board.is_stalemate() or self.board.is_insufficient_material() or self.board.is_fivefold_repetition() or self.board.is_seventyfive_moves()

    def avaliar(self, player):
        return ev.evaluate(self.board, not player)


def lerJogada(legalMovesList):
    print(legalMovesList)
    mov = input("Digite uma jogada: ")
    return mov

if __name__ == "__main__":
    player = int(input("0 pra preto, 1 pra branco: "))
    jogo = Game(chess.Board(),player)

    while not jogo.board.is_game_over():

        print(jogo.board.unicode())

        humano = lerJogada(list(jogo.board.legal_moves))
        jogo = jogo.jogar(humano)
        print("a")
        if jogo.venceu():
            print("Humano Venceu!")
            break
        elif jogo.empate():
            print("Empate!")
            break
        computador = melhor_jogada_agente_poda(jogo,3)
        print(f"Jogada do Computador é {computador}")
        jogo = jogo.jogar(computador.uci())
        
        if jogo.venceu():
            print("Computador venceu!")
            break
        elif jogo.empate():
            print("Empate!")
            break

# board = chess.Board(fen="4k3/p5pp/2p5/8/8/r7/5r2/3K4 b - - 11 35")
# ev.evaluate(board)



#an adjacency list
# positions = {}

# # depth-first search from a FEN string
# def generate_tree(fen, depth):
#     board = chess.Board(fen)
#     legal_moves = list(board.legal_moves)
#     if fen in positions:
#         positions[fen] += legal_moves
#     else:
#         positions[fen] = legal_moves

#     for move in legal_moves:
#         board.push(move)
#         next_fen = board.fen()
#         board.pop()
        
#         if not (depth == 0):
#             generate_tree(next_fen, depth-1)
#         else:
#             return

# try:
#     generate_tree(chess.STARTING_FEN, 3)
    
#     soma = 0

#     for p in positions:
#         soma += len(positions[p])
        
#     print(soma)
# except RecursionError: 
#     print("a")
#     print(len(positions) + sum(len(p) for p in positions))


# board = chess.Board()
# legalMovesList = board.legal_moves
# moves = []
# print(board.result())
# while not board.is_game_over():
#     moves.clear()
#     moves = list(board.legal_moves)

#     board.push(random.choice(moves))

# print(board)
# print(board.result())
# print(board.is_fivefold_repetition())
