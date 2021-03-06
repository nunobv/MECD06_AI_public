import pygame

WIDTH, HEIGHT = 500, 645
ROWS, COLS = 9, 7
SQUARE_SIZE = WIDTH//COLS

# IMAGES
BOARD = pygame.transform.scale(
    pygame.image.load('./assets/board.png'), (500, 645))
BLACKBOARD = pygame.transform.scale(
    pygame.image.load('./assets/blackboard.png'), (200, 370))
ALLOWED_MOVES = pygame.transform.smoothscale(
    pygame.image.load('./assets/allowed.png'), (50, 50))
HINT_POS = pygame.transform.smoothscale(
    pygame.image.load('./assets/hint_pos.png'), (50, 50))
HINT_PIECE = pygame.transform.smoothscale(
    pygame.image.load('./assets/hint_piece.png'), (72, 70))
SELECTED = pygame.transform.smoothscale(
    pygame.image.load('./assets/selected.png'), (72, 70))
RED_PIECE = pygame.transform.smoothscale(
    pygame.image.load('./assets/red.png'), (40, 40))
BLACK_PIECE = pygame.transform.smoothscale(
    pygame.image.load('./assets/black.png'), (40, 40))
RED_BTN = pygame.transform.smoothscale(
    pygame.image.load('./assets/red_btn.png'), (80, 28))
YELLOW_BTN = pygame.image.load('./assets/yellow_btn.png')
BLUE_BTN = pygame.transform.smoothscale(
    pygame.image.load('./assets/blue_btn.png'), (80, 28))
GREEN_BTN = pygame.transform.smoothscale(
    pygame.image.load('./assets/green_btn.png'), (160, 40))

RED_SCORE = pygame.transform.smoothscale(
    pygame.image.load('./assets/red_score.png'), (120, 40))
BLACK_SCORE = pygame.transform.smoothscale(
    pygame.image.load('./assets/black_score.png'), (120, 40))

# PLAYERS

P1_TYPE = 1
P2_TYPE = 0
P1AI_LEVEL = 1
P2AI_LEVEL = 1

RED = 10
BLACK = 20

FIRST_MOVE = RED

# ANIMAL ENUM
RAT = 1
CAT = 2
DOG = 3
WOLF = 4
PANTHER = 5
TIGER = 6
LION = 7
ELEPHANT = 8

ANIMALS = (RAT, CAT, DOG, WOLF, PANTHER, TIGER, LION, ELEPHANT)

# ALL COORDINATES BELOW IN (x,y) FORMAT

DIRECTIONS = ((-1, 0), (1, 0), (0, 1), (0, -1))

BLACK_TRAPS = ((0, 2), (0, 4), (1, 3))
RED_TRAPS = ((8, 2), (8, 4), (7, 3))

PONDS = ((3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2),
         (4, 4), (4, 5), (5, 1), (5, 2), (5, 4), (5, 5))

JUMPS = {(3, 0): [(3, 3)],
         (4, 0): [(4, 3)],
         (5, 0): [(5, 3)],

         (3, 6): [(3, 3)],
         (4, 6): [(4, 3)],
         (5, 6): [(5, 3)],

         (3, 3): [(3, 0), (3, 6)],
         (4, 3): [(4, 0), (4, 6)],
         (5, 3): [(5, 0), (5, 6)],

         (2, 1): [(6, 1)],
         (2, 2): [(6, 2)],
         (2, 4): [(6, 4)],
         (2, 5): [(6, 5)],

         (6, 1): [(2, 1)],
         (6, 2): [(2, 2)],
         (6, 4): [(2, 4)],
         (6, 5): [(2, 5)]}

BLACK_DEN = (0, 3)
RED_DEN = (8, 3)

BLACK_LOCATIONS = ((0, 2), (5, 1), (4, 2), (1, 1),
                   (2, 2), (6, 0), (0, 0), (6, 2))
RED_LOCATIONS = ((6, 6), (1, 7), (2, 6), (5, 7),
                 (4, 6), (0, 8), (6, 8), (0, 6))

POS_SCORE = [
    [40, 40, 40, 1000, 40, 40, 40],
    [30, 30, 30, 30, 30, 30, 30],
    [20, 20, 20, 20, 20, 20, 20],
    [10, 10, 10, 10, 10, 10, 10],
    [0, 0, 0, 0, 0, 0, 0],
    [-10, -10, -10, -10, -10, -10, -10],
    [-20, -20, -20, -20, -20, -20, -20],
    [-30, -30, -30, -30, -30, -30, -30],
    [-40, -40, -40, -1000, -40, -40, -40]]

RED_POS_SCORE = [
    [13, 13, 50, 10000, 50, 13, 11],
    [13, 13, 13, 50, 13, 12, 11],
    [13, 13, 13, 13, 11, 11, 10],
    [13, 12, 12, 11, 9, 9, 8],
    [12, 12, 12, 11, 9, 9, 8],
    [11, 12, 12, 10, 9, 9, 8],
    [10, 10, 10, 9, 8, 8, 8],
    [9, 9, 9, 9, 8, 8, 8],
    [8, 8, 8, 0, 8, 8, 8]]

BLACK_POS_SCORE = [
    [-8, -8, -8, 0, -8, -8, -8],
    [-9, -9, -9, -9, -8, -8, -8],
    [-10, -10, -10, -9, -8, -8, -8],
    [-11, -12, -12, -10, -9, -9, -8],
    [-12, -12, -12, -11, -9, -9, -8],
    [-13, -12, -12, -11, -9, -9, -8],
    [-13, -13, -13, -13, -11, -11, -10],
    [-13, -13, -13, -50, -13, -12, -11],
    [-13, -13, -50, -10000, -50, -13, -11]]

MAGIC_NUMBERS = {
    1: [
        [8, 8, 8, 0, 8, 8, 8],
        [9, 9, 9, 9, 8, 8, 8],
        [10, 10, 10, 9, 8, 8, 8],
        [11, 12, 12, 10, 9, 9, 8],
        [12, 12, 12, 11, 9, 9, 8],
        [13, 12, 12, 11, 9, 9, 8],
        [13, 13, 13, 13, 11, 11, 10],
        [13, 13, 13, 50, 13, 12, 11],
        [13, 13, 50, 10000, 50, 13, 11]
    ],
    2: [
        [8, 8, 8, 0, 8, 8, 8],
        [8, 8, 8, 8, 8, 10, 13],
        [8, 8, 8, 8, 10, 10, 10],
        [8, 0, 0, 8, 0, 0, 10],
        [8, 0, 0, 8, 0, 0, 10],
        [8, 0, 0, 10, 0, 0, 10],
        [10, 11, 11, 15, 11, 11, 10],
        [11, 11, 15, 50, 15, 11, 11],
        [11, 15, 50, 10000, 50, 15, 11]
    ],
    3: [
        [8, 8, 8, 0, 12, 12, 8],
        [8, 8, 8, 8, 13, 12, 8],
        [8, 8, 8, 8, 10, 8, 8],
        [8, 0, 0, 8, 0, 0, 8],
        [8, 0, 0, 8, 0, 0, 8],
        [9, 0, 0, 10, 0, 0, 9],
        [9, 10, 11, 15, 11, 10, 9],
        [10, 11, 15, 50, 15, 11, 10],
        [11, 15, 50, 10000, 50, 15, 11]
    ],
    4: [
        [8, 12, 12, 0, 8, 8, 8],
        [8, 10, 13, 8, 8, 8, 8],
        [8, 8, 8, 8, 8, 8, 8],
        [8, 0, 0, 8, 0, 0, 8],
        [8, 0, 0, 8, 0, 0, 8],
        [9, 0, 0, 10, 0, 0, 9],
        [9, 10, 11, 15, 11, 10, 9],
        [10, 11, 15, 50, 15, 11, 10],
        [11, 15, 50, 10000, 50, 15, 11]
    ],
    5: [
        [9, 9, 9, 0, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9],
        [9, 9, 10, 10, 9, 9, 9],
        [10, 0, 0, 13, 0, 0, 10],
        [11, 0, 0, 14, 0, 0, 11],
        [12, 0, 0, 15, 0, 0, 12],
        [13, 13, 14, 15, 14, 13, 13],
        [13, 14, 15, 50, 15, 14, 13],
        [14, 15, 50, 10000, 50, 15, 14]
    ],
    6: [
        [10, 12, 12, 0, 12, 12, 10],
        [12, 12, 12, 12, 12, 14, 12],
        [14, 16, 16, 14, 16, 16, 14],
        [15, 0, 0, 15, 0, 0, 15],
        [15, 0, 0, 15, 0, 0, 15],
        [15, 0, 0, 15, 0, 0, 15],
        [18, 20, 20, 30, 20, 20, 18],
        [25, 25, 30, 50, 30, 25, 25],
        [25, 30, 50, 10000, 50, 30, 25]
    ],
    7: [
        [10, 12, 12, 0, 12, 12, 10],
        [12, 14, 12, 12, 12, 12, 12],
        [14, 16, 16, 14, 16, 16, 14],
        [15, 0, 0, 15, 0, 0, 15],
        [15, 0, 0, 15, 0, 0, 15],
        [15, 0, 0, 15, 0, 0, 15],
        [18, 20, 20, 30, 20, 20, 18],
        [25, 25, 30, 50, 30, 25, 25],
        [25, 30, 50, 10000, 50, 30, 25]
    ],
    8: [
        [11, 11, 11, 0, 11, 11, 11],
        [11, 11, 11, 11, 11, 11, 11],
        [12, 14, 14, 14, 14, 15, 10],
        [12, 0, 0, 12, 0, 0, 12],
        [14, 0, 0, 14, 0, 0, 14],
        [16, 0, 0, 16, 0, 0, 16],
        [18, 20, 20, 30, 20, 20, 18],
        [25, 25, 30, 50, 30, 25, 25],
        [25, 30, 50, 10000, 50, 30, 25]
    ]
}

'''
Foram adicionados pesos diferentes para cada peca no board, conforme tabela seguinte:
    RAT = 500 (pelo valor intrinseco de poder comer o elefante)
    CAT = 200
    DOG = 300
    WOLF = 400
    PANTHER = 500
    TIGER = 800 (valiosa como peca ofensiva devido aos jumps)
    LION = 900 (valiosa como peca ofensiva devido aos jumps)
    ELEPHANT = 1000
'''
POSITION_VALUES = {
    1: [
        [508, 508, 254, 0, 254, 508, 508],
        [509, 509, 509, 255, 508, 508, 508],
        [510, 510, 510, 509, 508, 508, 508],
        [511, 512, 512, 510, 509, 509, 508],
        [512, 512, 512, 511, 509, 509, 508],
        [513, 512, 512, 511, 509, 509, 508],
        [513, 513, 513, 513, 511, 511, 510],
        [513, 513, 513, 550, 513, 512, 511],
        [513, 513, 550, 100000, 550, 513, 511]
    ],
    2: [
        [208, 208, 104, 0, 104, 208, 208],
        [208, 208, 208, 104, 208, 210, 213],
        [208, 208, 208, 208, 210, 210, 210],
        [208, 0, 0, 208, 0, 0, 210],
        [208, 0, 0, 208, 0, 0, 210],
        [208, 0, 0, 210, 0, 0, 210],
        [210, 211, 211, 215, 211, 211, 210],
        [211, 211, 215, 250, 215, 211, 211],
        [211, 215, 250, 100000, 250, 215, 211]
    ],
    3: [
        [308, 308, 154, 0, 161, 312, 308],
        [308, 308, 308, 154, 313, 312, 308],
        [308, 308, 308, 308, 310, 308, 308],
        [308, 0, 0, 308, 0, 0, 308],
        [308, 0, 0, 308, 0, 0, 308],
        [309, 0, 0, 310, 0, 0, 309],
        [309, 310, 311, 315, 311, 310, 309],
        [310, 311, 315, 350, 315, 311, 310],
        [311, 315, 350, 100000, 350, 315, 311]
    ],
    4: [
        [408, 412, 206, 0, 204, 408, 408],
        [408, 410, 413, 204, 408, 408, 408],
        [408, 408, 408, 408, 408, 408, 408],
        [408, 0, 0, 408, 0, 0, 408],
        [408, 0, 0, 408, 0, 0, 408],
        [409, 0, 0, 410, 0, 0, 409],
        [409, 410, 411, 415, 411, 410, 409],
        [410, 411, 415, 450, 415, 411, 410],
        [411, 415, 450, 100000, 450, 415, 411]
    ],
    5: [
        [509, 509, 255, 0, 255, 509, 509],
        [509, 509, 509, 255, 509, 509, 509],
        [509, 509, 510, 510, 509, 509, 509],
        [510, 0, 0, 513, 0, 0, 510],
        [511, 0, 0, 514, 0, 0, 511],
        [512, 0, 0, 515, 0, 0, 512],
        [513, 513, 514, 515, 514, 513, 513],
        [513, 514, 515, 550, 515, 514, 513],
        [514, 515, 550, 100000, 550, 515, 514]
    ],
    6: [
        [810, 812, 406, 0, 406, 812, 810],
        [812, 812, 812, 406, 812, 814, 812],
        [814, 816, 816, 814, 816, 816, 814],
        [815, 0, 0, 815, 0, 0, 815],
        [815, 0, 0, 815, 0, 0, 815],
        [815, 0, 0, 815, 0, 0, 815],
        [818, 820, 820, 830, 820, 820, 818],
        [825, 825, 830, 850, 830, 825, 825],
        [825, 830, 850, 100000, 850, 830, 825]
    ],
    7: [
        [910, 912, 456, 0, 456, 912, 910],
        [912, 914, 912, 456, 912, 912, 912],
        [914, 916, 916, 914, 916, 916, 914],
        [915, 0, 0, 915, 0, 0, 915],
        [915, 0, 0, 915, 0, 0, 915],
        [915, 0, 0, 915, 0, 0, 915],
        [918, 920, 920, 930, 920, 920, 918],
        [925, 925, 930, 950, 930, 925, 925],
        [925, 930, 950, 100000, 950, 930, 925]
    ],
    8: [
        [1011, 1011, 506, 0, 506, 1011, 1011],
        [1011, 1011, 1011, 506, 1011, 1011, 1011],
        [1012, 1014, 1014, 1014, 1014, 1015, 1010],
        [1012, 0, 0, 1012, 0, 0, 1012],
        [1014, 0, 0, 1014, 0, 0, 1014],
        [1016, 0, 0, 1016, 0, 0, 1016],
        [1018, 1020, 1020, 1030, 1020, 1020, 1018],
        [1025, 1025, 1030, 1050, 1030, 1025, 1025],
        [1025, 1030, 1050, 100000, 1050, 1030, 1025]
    ]
}
