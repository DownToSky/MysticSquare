#!/usr/bin/python
import sys

HELP_MESSAGE = "This program requires two inputs.\n"\
                "Do:\n"\
                "$ pyhton driver.py <method> <board>\n"\
                "\t <method> should be one of:\n"\
                "\t bfs\n"\
                "\t dfs\n"\
                "\t ast\n"\
                "\t ida\n"\
                "\n"\
                "\t <board> is comma separated numbers from 1 to 9\n"


def Initiate_Inputs(argv):
    if len(argv) != 3:
        print("argument count error:\n" + HELP_MESSAGE)
        return -1
    if argv[1] not in ['bfs','dfs','ast','ida']:
        print("valid method name error:\n" + HELP_MESSAGE)
        return -1
    board = argv[2].split(',')
    for e in board:
        if not e.isdigit():
            print(e)
            print("non digital board number error:\n" + HELP_MESSAGE)
            return -1
        e = int(e)
    if len(board) != 3*3:
        print("invalid number of board position given\n" + HELP_MESSAGE)
        return -1
    method = argv[1]
    board = [[board[i+3*j] for i in range(0,3)] for j in range(0,3)]
    return (method, board)

def Board_To_String(board):
    output_string = ""
    for row in range(0,len(board)):
        for col in range(0,len(board[row])):
            if col != len(board[row])-1:
                output_string += "\t{}\t*".format(board[row][col])
            else:
                output_string += "\t{}\n".format(board[row][col])
        if row != len(board)-1:
            output_string += 3*8*"* "+"\n"
    return output_string

if __name__ == "__main__":
    configuration = Initiate_Inputs(sys.argv)
    if configuration == -1:
        sys.exit()
    else:
        method = configuration[0]
        board = configuration[1]

    print("method is:\n"\
            "\t{method}\n\n"\
            "the board is:\n"
            "{board}\n\n".format(method = method, board = Board_To_String(board)))

