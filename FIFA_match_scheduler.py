import math
from random import shuffle

def roundRobin(units, sets=None):
    """ Generates a schedule of "fair" pairings from a list of units """
    if len(units) % 2:
        units.append(None)
    count    = len(units)
    sets     = sets or (count - 1)
    half     = int(count / 2)
    schedule = []
    for turn in range(sets):
        pairings = []
        for i in range(half):
            pairings.append((units[i], units[count-i-1]))
        units.insert(1, units.pop())
        schedule.append(pairings)
    return schedule

""" test code """
if __name__ == '__main__':

    players = ["P01","P02","P03","P04","P05","P06","P07","P08","P09","P10","P11","P12","P13","---"]
    shuffle(players)

    prt = ''


    i = 1
    for pairings in roundRobin(players):
        
        print ("Fixture no.: %d" %i)
        for z in pairings:
            prt = prt + z[0] + ' vs. ' + z[1] + '\n'

        print (prt)
        prt = ''

        i = i + 1


    
