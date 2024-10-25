import random
import os


class Players():
    def __init__(self,number,name,color):
        self.number = number
        self.name = name
        self.color = color


    def create_players():    # ADD TRY EXCEPT IF SOMEONE INPUT STR nao ta funfando inda
        too_much_players = True
        while too_much_players:
            try:
                qtd_players = int(input("Number of players: "))
                if qtd_players <= 7 and qtd_players >= 2:
                    too_much_players = False
                else:
                    print("The maximum number of players is 7 and the minimun is 2")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        players_list = {}
        number = 0
        colors = ["yellow","blue","green","red","pink","orange","purple"]

        while qtd_players > 0:
            name = input("Type the player name: ")
            number += 1
            color = random.choice(colors)
            colors.remove(color)
            new_player = Players(number,name,color)
            players_list.update({new_player.number:[new_player.name, new_player.color]})
            qtd_players -= 1
        return players_list
    

    def turn(player_number): 
        turns = 4
        story = ""
        while turns > 0:                                                          #color = player_number[player][1]
            for player in player_number: 
                if turns == 4:
                    story += "Once upon a time, "
                    story += input(f"{player_number[player][0]}, start the story: Once upon a time, ") # ADICIONAR INICIO ALEATORIO de uma lista ANTES DO INPUT / verificar input por palavroes e substituir por ****
                    story += " "
                    turns -= 1
                    os.system('cls')
                elif turns == 1:
                    words = story.split()
                    story += input(f"{player_number[player][0]}, write a piece of the story: {" ".join(words[-3:])}") #ADICIONAR FINAL ALEATORIO NO FIM DO INPUT
                    story += ". But it all was just a dream. THE END!"
                    turns -= 1
                    os.system('cls')
                    return story
                else:
                    words = story.split()
                    story += input(f"{player_number[player][0]}, write a piece of the story: {" ".join(words[-3:])} ") #ADICIONAR ALEATORIAMENTE UM DESSES: FOI ENTAO QUE, DE REPENTE, FOI AI QUE, RESOLVEU FAZER, E NUM PISCAR DE OLHOS...
                    story += " "
                    turns -= 1
                    os.system('cls')


