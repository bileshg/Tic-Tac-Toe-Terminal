# Tic Tac Toe

This project is a simple implementation of the classic Tic Tac Toe game using Python, designed to run in the command-line interface.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

### Requirements

This project requires the following dependencies:

- Python 3.6+
- Poetry
- terminaltables
- termcolor

### Installation

1. Install [Poetry](https://python-poetry.org/docs/#installation) if you haven't already.

2. Clone the repository:
   ```bash
   git clone https://github.com/bileshg/Tic-Tac-Toe-Terminal
   ```
3. Change to the repository directory:
   ```bash
   cd Tic-Tac-Toe-Terminal
   ```
4. Install the dependencies using Poetry:
   ```bash
   poetry install
   ```

### Usage

1. Run the main.py file to launch the game using Poetry:
   ```bash
   poetry run python main.py
   ```
2. The command-line interface will display the Tic Tac Toe board.

3. Players take turns by entering the number of the empty box they want to mark. The game will automatically detect the winner or a tie.

4. Once the game ends, you can run the `main.py` file again to start a new game.