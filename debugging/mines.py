def play(self):
    while True:
        self.print_board()
        try:
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break
            # Check for win
            total_cells = self.width * self.height
            revealed_cells = sum(row.count(True) for row in self.revealed)
            if revealed_cells == total_cells - len(self.mines):
                self.print_board(reveal=True)
                print("Congratulations! You've won the game.")
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

