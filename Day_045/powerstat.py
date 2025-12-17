import requests
import random
import os  # To clear the screen

# A list to hold all our hero 'cards'
all_cards = []

# Let's fetch 10 cards for a 5 vs 5 game
print("Fetching superhero cards from the database...")
for _ in range(10):
    num = random.randint(1, 731)
    TOKEN = "Enter_Your_Token_Here"  # Use your own token if you have one
    ENDPOINT = f"https://superheroapi.com/api/{TOKEN}/{num}"

    response = requests.get(f"{ENDPOINT}/powerstats")
    powerstats_data = response.json()

    # Create a dictionary for the current hero card
    # This keeps all the data together!
    card = {
        'name': powerstats_data.get('name', 'Unknown'),
        'stats': {}
    }


    # A helper function to safely convert 'null' stats to 0
    def clean_stat(value):
        if value == "null" or value is None:
            return 0
        return int(value)


    # Populate the stats, cleaning them as we go
    stats = powerstats_data
    card['stats']['intelligence'] = clean_stat(stats.get('intelligence'))
    card['stats']['strength'] = clean_stat(stats.get('strength'))
    card['stats']['speed'] = clean_stat(stats.get('speed'))
    card['stats']['durability'] = clean_stat(stats.get('durability'))
    card['stats']['power'] = clean_stat(stats.get('power'))
    card['stats']['combat'] = clean_stat(stats.get('combat'))

    all_cards.append(card)

print("All cards fetched!")
# Shuffle the deck to make it random
random.shuffle(all_cards)

# Deal the cards into two hands
player_deck = all_cards[:5]
opponent_deck = all_cards[5:]

print(f"You have {len(player_deck)} cards. The opponent has {len(opponent_deck)} cards.")


# (This code goes after the card dealing code from above)

# Let's reuse the card display function from before
def display_card(card_data):
    name = card_data['name']
    stats = card_data['stats']
    print(f"╔══════════════════════════════╗")
    print(f"║ {name.upper():^28} ║")
    print(f"╠══════════════════════════════╣")
    for stat, value in stats.items():
        print(f"║ {stat.title():<13}: {str(value):<14} ║")
    print(f"╚══════════════════════════════╝")


# --- MAIN GAME LOOP ---
round_num = 1
while len(player_deck) > 0 and len(opponent_deck) > 0:
    # Clear screen for a clean look (optional)
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"--- Round {round_num} ---")
    print(f"Your cards: {len(player_deck)} | Opponent's cards: {len(opponent_deck)}")

    # Get the top card from each deck
    player_card = player_deck.pop(0)
    opponent_card = opponent_deck.pop(0)

    print("\nYour card is:")
    display_card(player_card)

    # Get player's choice
    stat_choice = ""
    while stat_choice not in player_card['stats']:
        stat_choice = input("Choose a stat to compare (e.g., intelligence, strength): ").lower()

    # Get the values for comparison
    player_value = player_card['stats'][stat_choice]
    opponent_value = opponent_card['stats'][stat_choice]

    print(f"\nOpponent's card is {opponent_card['name']}!")
    print(f"Comparing {stat_choice.title()}: Your {player_value} vs. Opponent's {opponent_value}")

    # Determine the winner
    if player_value > opponent_value:
        print("🎉 You win this round! 🎉")
        player_deck.append(player_card)
        player_deck.append(opponent_card)
    elif opponent_value > player_value:
        print("😭 You lose this round! 😭")
        opponent_deck.append(opponent_card)
        opponent_deck.append(player_card)
    else:
        print("💥 It's a draw! 💥 The cards are returned to the decks.")
        player_deck.append(player_card)
        opponent_deck.append(opponent_card)

    round_num += 1
    input("\nPress Enter to continue to the next round...")

# (This code goes after the while loop)

# --- GAME OVER ---
os.system('cls' if os.name == 'nt' else 'clear')
if len(player_deck) > 0:
    print("CONGRATULATIONS! You have won the game! 💪")
else:
    print("GAME OVER. The opponent has won. Better luck next time! 😥")