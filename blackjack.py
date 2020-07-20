import random 


def deal():
    card = random.randint (1, 13)
    if (card == 11 or card == 12 or card == 13):
        card = 10
    return card

def bust():
    if sum(hand)<21:
        hit()

def hit():
    print ("Hit me?")
    ans = input()
    if ans == ("yes"):
        newcard = deal()
        print ("Your next card is " + str(newcard))
        hand.append(newcard)
        print ("This means your new total is " + str(sum(hand)))
        bust()
    elif ans == ("no"):
        print ("You stayed and your final value was " + str(sum(hand)))
    else:
        print ("error")

def card():
    nc = deal()
    print ("The dealer drew a " + str(nc))
    return nc

def dealer(xc):
    global dh
    dh = [xc, deal()]
    while (sum(dh) <= 15):
            dh.append(deal())
def wol():
    if sum(hand) > 21:
        print ("You busted and lost")
    else:
        print ("The dealer's hand is " + str(dh))  
    if sum(dh)> 21:
        print("The dealer busted and you won")
    elif sum(hand) > sum(dh):
        print ("Your total was " + str(sum(hand)) + " while the dealers total was " + str(sum(dh)) + ". You won.")
    elif sum(hand) == sum(dh):
        print ("Your total was " + str(sum(hand)) + " while the dealers total was " + str(sum(dh)) + " and the both of you tied")
    elif sum(hand) < sum(dh):
        print ("Your total was " + str(sum(hand)) + " while the dealers total was " + str(sum(dh)) + ". You lost.")

hand = [deal(), deal()]
print ("Your hand is " + str(hand))
print ("Your total is " + str(sum(hand)))
xc = card()
hit()
dealer(xc)
wol()