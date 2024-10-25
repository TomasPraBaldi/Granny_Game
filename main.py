'''
1perguntar quantos jogadores serao. OK
2gerar um inicio de historia random como ex: Era uma vez, Na cidade so se falava em uma coisa:, Ha muito tempo, Foi vendo o mar que...
3primeiro input de X caracteres do usuario 1 vai ter o inicio da historia para ele continuar um pouco(+- 10 palavras),
4pegar as tres ultimas palavras e guardar em uma variavel.
5jogar as tres ultimas palavras para o usuario 2 continuar, assim por diante.
6no final gerar um final aleatorio ex: FIM, e todos viveram felizes para sempre, E deu., Depois todos morreram.
7perguntar se o usuario quer salvar a historia em um documento.
8cada jogador tera uma cor. OK
9texto de cada vai ter a cor do jogador.
'''
from players_class import Players



n_of_players = Players.create_players()


for player in n_of_players:
     print(f"Player {player} is {n_of_players[player][0]} and has the {n_of_players[player][1]} color.")



story = Players.turn(n_of_players)


print(story)

