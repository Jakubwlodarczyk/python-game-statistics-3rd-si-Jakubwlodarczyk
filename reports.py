#!/usr/bin/python3
import os


def count_games(data_file_name):
    # count lines of a file (cause each line is a game)
    with open(data_file_name) as f:
        games = (len(f.readlines()))
    return games


def decide(data_file_name, year=''):
    # checking if given 'year' is located in file
    year = str(year)
    if len(year) == 4:
        found = False
        with open(data_file_name) as f:
            read_file = f.read()
            if year in read_file:
                found = True
            else:
                found = False
            return found
    

def get_latest(data_file_name):
    # make a new list of file data
    list_of_line = []
    with open(data_file_name, 'r') as open_file:
        list_of_line = [line.strip().split('\t') for line in open_file]
        # sort a list on key=2 (2- is a position of year-value in list)
        list_of_line.sort(key=lambda x: x[2], reverse=True)
    # return the first value of first line of list (which is a name of game)
    return list_of_line[0][0]


def count_by_genre(data_file_name, genre=''):
    # count how many times "genre" is located in text file, and return the value
    total = 0
    with open(data_file_name) as f:
        for line in f:
            finded = line.find(genre)
            if finded != -1 and finded != 0:
                total += 1
    return total


def get_line_number_by_title(data_file_name, title=''):
    # check if title is located in text file, and return the number of line where it is located
    with open(data_file_name) as f:
        for num, line in enumerate(f, 1):
            if title in line:
                return num
