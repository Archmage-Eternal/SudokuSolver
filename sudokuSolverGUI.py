import pygame
import time
import SudokuSolver

pygame.font.init()


class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.squares = [[Square(self.board[i][j], i, j, width, height)
                         for j in range(cols)] for i in range(rows)]
        self.model = None
        self.selected = None

    def updateModel(self):
        self.model = [[self.squares[i][j].value
                       for j in range(self.cols)] for i in range(self.rows)]

    def place(self, value):
        row, col = self.selected
        if self.squares[row][col].value == 0:
            self.squares[row][col].set(value)
            self.updateModel()
            if SudokuSolver.is_safe(self.model, row, col, value) and SudokuSolver.solve_puzzle(self.model):
                return True
            else:
                self.squares[row][col].set(0)
                self.squares[row][col].setTemp(0)
                self.updateModel()
                return False

    def sketch(self, value):
        row, col = self.selected
        self.squares[row][col].setTemp(value)

    def draw(self, win):
        # Draw grid lines.
        divisions = self.width/9
        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(win, (0, 0, 0), (0, int(i * divisions)),
                             (self.width, int(i * divisions)), thickness)
            pygame.draw.line(win, (0, 0, 0), (int(i * divisions), 0),
                             (int(i * divisions), self.height), thickness)
        # Draw squares.
        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j].draw(win)

    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j].selected = False

            self.squares[row][col].selected = True
            self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.squares[row][col].value == 0:
            self.squares[row][col].setTemp(0)

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            division = self.width / 9
            x = pos[0] // division
            y = pos[1] // division
            return (int(y), int(x))
        else:
            return None

    def isFinished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.squares[i][j].value == 0:
                    return False

        return True

    def quickSolve(self):
        solution = self.board
        SudokuSolver.solve_puzzle(solution)
        for row in range(9):
            for col in range(9):
                if self.squares[row][col].value == 0:
                    self.squares[row][col].set(solution[row][col])
        self.updateModel()


class Square:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("FiraCode", 40)

        divisions = self.width / 9
        x = self.col * divisions
        y = self.row * divisions

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x+5, y+5))
        elif not self.value == 0:
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (int(x + (divisions/2 - text.get_width()/2)),
                            int(y + (divisions/2 - text.get_height()/2))))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, divisions, divisions), 4)

    def set(self, val):
        self.value = val

    def setTemp(self, val):
        self.temp = val


def redraw_window(win, board, time):
    win.fill((255, 255, 255))
    # Draw timer.
    fnt = pygame.font.SysFont("FiraCode", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0, 0, 0))
    win.blit(text, (540 - 160, 560))
    # Draw grid and board.
    board.draw(win)


def format_time(secs):
    sec = secs % 60
    minute = secs // 60
    return " " + str(minute) + ":" + str(sec)


if __name__ == '__main__':
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku Solver")
    board = Grid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    while run:
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.quickSolve()
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.squares[i][j].temp != 0:
                        if board.place(board.squares[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                        key = None

                        if board.isFinished():
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time)
        pygame.display.update()

pygame.quit()
