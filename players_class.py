import random
import os
from lists import story_beginnings, story_ends
import tkinter as tk
import ttkbootstrap as ttk

class Players():
    def __init__(self,number,name,color):
        self.number = number
        self.name = name
        self.color = color


    def create_players(): 
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
        count = 0
        colors = ["yellow","blue","green","red","pink","orange","purple"]

        while qtd_players > 0:
            name = input("Type the player name: ")
            count += 1
            color = random.choice(colors)
            colors.remove(color)
            new_player = Players(count,name,color)
            players_list.update({new_player.number:[new_player.name, new_player.color]})
            qtd_players -= 1
        return players_list
    

    def turn(player_number): 
        turns = 6
        story = ""
        while turns > 0:                  #color = player_number[player][1]
            for player in player_number: 
                if turns == 6:
                    beginning = str(random.choice(story_beginnings))
                    story += beginning 
                    story += " "
                    story += input(f"{player_number[player][0]}, start the story: {beginning}, ") #verificar input por palavroes e substituir por ****
                    story += " "
                    turns -= 1
                    os.system('cls')
                elif turns == 1:
                    ending = str(random.choice(story_ends))
                    words = story.split()
                    story += input(f"{player_number[player][0]}, write a piece of the story: {" ".join(words[-3:])} ")
                    story += f". {ending}. THE END!"
                    turns -= 1
                    os.system('cls')
                    return story
                else:
                    words = story.split()
                    story += input(f"{player_number[player][0]}, write a piece of the story: {" ".join(words[-3:])} ") 
                    story += " "
                    turns -= 1
                    os.system('cls')

