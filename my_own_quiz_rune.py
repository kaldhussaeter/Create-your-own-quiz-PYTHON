# Sources, help, tips: stackoverflow.com, www.wikipedia.org, google.com

# The question lists and answer lists
import string


easy_test = ["__1__ is used to define a function or method. ",
             "__2__ is used to write a comment. ",
             "The Python files are saved as .__3__. ",
             "Python is a programming __4__"],

medium_test = ["'For' and 'while' are forms of __1__. ",
              "__2__ adds an element to an existing list. ",
              "Using the __3__ helps you locate strings in other strings. ",
              "__4__ means 'equal to' in Python language"]

hard_test = ["Python was created in __1__ ",
            "Python was created by __2__ "
            "The terms of functions and __3__ can be used interchangeably ",
            "Lists and dictionaries are examples of ___4___ objects"]


easy_key = ['def', '#', 'py', 'language']

medium_key = ['loops', 'Append', 'find', '==']

hard_key = ['1991', 'Guido van Rossum', 'procedures', 'immutable']

blank_space = ['__1__', '__2__', '__3__', '__4__']

# Saying hello to the player and asks for the name
# take the name as input and add it to the next question (to make it more personal)
# This gives me the inputs to use for my other functions.

player_name = input("Hello and welcome to my quiz! Please enter your name: ")
player_level = input(player_name + ".. You can choose between easy, medium or hard. Which level do you want to play?: ")

# takes players input and returns the right test.

def difficulty(player_level):
    if player_level == 'easy':
        return easy_test
    if player_level == 'medium':
        return medium_test
    if player_level == 'hard':
        return hard_test
    else:
        print ("That wasn't an option! Try again")
        


# takes the players input and returns the right list of answers.

def answers(player_level):
    if difficulty(player_level) == easy_test:
        return easy_key
    elif difficulty(player_level) == medium_test:
        return medium_key
    elif difficulty(player_level) == hard_test:
        return hard_key





# If player have entered valid difficulty, it starts the quiz.
# answer_list gets the right answer list from the function.
# loops through the players input and checks if it's correct.
# if it's incorrect it's gonna stay at the same question, if it's correct
# it will return "correct" it adds 1 to the index's (question, blanks and answer list)
# When the quiz is done (index is the same as total sentence) it will break from
# the loop and congratulate the player with the name he/she put in at the beginning.
    
    
def start_quiz():
    quiz = difficulty(player_level)
    if quiz != None:
      answer_list = answers(player_level)
      index = 0
      quiz = '\n'.join(''.join(elems) for elems in quiz)
      print(quiz)
      total_sentence = len(answer_list)
      while index < total_sentence:
          player_answer = input("Type in your answer for " + blank_space[index] + " here: ")
          while player_answer not in answer_list[index]:
              index = 0
              print ("Wrong answer, try again!")
              start_quiz() 
          if player_answer == answer_list[index]:
              print ("Correct! Keep going..")
              quiz = quiz.replace(blank_space[index], player_answer)
              index += 1
              print (quiz)
    print ("Congratulations, " + player_name + "!!! You've made it!")





start_quiz()
