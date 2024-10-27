'''
perguntar se o usuario quer salvar a historia em um documento.
texto de cada vai ter a cor do jogador.
'''
from players_class import Players



n_of_players = Players.create_players()


for player in n_of_players:
     print(f"Player {player} is {n_of_players[player][0]} and has the {n_of_players[player][1]} color.")



story = Players.turn(n_of_players)


print(story)

