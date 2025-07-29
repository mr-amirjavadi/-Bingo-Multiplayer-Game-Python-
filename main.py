import random
import json


# OopCompanion:suppressRename


# Player class represents each individual player
class Player:
    def __init__(self, name, rand_num, guess_left):
        self._name = name                    # Player's name
        self._rand_num = rand_num            # The random number the player needs to guess
        self._guess_left = guess_left        # Number of guesses left
        self._score = 0                      # Initial score
        self._win_state = False              # Win status (False initially)

    # Check the player's guess against the random number
    def check_answer(self):
        try:
            answer = int(input(f"{self._name}, enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if answer > self._rand_num:
            print("Too high! Try a lower number.")
            self._score -= 2
        elif answer < self._rand_num:
            print("Too low! Try a higher number.")
            self._score -= 2
        else:
            print("Bingo! You guessed it right.")
            self._win_state = True
            self._score += 10

        self._guess_left -= 1
        print(f"{self._guess_left} guesses left.")

    # Returns True if the player has remaining guesses
    def has_guess_left(self):
        return self._guess_left > 0

    # Returns True if the player has won
    def has_won(self):
        return self._win_state

    # Returns the player's name
    def get_name(self):
        return self._name

    # Returns the player's current score
    def get_score(self):
        return self._score

    # Prepares player data for saving
    def to_dict(self):
        return {
            "name": self._name,
            "score": self._score,
            "won": self._win_state
        }

# BingoGame class manages the entire game logic
class BingoGame:
    def __init__(self):
        self.players = []  # List to store all players

    # Add a new player to the game
    def add_player(self):
        name = input("Enter player name: ")
        if any(p.get_name() == name for p in self.players):
            print("Name already exists. Choose another name.")
            return

        # Choose difficulty level
        level = input("Choose difficulty (easy / medium / hard): ").lower()
        if level == "easy":
            rand_num = random.randint(0, 5)
            guess_left = 5
        elif level == "hard":
            rand_num = random.randint(0, 20)
            guess_left = 3
        else:
            rand_num = random.randint(0, 10)
            guess_left = 4
            if level != "medium":
                print("Invalid choice. Defaulting to medium difficulty.")

        # Create the player and add to list
        player = Player(name, rand_num, guess_left)
        self.players.append(player)
        print(f"Player '{name}' added with '{level}' difficulty.\n")

    # Show the list of players
    def show_players(self):
        print("Current players:")
        for i, player in enumerate(self.players, 1):
            print(f"{i}. {player.get_name()}")
        print()

    # Start the game for all players
    def start_game(self):
        print("\n--- Game Started ---")
        for player in self.players:
            print(f"\n{player.get_name()}'s turn")
            while player.has_guess_left() and not player.has_won():
                player.check_answer()

            if not player.has_won():
                print(f"Out of guesses! The number was {player._rand_num}.")

        self.save_results()

    # Save game results to a JSON file
    def save_results(self):
        data = [player.to_dict() for player in self.players]
        with open("data/bingo_results.json", "w") as file:
            json.dump(data, file, indent=4)
        print("\nGame results saved to 'data/bingo_results.json'.")

    # Display saved results from previous games
    def show_results(self):
        try:
            with open("data/bingo_results.json", "r") as file:
                data = json.load(file)
                print("\n--- Previous Game Results ---")
                for entry in data:
                    status = "Won" if entry["won"] else "Lost"
                    print(f"{entry['name']} - Score: {entry['score']} - {status}")
        except FileNotFoundError:
            print("No results found yet.")

    # Show the main menu and handle user choices
    def main_menu(self):
        while True:
            print("""
--- Bingo Game Menu ---
1. Add Player
2. Show Players
3. Start Game
4. Show Previous Results
5. Exit
""")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_player()
            elif choice == '2':
                self.show_players()
            elif choice == '3':
                self.start_game()
            elif choice == '4':
                self.show_results()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

# Entry point of the program
if __name__ == "__main__":
    game = BingoGame()
    game.main_menu()
