"""
The sum of all natural ndividers of a number 220 is equal to 284
The sum of all natural ndividers of a number 284 is equal to 220
These number are called friends.
Write a program to calculate all number friends from 2 to N
"""

def friends(n):
    """
    Function for finding friend numbers from 2 - n
    :param n: maximum number 
    :return: a list of pairs containing friend numbers
    """
    #
    dictOfNumbersAndSums = getDictOfNumbersAndTheirDividerSums(n)
    friends = []
    for number, sum in dictOfNumbersAndSums.items():
        for friendNumber, friendSum in dictOfNumbersAndSums.items():
            if number == friendSum and sum == friendNumber and number != friendNumber:
                friends.append([number, friendNumber])
    return friends


def getDictOfNumbersAndTheirDividerSums(n):
    """
    Functions that returns the full dictionary for all numbeer between 2 and n and their divider sums
    :param n: number
    :return: dictionary or numbers and their divider sums
    """
    if n < 2: return {}
    dictOfNumbersAndSums = {}
    for i in range (2, n):
        dictOfNumbersAndSums.update(getNumberAndDividerSumDict(i))
    return dictOfNumbersAndSums


def getNumberAndDividerSumDict(n):
    """
    Function that creates a dictionary where number is the key and the sum of its dividers is the value
    :param n: number
    :return: dictionary {number : sum of its divisors}
    """
    return {n : sum(getDividers(n))}


def getDividers(n):
    """
    Function for getting a list of dividers
    :param n: number for which the dividers are to be found
    :return: list of dividers on n
    """
    dividers = []
    for i in range(1, int(n / 2 + 1)):
        if n % i == 0:
            dividers.append(i)
    return dividers


if __name__ == '__main__':
    print(friends(2))