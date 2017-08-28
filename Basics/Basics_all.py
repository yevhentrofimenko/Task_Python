#    1. Define a function, that takes string as argument and prints "Heelo, %arg%!"

def print_hello(string):
    print('Heelo, %s' % (string))


# --------------------------------------------------------------------------------------------


#    2.Define a function sum() and a function multiply() that sums and multiplies
#    (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4])
#    should return 10, and multiply([1, 2, 3, 4]) should return 24.
import unittest


def sum(user_arrray):
    sum = 0
    for i in user_arrray:
        sum += i

    if len(user_arrray) == 0:
        return ''
    return sum


def multiply(user_arrray):
    mult = 1
    for i in user_arrray:
        mult *= i
    if len(user_arrray) == 0:
        return ''
    return mult


# --------------------------------------------------------------------------------------------


#    3.Define a function reverse() that computes the reversal of a string. For example,
#    reverse("I am testing") should return the string "gnitset ma I".

def reverse(user_str):
    return user_str[::-1]


# print(reverse("I am testing"))

# --------------------------------------------------------------------------------------------


#    4. Define a function is_palindrome() that recognizes palindromes (i.e. words that look
#    the same written backwards). For example, is_palindrome("radar") should return True.

def is_palindrome(user_str):
    reverse = user_str[::-1]
    if (reverse == user_str):
        return True
    else:
        return False


# print(is_palindrome("radar"))

# --------------------------------------------------------------------------------------------


#    5. Define a procedure histogram() that takes a list of integers and prints a histogram
#    to the screen. For example, histogram([4, 9, 7]) should print the following:
#    ****
#    *********
#    ******
#    (usage time.sleep(s) possible for better visualization)

def histogram(usr_array):
    for i in usr_array:
        print("*" * i)


# histogram([4, 9, 7])

# --------------------------------------------------------------------------------------------


#    6.Define a function caesar_cipher that takes string and key(number), which returns
#    encrypted string

def caesar_cipher(usr_str, key):
    result = ''
    for i in usr_str:
        if (97 <= ord(i) <= 122):
            if (ord(i) + key > 122):
                result += chr(ord(i) + key - 26)
            else:
                result += chr(ord(i) + key)
        elif (65 <= ord(i) <= 90):
            if (ord(i) + key > 90):
                result += chr(ord(i) + key - 26)
            else:
                result += chr(ord(i) + key)
    return result


# print(caesar_cipher('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 13))

# --------------------------------------------------------------------------------------------


# 7.define a function diaginal_reverse() that takes matrix and returns diagonal-reversed one:

# 1 2 3         1 4 7
# 4 5 6 returns 2 5 8
# 7 8 9         3 6 9

import numpy as np


def diagonal_reverse(input_matrix):
    res = np.eye(3)
    for i in range(0, len(input_matrix)):
        for j in range(0, len(input_matrix[i])):
            if (i == j):
                res[i][j] = input_matrix[i][j]
            else:
                res[i][j] = input_matrix[j][i]
    return res


# print(diagonal_reverse([[1,2,3],
#                         [4,5,6],
#                         [7,8,9]]
#                        ))


# --------------------------------------------------------------------------------------------


#     8. Write a function game() number-guessing game, that takes 2 int parameters defining the
#     range. Using random.randint(A, B) generate random int from the range. While user input
#     isn't equal that number, print "Try again!". If user guess the number, congratulate
#     him and exit. (use raw_input())

import random


def game():
    attempts = 2
    start = input('From which number start range?\n')
    to = input('Till which number?\n')
    answer = random.randint(int(start), int(to))
    print('Now try to guess the number that i made, you have 3 attempts')
    for i in range(3):
        user_answer = input('(input your guess)\n')
        if (int(user_answer) == answer):
            print('You win')
            break
        else:
            if (attempts == 0):
                print('You lose')
                break

            print('Try again')
            print('%d left' % (attempts))
            attempts -= 1


# game()

# --------------------------------------------------------------------------------------------


#    9.Define a function, which takes a string with N opening brackets ("[") and N closing brackets ("]"),
#    in some arbitrary order.
#    Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of
#    opening/closing brackets (in that order), none of which mis-nest.
#    Examples:

#    []        OK   ][        NOT OK
#    [][]      OK   ][][      NOT OK
#    [[][]]    OK   []][[]    NOT OK


def brackets(usr_str):
    if (len(usr_str) == 0):
        print('NOT OK')

    elif (len(usr_str) % 2 == 0):
        resut = usr_str.replace('[]', '')
        if (resut == '[]' or resut == ''):
            print('OK')
        else:
            print('NOT OK')
    else:
        print('NOT OK')


# --------------------------------------------------------------------------------------------


#    10. Write a function char_freq() that takes a string and builds a frequency listing of
#    the characters contained in it. Represent the frequency listing as a Python dictionary.
#    Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(str):
    freq_list = {}
    for i in str:
        if i in freq_list:
            freq_list[i] += 1
        else:
            freq_list[i] = 1
    return freq_list


# print(char_freq("abbabcbdbabdbdbabababcbcbab"))


# --------------------------------------------------------------------------------------------


#    11. Write a function dec_to_bin() that takes decimal integer and outputs its binary
#    representation.

def dec_to_bin(integer):
    return bin(integer)


# print(dec_to_bin(12))


# --------------------------------------------------------------------------------------------


#    12. Write a ship battle game, which is similar to ex.8, except it takes 1 integer as 
#    an order of matrix, randomly generates index (x, y) and checks user input (2 integers).
#    (tip: use var1, var2 = raw_input("Enter two numbers here: ").split())
#    *Visualize the game.

from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


def start_game():
    print_board(board)
    ship_row = random_row(board)
    ship_col = random_col(board)
    # ======================================
    # DElETE THE COMMENT FOR SHOWING ANSWER

    # print('Answer row: %d'%(ship_row))
    # print('Answer col: %d'%(ship_col))
    # ======================================
    for turn in range(4):
        print("Turn", turn + 1)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sank my battleship!")
            break
        else:
            if guess_row not in range(5) or \
                            guess_col not in range(5):
                print("That's not even in the ocean.")
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            print_board(board)
            if turn == 3:
                print('Game Over')


# start_game()

class TestSum(unittest.TestCase):
    def test_empty(self):
        res = sum([])
        self.assertEqual(res, '')

    def test_one(self):
        res = sum([1])
        self.assertEqual(res, 1)

    def test_normal(self):
        res = sum([1, 2, 3, 4, 5])
        self.assertEqual(res, 15)

    def test_negative(self):
        res = sum([-1, -2, -3, -4, -5])
        self.assertEqual(res, -15)

    def test_mixed(self):
        res = sum([-1, 2, -3, 4, -5])
        self.assertEqual(res, -3)

    def test_big(self):
        res = sum([10000, 2222, 234542, 542532, 5349285])
        self.assertEqual(res, 6138581)


class TestMult(unittest.TestCase):
    def test_empty(self):
        res = multiply([])
        self.assertEqual(res, '')

    def test_one(self):
        res = multiply([1])
        self.assertEqual(res, 1)

    def test_normal(self):
        res = multiply([1, 2, 3, 4, 5])
        self.assertEqual(res, 120)

    def test_negative(self):
        res = multiply([-1, -2, -3, -4, -5])
        self.assertEqual(res, -120)

    def test_mixed(self):
        res = multiply([-1, 2, -3, 4, -5])
        self.assertEqual(res, -120)

    def test_big(self):
        res = multiply([10000, 2222, 234542, 542532, 535])
        self.assertEqual(res, 1512668697647368800000)

class TestReverse(unittest.TestCase):
    def test_reverse(self):
        res = reverse('I do it')
        self.assertEqual(res,'ti od I')

class TestAlwaysTrue(unittest.TestCase):

    def test_simple(self):
        result = is_palindrome('sas')
        self.assertTrue(result)

    def test_rus(self):
        result = is_palindrome('шабаш')
        self.assertTrue(result)

class TestBrakets(unittest.TestCase):

    def test_first(self):
        res = brackets('[]')
        self.assertEqual(res, 'OK')

if __name__ == '__main__':
    unittest.main()
