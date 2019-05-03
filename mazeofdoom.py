from random import random, randint
from time import sleep, time
from keyboard import is_pressed
from os import system



#     ▄▄▄▄███▄▄▄▄      ▄████████  ▄███████▄     ▄████████      ▄██████▄     ▄████████     ████████▄   ▄██████▄   ▄██████▄    ▄▄▄▄███▄▄▄▄   
#   ▄██▀▀▀███▀▀▀██▄   ███    ███ ██▀     ▄██   ███    ███     ███    ███   ███    ███     ███   ▀███ ███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄ 
#   ███   ███   ███   ███    ███       ▄███▀   ███    █▀      ███    ███   ███    █▀      ███    ███ ███    ███ ███    ███ ███   ███   ███ 
#   ███   ███   ███   ███    ███  ▀█▀▄███▀▄▄  ▄███▄▄▄         ███    ███  ▄███▄▄▄         ███    ███ ███    ███ ███    ███ ███   ███   ███ 
#   ███   ███   ███ ▀███████████   ▄███▀   ▀ ▀▀███▀▀▀         ███    ███ ▀▀███▀▀▀         ███    ███ ███    ███ ███    ███ ███   ███   ███ 
#   ███   ███   ███   ███    ███ ▄███▀         ███    █▄      ███    ███   ███            ███    ███ ███    ███ ███    ███ ███   ███   ███ 
#   ███   ███   ███   ███    ███ ███▄     ▄█   ███    ███     ███    ███   ███            ███   ▄███ ███    ███ ███    ███ ███   ███   ███ 
#    ▀█   ███   █▀    ███    █▀   ▀████████▀   ██████████      ▀██████▀    ███            ████████▀   ▀██████▀   ▀██████▀   ▀█   ███   █▀  
#                                                                                                                                          
                                                                                        

logothing = "   __    __  ______  ______  ______       ______  ______     _____   ______  ______  __    __    \n  /\ \-./  \/\  __ \/\___  \/\  ___\     /\  __ \/\  ___\   /\  __-./\  __ \/\  __ \/\ \-./  \   \n  \ \ \-./\ \ \  __ \/_/  /_\ \  __\     \ \ \/\ \ \  __\   \ \ \/\ \ \ \/\ \ \ \/\ \ \ \-./\ \  \n   \ \_\ \ \_\ \_\ \_\/\_____\ \_____\    \ \_____\ \_\      \ \____-\ \_____\ \_____\ \_\ \ \_\ \n    \/_/  \/_/\/_/\/_/\/_____/\/_____/     \/_____/\/_/       \/____/ \/_____/\/_____/\/_/  \/_/"

player_pos = 89

LENGTH = 0.1

LEVELS = ["##########\n#...&....#\n####.....#\n#..#...###\n#..##.####\n#..O#....#\n#.###.####\n#.#...#$$#\n#.....#$$#\n##########", "##########\n##.O##..$#\n##.##..###\n##.##.####\n##.##....#\n#...#....#\n#.#.#.#.##\n#.#.#.#..#\n#.#...#.&#\n##########", "##########\n##......##\n###....###\n######.###\n#..O..#..#\n###%###..#\n#..&...#.#\n###%.###.#\n#....#####\n##########", "##########\n#%%.....O#\n#%%.%%%%%#\n#%%%.%%%%#\n#%%&%%%%%#\n#%%.%%%%%#\n#%.%%%%%%#\n#.%%%%%%%#\n#.%%%%%%%#\n##########", "##########\n#%%%%%%%O#\n#$%.%...%#\n#%...%.%##\n#%.#######\n###...####\n####.#####\n##.#....&#\n#.#.######\n##########", "##########\n#%.....%$#\n#.%.#%.%.#\n#..%#..%.#\n#&..#.%..#\n#####%.%%#\n#..%#.#..#\n#.%.#.#..#\n#.O...#$.#\n##########", "##########\n#.......&#\n#.######.#\n#.######.#\n#.###.##.#\n#.####.#.#\n#.###.##.#\n#.#..###.#\n#O.......#\n##########", "##########\n#.......O#\n########.#\n#......#.#\n#.####.#.#\n#.#&.#.#.#\n#.#....#.#\n#.######.#\n#........#\n##########", "##########\n#%.%#%.%.#\n#.#.#.#..#\n#.#.#.#..#\n#.#.#.#..#\n#.#.#.#..#\n#.#.#.#..#\n#.#.#.#&.#\n#.#%.%#O.#\n##########", "##########\n#........#\n#.#...#..#\n#.##.##..#\n#.#.#.#..#\n#.#...#..#\n#.#...#..#\n#.#...#..#\n#.#$&$#.O#\n##########"]
ST_P = [89, 89, 89, 89, 89, 89, 49, 13, 89, 89]

def add_player(lst):
    level = list(lst)
    level[player_pos] = "@"
    lst = "".join(level)
    return lst

def add_dot(lst, pos):
    level = list(lst)
    level[pos] = "."
    lst = "".join(level)
    return lst

########
# GAME #
########
coins = 0

system("cls")

try: input(logothing)
except: pass

system("cls")

starttime = time()

for i in range(len(LEVELS)):
    key = False
    leveladv = False
    player_pos = ST_P[i]
    system("cls")
    LEVELS[i] = add_player(LEVELS[i])
    print("Floor #" + str(i + 1) + " | $" + str(coins))
    print(LEVELS[i])
    keypress = False
    while not keypress and not leveladv:
        if is_pressed('up') and ((LEVELS[i][player_pos - 11] == "." or LEVELS[i][player_pos - 11] == "&" or LEVELS[i][player_pos - 11] == "$" or LEVELS[i][player_pos - 11] == "%") or (LEVELS[i][player_pos - 11] == "O" and key)):
            system("cls")
            keypress = True
            LEVELS[i] = add_dot(LEVELS[i], player_pos)
            player_pos -= 11
            if LEVELS[i][player_pos] == "&": key = True
            if LEVELS[i][player_pos] == "$": coins += 3
            if LEVELS[i][player_pos] == "%": coins -= 5
            if LEVELS[i][player_pos] == "O": leveladv = True
            LEVELS[i] = add_player(LEVELS[i])
            print("Floor #" + str(i + 1) + " | $" + str(coins))
            print(LEVELS[i])
            sleep(LENGTH)
            keypress = False
        if is_pressed('right') and ((LEVELS[i][player_pos + 1] == "." or LEVELS[i][player_pos + 1] == "&" or LEVELS[i][player_pos + 1] == "$" or LEVELS[i][player_pos  + 1] == "%") or (LEVELS[i][player_pos + 1] == "O" and key)):
            system("cls")
            keypress = True
            LEVELS[i] = add_dot(LEVELS[i], player_pos)
            player_pos += 1
            if LEVELS[i][player_pos] == "&": key = True
            if LEVELS[i][player_pos] == "$": coins += 3
            if LEVELS[i][player_pos] == "%": coins -= 5
            if LEVELS[i][player_pos] == "O": leveladv = True
            LEVELS[i] = add_player(LEVELS[i])
            print("Floor #" + str(i + 1) + " | $" + str(coins))
            print(LEVELS[i])
            sleep(LENGTH)
            keypress = False
        if is_pressed('left') and ((LEVELS[i][player_pos - 1] == "." or LEVELS[i][player_pos - 1] == "&" or LEVELS[i][player_pos - 1] == "$" or LEVELS[i][player_pos - 1] == "%") or (LEVELS[i][player_pos - 1] == "O" and key)):
            system("cls")
            keypress = True
            LEVELS[i] = add_dot(LEVELS[i], player_pos)
            player_pos -= 1
            if LEVELS[i][player_pos] == "&": key = True
            if LEVELS[i][player_pos] == "$": coins += 3
            if LEVELS[i][player_pos] == "%": coins -= 5
            if LEVELS[i][player_pos] == "O": leveladv = True
            LEVELS[i] = add_player(LEVELS[i])
            print("Floor #" + str(i + 1) + " | $" + str(coins))
            print(LEVELS[i])
            sleep(LENGTH)
            keypress = False
        if is_pressed('down') and ((LEVELS[i][player_pos + 11] == "." or LEVELS[i][player_pos + 11] == "&") or LEVELS[i][player_pos + 11] == "$"  or LEVELS[i][player_pos + 11] == "%" or (LEVELS[i][player_pos + 11] == "O" and key)):
            system("cls")
            keypress = True
            LEVELS[i] = add_dot(LEVELS[i], player_pos)
            player_pos += 11
            if LEVELS[i][player_pos] == "&": key = True
            if LEVELS[i][player_pos] == "$": coins += 3
            if LEVELS[i][player_pos] == "%": coins -= 5
            if LEVELS[i][player_pos] == "O": leveladv = True
            LEVELS[i] = add_player(LEVELS[i])
            print("Floor #" + str(i + 1) + " | $" + str(coins))
            print(LEVELS[i])
            sleep(LENGTH)
            keypress = False
        if is_pressed('s') and ((LEVELS[i][player_pos + 12] == "." or LEVELS[i][player_pos + 12] == "&") or LEVELS[i][player_pos + 12] == "$"  or LEVELS[i][player_pos + 12] == "%" or (LEVELS[i][player_pos + 12] == "O" and key)):
            system("cls")
            keypress = True
            LEVELS[i] = add_dot(LEVELS[i], player_pos)
            player_pos += 12
            if LEVELS[i][player_pos] == "&": key = True
            if LEVELS[i][player_pos] == "$": coins += 3
            if LEVELS[i][player_pos] == "%": coins -= 5
            if LEVELS[i][player_pos] == "O": leveladv = True
            LEVELS[i] = add_player(LEVELS[i])
            print("Floor #" + str(i + 1) + " | $" + str(coins))
            print(LEVELS[i])
            sleep(LENGTH)
            keypress = False
        if is_pressed('q') and ((LEVELS[i][player_pos - 12] == "." or LEVELS[i][player_pos - 12] == "&") or LEVELS[i][player_pos - 12] == "$"  or LEVELS[i][player_pos - 12] == "%" or (LEVELS[i][player_pos - 12] == "O" and key)):
            system("cls")
            keypress = True
            LEVELS[i] = add_dot(LEVELS[i], player_pos)
            player_pos -= 12
            if LEVELS[i][player_pos] == "&": key = True
            if LEVELS[i][player_pos] == "$": coins += 3
            if LEVELS[i][player_pos] == "%": coins -= 5
            if LEVELS[i][player_pos] == "O": leveladv = True
            LEVELS[i] = add_player(LEVELS[i])
            print("Floor #" + str(i + 1) + " | $" + str(coins))
            print(LEVELS[i])
            sleep(LENGTH)
            keypress = False
        if is_pressed('a') and ((LEVELS[i][player_pos + 10] == "." or LEVELS[i][player_pos + 10] == "&") or LEVELS[i][player_pos + 10] == "$" or LEVELS[i][player_pos + 10] == "%" or (LEVELS[i][player_pos + 10] == "O" and key)):
            system("cls")
            keypress = True
            LEVELS[i] = add_dot(LEVELS[i], player_pos)
            player_pos += 10
            if LEVELS[i][player_pos] == "&": key = True
            if LEVELS[i][player_pos] == "$": coins += 3
            if LEVELS[i][player_pos] == "%": coins -= 5
            if LEVELS[i][player_pos] == "O": leveladv = True
            LEVELS[i] = add_player(LEVELS[i])
            print("Floor #" + str(i + 1) + " | $" + str(coins))
            print(LEVELS[i])
            sleep(LENGTH)
            keypress = False
        if is_pressed('w') and ((LEVELS[i][player_pos - 10] == "." or LEVELS[i][player_pos - 10] == "&") or LEVELS[i][player_pos - 10] == "$" or LEVELS[i][player_pos - 10] == "%"  or (LEVELS[i][player_pos - 10] == "O" and key)):
            system("cls")
            keypress = True
            LEVELS[i] = add_dot(LEVELS[i], player_pos)
            player_pos -= 10
            if LEVELS[i][player_pos] == "&": key = True
            if LEVELS[i][player_pos] == "$": coins += 3
            if LEVELS[i][player_pos] == "%": coins -= 5
            if LEVELS[i][player_pos] == "O": leveladv = True
            LEVELS[i] = add_player(LEVELS[i])
            print("Floor #" + str(i + 1) + " | $" + str(coins))
            print(LEVELS[i])
            sleep(LENGTH)
            keypress = False
endtime = time()

scoretxt = "\n\n   SSSSSSSSSSSSSSS                                                                              \n SS:::::::::::::::S                                                                             \nS:::::SSSSSS::::::S                                                                             \nS:::::S     SSSSSSS                                                                             \nS:::::S                cccccccccccccccc   ooooooooooo   rrrrr   rrrrrrrrr       eeeeeeeeeeee    \nS:::::S              cc:::::::::::::::c oo:::::::::::oo r::::rrr:::::::::r    ee::::::::::::ee  \n S::::SSSS          c:::::::::::::::::co:::::::::::::::or:::::::::::::::::r  e::::::eeeee:::::ee\n  SS::::::SSSSS    c:::::::cccccc:::::co:::::ooooo:::::orr::::::rrrrr::::::re::::::e     e:::::e\n    SSS::::::::SS  c::::::c     ccccccco::::o     o::::o r:::::r     r:::::re:::::::eeeee::::::e\n       SSSSSS::::S c:::::c             o::::o     o::::o r:::::r     rrrrrrre:::::::::::::::::e \n            S:::::Sc:::::c             o::::o     o::::o r:::::r            e::::::eeeeeeeeeee  \n            S:::::Sc::::::c     ccccccco::::o     o::::o r:::::r            e:::::::e           \nSSSSSSS     S:::::Sc:::::::cccccc:::::co:::::ooooo:::::o r:::::r            e::::::::e          \nS::::::SSSSSS:::::S c:::::::::::::::::co:::::::::::::::o r:::::r             e::::::::eeeeeeee  \nS:::::::::::::::SS   cc:::::::::::::::c oo:::::::::::oo  r:::::r              ee:::::::::::::e  \n SSSSSSSSSSSSSSS       cccccccccccccccc   ooooooooooo    rrrrrrr                eeeeeeeeeeeeee  \n                                                                                                \n                                                                                                "

score = str(int(((12 * len(LEVELS)) - ((endtime - starttime) - coins)) * 100))

print(scoretxt + "\n\n" + score)
