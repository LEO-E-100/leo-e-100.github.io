---
layout: post
title: "Rock Paper Scissors"
date: 2017-06-11
---

### Rock Paper Scissors project

## [Code Repo](https://github.com/LEO-E-100/Rock-Paper-Scissors)

This project was my first time programming after finishing some basic python tutorials. I think I did an ok job and iterated until it was nearly perfect. This whole project took me a long time and taught me a huge amount about how Python works.

It is essentially composed of a series of functions which iteratively call the next function. The data structures used were the most basic. First the values of 'rock' 'paper' and 'scissors' are assigned integer values which allows for random generation, next the variables are assigned to string equivalents using a dictionary (key-value pairs). Having now studied data structures formally I can say this is a look up table and has many efficiency benefits, when I wrote this I considered this to simply be the best way to make it work (much googling was done). Finally to give the game some replay value I decided to keep score by initialising two variables to zero to keep score.

Having set up the values to work on I set about creating functionality. This involved some simple white board diagrams and a step by step definition of what a game of rock-paper-scissors involves. Defining a computer generated move was a simple case of randomly generating a number between 1 and 3.

```python
computer = random.randint(1,3)
```

A user generated move was more complex, having not learned much about making programs interactive during my early tutorials I had to learn about the `raw_input` function of python. This worked initially however it occurred to me that a person could enter a value that wasn't an integer between one and three and the program would break. This introduced me to exception handling for the first time. A try-except block was used to ensure that if the value was invalid a reminder would pop up to show the user the way. I also got stuck on casting the input value as an integer, after googling why the system might be throwing errors I found the answer, however it was only after my Intro to Programming class at UCL that I found out the underlying reason for doing this.

After functions had been defined to show the two moves made, the results had to be evaluated. This was first achieved by simply printing the result using some if-else blocks to compare the two values. However I thought this was unsatisfying as there was no *'game'* feeling to the program. I decided to add a countdown, this would reflect the atmosphere of the game, and mimic a real game of rps better than simply printing results. Using the 'time' package the countdown was achieved fairly simply.

```python
def result(player, computer):
    print "1..."
    time.sleep(1)
    print "2..."
    time.sleep(1)
    print "3!"
    time.sleep(0.5)
    print "Computer threw {0}!".format(names[computer])
    global player_score, computer_score
    if player == computer:
        print "Tie game."
    else:
        if rules[player] == computer:
            print "You Win."
            player_score += 1
        else:
            print "You Lose."
            computer_score += 1
```
This comparison also required the initialisation of the 'rules' dictionary which simply outlined which value would beat which. I have to admit that this particular method was largely gained from googling around for an elegant solution that didn't require a long series of if-else blocks with each combination in (this was my first solution).

The final function was a simple printing of the scores at the end of the game. This took me longer than I care to admit as the variables did not have block level scope. This taught me a valuable lesson about how variables work in python.
