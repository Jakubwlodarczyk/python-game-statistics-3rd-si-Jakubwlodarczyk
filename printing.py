#!/usr/bin/python3
import os
from reports import *


def count_games_print(data_file_name):
    print("Games count is: {}.".format(count_games(data_file_name)))


def decide_print(data_file_name, year=''):
    print("Is there a game from a {} year? {}.".format(year, decide(data_file_name, year='2000')))


def count_by_genre_print(data_file_name, genre=''):
    print("We have {} {} games.".format(count_by_genre(data_file_name, 'RPG'),genre))


def get_line_number_by_title_print(data_file_name, title=''):
    print("{} is a line number of {}.".format(get_line_number_by_title(data_file_name, 'World of Warcraft'), title))

def get_latest_print(data_file_name):
    print("The latest game is: {}.".format(get_latest(data_file_name)))


def main():
    # Check out for file which ends on ".txt"
    # Assign founded file to - data_file_name 
    # Write your own path to the file - to let the program work properly
    for file in os.listdir("/home/jakub/codecool/python-game-statistics-3rd-si-Jakubwlodarczyk"):
        if file.endswith(".txt"):
            data_file_name = file
    count_games_print(data_file_name)
    decide_print(data_file_name, '2000') # '2000' - is my random value of year
    count_by_genre_print(data_file_name, 'RPG') # 'RPG ' - random name of genre
    get_line_number_by_title_print(data_file_name, 'World of Warcraft') # "World of Warcraft" - random game name
    get_latest_print(data_file_name)



if __name__ == "__main__":
    main()
