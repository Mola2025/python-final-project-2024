import random

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [RED, BLUE, GREEN]

# Tetromino shapes
SHAPES = [
    [
        ['.....', '.....', '.....', 'OOOO.', '.....'],
        ['.....', '..O..', '..O..', '..O..', '..O..']
    ],
    [
        ['.....', '.....', '..O..', '.OOO.', '.....'],
        ['.....', '..O..', '.OO..', '..O..', '.....'],
        ['.....', '.....', '.OOO.', '..O..', '.....'],
        ['.....', '..O..', '..OO.', '..O..', '.....']
    ],
    [
        ['.....', '.....', '..OO.', '.OO..', '.....'],
        ['.....', '.....', '.OO..', '..OO.', '.....'],
        ['.....', '.O...', '.OO..', '..O..', '.....'],
        ['.....', '..O..', '.OO..', '.O...', '.....']
    ],
    [
        ['.....', '..O..', '..O.', '..OO.', '.....'],
        ['.....', '...O.', '.OOO.', '.....', '.....'],
        ['.....', '.OO..', '..O..', '..O..', '.....'],
        ['.....', '.....', '.OOO.', '.O...', '.....']
    ],
]


class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        # You can choose different colors for each shape
        self.color = random.choice(COLORS)
        self.rotation = 0
