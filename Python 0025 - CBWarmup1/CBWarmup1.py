# CBWarmup1.py
# http://codingbat.com/python/Warmup-1
# created 10.05.2017 by CB Fay

# http://codingbat.com/prob/p173401
def sleep_in(weekday, vacation):
    """The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
    """
    if not weekday or vacation:
        return True
    return False

# http://codingbat.com/prob/p120546
def monkey_trouble(a_smile, b_smile):
    """We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
    """
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    return False

def monkey_trouble2(a_smile, b_smile):
    return a_smile == b_smile

# http://codingbat.com/prob/p141905
def sum(a,b):
    """Given two int values, return their sum. Unless the two values are the same, then return double their sum.
    """
    if a == b:
        return a*4
    return a+b

# http://codingbat.com/prob/p197466
def diff21(n):
    """Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
    """
    if n > 21:
        return abs((21 - n) * 2)
    return abs(21 - n)

# http://codingbat.com/prob/p166884
def parrot_trouble(talking, hour):
    """We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
    """
    if(talking and (hour < 7 or hour > 20)):
        return True
    return False
