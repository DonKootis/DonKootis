import random
import time
import itertools


balance = 100
print('Your balance is', balance)


items = ['Cherry', 'Seven', 'Bar', 'Lemon', 'Watermelon', 'Bell']

#possibleReels = list(itertools.product(items, items, items))

a = random.choice(items)
b = random.choice(items)
c = random.choice(items)

userReel = (a, b, c)

winningReels = {
    "Cherry": 10,
    "Seven": 20,
    "Bar": 30,
    "Lemon": 40,
    "Watermelon": 50,
    "Bell": 60
}

def spin():
    global balance
    #userReel = random.choice(possibleReels)

    #if userReel == winningReels:
    if (a == b and b == c):
        payout = winningReels[a]
        print(f'You won! Your spin was {userReel} and your payout is {payout}')
        balance += payout
    else:
        print("You lost :( Your spin was", userReel)



while balance > 0:
    try:
        bet = int(input("Enter your bet(or 0 to quit): "))

        if bet == 0:
            print('Thanks for playing')
            break

        if (bet > balance and bet != 12345):
            print('Bet cannot be greater then balance')
            continue

        if bet == 12345:
            balance = 100000000000000000000000
            print('Infinite Balance!')
            continue


        balance -= bet
        spin()
        print('Your balance is now', balance)

    except ValueError:
        print("Invalid bet, Please input a whole number:")
