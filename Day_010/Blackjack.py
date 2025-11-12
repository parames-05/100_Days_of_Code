import random as r

# Card art and values
cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}
ascii_cards = {
    "A": """
┌─────────┐
│A        │
│         │
│    ♠    │
│         │
│        A│
└─────────┘""",

    "2": """
┌─────────┐
│2        │
│    ♠    │
│         │
│    ♠    │
│        2│
└─────────┘""",

    "3": """
┌─────────┐
│3        │
│    ♠    │
│    ♠    │
│    ♠    │
│        3│
└─────────┘""",

    "4": """
┌─────────┐
│4        │
│♠       ♠│
│         │
│♠       ♠│
│        4│
└─────────┘""",

    "5": """
┌─────────┐
│5        │
│♠       ♠│
│    ♠    │
│♠       ♠│
│        5│
└─────────┘""",

    "6": """
┌─────────┐
│6        │
│♠   ♠   ♠│
│         │
│♠   ♠   ♠│
│        6│
└─────────┘""",

    "7": """
┌─────────┐
│7        │
│♠   ♠   ♠│
│    ♠    │
│♠   ♠   ♠│
│        7│
└─────────┘""",

    "8": """
┌─────────┐
│8        │
│♠   ♠   ♠│
│♠   ♠   ♠│
│♠   ♠   ♠│
│        8│
└─────────┘""",

    "9": """
┌─────────┐
│9        │
│♠ ♠   ♠ ♠│
│♠   ♠   ♠│
│♠ ♠   ♠ ♠│
│        9│
└─────────┘""",

    "10": """
┌─────────┐
│10       │
│♠ ♠ ♠ ♠ ♠│
│♠ ♠ ♠ ♠ ♠│
│♠ ♠ ♠ ♠ ♠│
│       10│
└─────────┘""",

    "J": """
┌─────────┐
│J        │
│         │
│   ♠♠♠   │
│   JACK  │
│        J│
└─────────┘""",

    "Q": """
┌─────────┐
│Q        │
│         │
│  ♠♠♠♠   │
│  QUEEN  │
│        Q│
└─────────┘""",

    "K": """
┌─────────┐
│K        │
│         │
│  ♠♠♠♠   │
│  KING   │
│        K│
└─────────┘"""
}


def draw_card():
    return r.choice(list(cards.keys()))

def calculate_total(hand):
    total = sum(cards[card] for card in hand)
    # Handle Aces as 1 or 11
    ace_count = hand.count("A")
    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1
    return total

def show_hand(hand, hidden=False):
    if hidden:
        print(ascii_cards[hand[0]])
        print("┌─────────┐\n│ ?       │\n│   ???   │\n│       ? │\n└─────────┘")
    else:
        for card in hand:
            print(ascii_cards[card])

# --- Game starts here ---
print("\nWelcome to Blackjack!\n")

player_hand = [draw_card(), draw_card()]
dealer_hand = [draw_card(), draw_card()]

print("Your cards:")
show_hand(player_hand)
player_total = calculate_total(player_hand)
print(f"Total: {player_total}\n")

print("Dealer shows:")
show_hand(dealer_hand, hidden=True)

# Player turn
while player_total < 21:
    choice = input("\nDo you want to hit (y) or stand (n)? ").lower()
    if choice == "y":
        new_card = draw_card()
        player_hand.append(new_card)
        player_total = calculate_total(player_hand)
        print(f"\nYou drew {new_card}!")
        show_hand(player_hand)
        print(f"Total: {player_total}")
    elif choice == "n":
        break
    else:
        print("Invalid input. Please type 'y' or 'n'.")

# Dealer turn
dealer_total = calculate_total(dealer_hand)
print("\nDealer's turn...")
show_hand(dealer_hand)
print(f"Dealer total: {dealer_total}")

while dealer_total < 17:
    new_card = draw_card()
    dealer_hand.append(new_card)
    dealer_total = calculate_total(dealer_hand)
    print(f"\nDealer drew {new_card}:")
    show_hand(dealer_hand)
    print(f"Dealer total: {dealer_total}")

# --- Results ---
print("\nFinal Results:")
print(f"Your total: {player_total}")
print(f"Dealer total: {dealer_total}")

if player_total > 21:
    print("Bust! You lose.")
elif dealer_total > 21:
    print("Dealer busts! You win!")
elif player_total > dealer_total:
    print("You win!")
elif player_total < dealer_total:
    print("Dealer wins.")
else:
    print("It's a tie!")
