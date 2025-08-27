import random

def take_card(hand, cards):
    random_card = random.choice(cards)
    hand.append(random_card)
    cards.remove(random_card)

def sum(hand):
    s = 0
    for item in hand:
        if item == "A":
            hand.remove(item)
            hand.append(item)
    for item in hand:
        if item == "A" and s < 10:
            s += 11
        elif item == "A" and s >= 10:
            s += 1
        elif item == "J":
            s += 12
        elif item == "Q":
            s += 13
        elif item == "K":
            s += 14
        else:
            s += int(item)
    return s

            

cards = [
    'A', 'A', 'A', 'A',
    '2', '2', '2', '2',
    '3', '3', '3', '3',
    '4', '4', '4', '4',
    '5', '5', '5', '5',
    '6', '6', '6', '6',
    '7', '7', '7', '7',
    '8', '8', '8', '8',
    '9', '9', '9', '9',
    '10', '10', '10', '10',
    'J', 'J', 'J', 'J',
    'Q', 'Q', 'Q', 'Q',
    'K', 'K', 'K', 'K'
]

print("Do you want to play? (y/n)")
answer = input()
my_cards = []
computer_cards = []
if answer == 'y':
    my_cards.append(random.choice(cards))
    my_cards.append(random.choice(cards))
  #  my_cards = ["A", "A"]
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    for card in my_cards:
        cards.remove(card)
    for card in computer_cards:
        cards.remove(card)
    print(f"Your cards: {my_cards}")
    print("Computer's card: " + computer_cards[0])
    
    ask = True
    while(True):
        if sum(my_cards) < 21 and sum(computer_cards) < 21:
            if ask:
                print("Do you want to take one more card? (y/n)")
                take = input()
                if take == 'y':
                    take_card(my_cards, cards)
                    print(f"Your cards: {my_cards}")
                elif take == 'n':
                    ask = False
            if sum(computer_cards) < 17:
                print("Computer took one more card")
                take_card(computer_cards, cards)
            else:
                print("Computer stopped")
                if not ask:
                    break
        else:
            break

    my_sum = sum(my_cards)
    comp_sup = sum(computer_cards)
    if my_sum == comp_sup or (my_sum > 21 and comp_sup > 21):
        print(f"Tie (your cards: {my_cards}, " + f"computer's cards: {computer_cards})")
    elif (comp_sup > 21 and my_sum <= 21) or (my_sum > comp_sup and my_sum <= 21):
        print(f"You won!! (your cards: {my_cards}, " + f"computer's cards: {computer_cards})")
    elif (my_sum > 21 and comp_sup <= 21) or (comp_sup > my_sum and comp_sup <= 21):
        print(f"You lost.. (your cards: {my_cards}, " + f"computer's cards: {computer_cards})")