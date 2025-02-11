import chess
import chess.pgn
import numpy as np

pgn = open("lichess_partial.pgn")
move_array = []
data_list = np.empty(shape = [0, 4])
i = 0
for i in range (10000):
    game = chess.pgn.read_game(pgn)
    if game is None:
        break
    print(i)
    opening = game.headers["Opening"]
    result = game.headers["Result"]
    whiteElo = game.headers["WhiteElo"]
    blackElo = game.headers["BlackElo"]
    for move in game.mainline_moves():
        move_array.append(str(move))
    row = np.array([opening, result, whiteElo, blackElo])
    data_list = np.append(data_list, [row], axis = 0)
print(data_list)