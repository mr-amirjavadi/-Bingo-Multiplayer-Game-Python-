<h1 align="center">🎯 Bingo Game 🎮</h1>
<p align="center">
  A Python OOP-based multiplayer number guessing game with difficulty levels, scoring, and game history.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue?logo=python">
  <img src="https://img.shields.io/badge/project-terminal%20game-lightgrey">
  <img src="https://img.shields.io/badge/status-active-brightgreen">
</p>

---

## 📌 About the Project

Bingo is a fun number-guessing game where each player competes to guess a secret number in limited attempts. This version supports multiple players, difficulty levels, scoring, and saves the results in JSON format.

Designed with 💡 **Object-Oriented Programming** principles in Python for clean, scalable code.

---

## 🚀 Features

- 👥 Multi-player support
- 🔁 Turn-based game logic
- 🎚 3 difficulty levels (easy, medium, hard)
- 🧠 Random number generation per player
- ⭐ Scoring system (+10 for correct, -2 for wrong guesses)
- 💾 Automatic result saving (JSON)
- 📖 View previous game history
- 🔒 Validates user input and prevents name duplication
- 🔧 Fully modular and extensible OOP structure

---

## 📂 Project Structure

```bash
bingo-game/
├── src/                # Main game logic
│   └── main.py
├── data/               # Stored game results
│   └── bingo_results.json
├── docs/               # Documentation (diagrams, notes, etc.)
├── tests/              # Unit tests (future)
├── README.md           # This file
├── requirements.txt    # Dependencies
├── LICENSE             # MIT License
└── .gitignore
```

---

## 🛠 Installation

### ✅ Clone the repo

```bash
git clone https://github.com/your-username/bingo-game.git
cd bingo-game
```

### ✅ (Optional) Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### ✅ Install requirements

```bash
pip install -r requirements.txt
```

### ✅ Run the game

```bash
python src/main.py
```

---

## 🖥️ Game Preview (Terminal UI)

```text
--- Bingo Game Menu ---
1. Add Player
2. Show Players
3. Start Game
4. Show Previous Results
5. Exit

> Enter player name: Sara
> Choose difficulty (easy / medium / hard): hard
> Sara, enter your guess: 15
Too high! Try a lower number.
2 guesses left.
```

---

## 🧪 Future Improvements

- 🪟 GUI with `tkinter` or `pygame`
- 🌐 Web version using Flask or Django
- 🏆 Leaderboard and statistics tracking
- 🎨 Colorful output (with `colorama`)
- ✅ Unit testing with `pytest`

---

## 📜 License

Distributed under the MIT License.  
See [`LICENSE`](LICENSE) for more information.

---

## 🙌 Author

**MohammadAmin Pesarakloo**  
🧠 Python Developer | OOP Enthusiast | Learning by Building  
📧 Email: [your.email@example.com]  
🔗 GitHub: [https://github.com/your-username](https://github.com/your-username)

---

> Made with ❤️ for learning, growth, and fun!
