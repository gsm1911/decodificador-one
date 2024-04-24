# -*- coding: utf-8 -*-
"""
Created on Mon May  1 12:57:39 2023

@author: Desktop
"""
guessed = False;
guess = ''
secret_word = "adab"
letters_guessed = ["a", "c", "d"]


for i in letters_guessed:
    for n in secret_word:
        if i in secret_word:
            if i == n:
                guess += i
            else:
                continue
    print(guess)