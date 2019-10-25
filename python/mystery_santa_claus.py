# -*- coding: utf-8 -*-

# That little script let you select who you are,
# Display for who you have to give gifts
# After x seconds, clear screen and it's for next person.

# Requirements : PyInquirer

from __future__ import print_function, unicode_literals
import os
import regex
import time

import random
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


def tirage(result):
    u"""TAS"""

    offer = result[-1]
    while offer == answers.get('who'):
        random.shuffle(result, random.random)
        offer = result[-1]

    return offer


questions = [
    {
        'type': 'list',
        'name': 'who',
        'message': 'Who are you ?',
        'choices': ['A', 'B', 'C', 'D'],
    },
]

result = ["A", "B", "C", "D"]

for i in range(0, len(questions[0]['choices'])):
    answers = prompt(questions, style=style)

    # Print line separator.
    print("-" * 12)

    random.shuffle(result, random.random)

    offer = tirage(result)
    result.remove(offer)

    print("You are the santa claus of : " + offer)

    # Wait X seconds
    time.sleep(1)

    # Clear the script to not cheat
    os.system('clear')

    # Remove player from prompt
    questions[0]['choices'].remove(answers.get('who'))

