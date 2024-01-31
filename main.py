#chess game for two players C.N.C
import pygame

pygame.init() #initialises pygame
width = 1000 #defines the width of the board 
height = 900 #defines the height of the board
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('C.N.C Chess game')
font = pygame.font.Font('freesansbold.ttf', 35) #defines type of font and font size
medium_font = pygame.font.Font('freesansbold.ttf', 35)
big_font = pygame.font.Font('freesansbold.ttf', 54)
timer = pygame.time.Clock()
fps = 90 #number of frames per second

#game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'] #white chess pieces on the board

white_location = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                  (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)] #white chess pieces' position on the board

black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'] #black chess pieces on the board

black_location = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                  (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)] # black chess pieces' position on the board

captured_pieces_white = [] # pieces that have been captured by white
captured_pieces_black = [] # pieces that have been captured by black

# 0 - white turn no selection : 1 - white turn piece selected : 2 - black turn no selection : 3 - black turn piece selected
turn_step = 0
selection = 1000
moves_valid = []

#Add piece images in game(queen, king, rook , knight, bishop, pawn) black
black_queen = pygame.image.load('chess_assets/black queen.png') # loads queen's image onto the board
black_queen = pygame.transform.scale(black_queen, (90, 90)) # scales down queen's image into appropriate size for playing queen
black_queen_small = pygame.transform.scale(black_queen, (45, 45)) #scales down queen's image into appropriate size for captured queen
black_king = pygame.image.load('chess_assets/black king.png') #loads king's image onto board 
black_king = pygame.transform.scale(black_king, (90, 90)) #scales down king's image into appropriate size for playing king
black_king_small = pygame.transform.scale(black_king, (45, 45)) # scales down king's image for checked king
black_bishop = pygame.image.load('chess_assets/black bishop.png') #loads bishop's image onto the board 
black_bishop = pygame.transform.scale(black_bishop, (90, 90)) # scales down bishop's image into appropriate size for playing bishop
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45)) # scales down bishop's image into appropriate size for captured bishop
black_knight = pygame.image.load('chess_assets/black knight.png') # loads knight's image onto the board
black_knight = pygame.transform.scale(black_knight, (90, 90)) #scales down knight's image into appropriate size for playing knight
black_knight_small = pygame.transform.scale(black_knight, (45,45)) # scales down knight's image into appropriate size for capture knight
black_rook = pygame.image.load('chess_assets/black rook.png') #loads rook image onto the board
black_rook = pygame.transform.scale(black_rook, (90, 90)) #scales down rook's image into appropriate size for playing rook
black_rook_small = pygame.transform.scale(black_rook, (45, 45)) #scales down rook's image into appropriate size for captured rook
black_pawn = pygame.image.load('chess_assets/black pawn.png') #loads pawn's image onto the board
black_pawn = pygame.transform.scale(black_pawn, (70, 70)) #scales down pawn's image into appropriate size for playing pawn
black_pawn_small = pygame.transform.scale(black_pawn, (35, 35)) #scales down pawn's image into appropriate size for capture pawn

#white
white_queen = pygame.image.load('chess_assets/white queen.png') #loads queen's image onto the board
white_queen = pygame.transform.scale(white_queen, (90, 90)) #scales down queen's image into appropriate size for playing queen 
white_queen_small = pygame.transform.scale(white_queen, (45, 45)) #scales down queen's image into appropriate size for captured queen
white_king = pygame.image.load('chess_assets/white king.png') #loads king's image onto the board
white_king = pygame.transform.scale(white_king, (90, 90)) #scales down king's image into appropriate size for playing king
white_king_small = pygame.transform.scale(white_king, (45, 45)) #scales down king's image into appropriate size for checked king
white_bishop = pygame.image.load('chess_assets/white bishop.png') #loads bishop image onto the board
white_bishop = pygame.transform.scale(white_bishop, (90, 90)) #scales down bishp's image into appropriate image for playing bishop
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45)) #scales down bishop image into appropriate image for captured bishop
white_rook = pygame.image.load('chess_assets/white rook.png') #loads rook's image onto the board 
white_rook = pygame.transform.scale(white_rook, (90, 90)) #scales down rook's image into appropriate size for playing rook
white_rook_small = pygame.transform.scale(white_rook, (45, 45)) #scales down rook's image into appropriate size for captured rook
white_knight = pygame.image.load('chess_assets/white knight.png') #loads knight's image onto the board
white_knight = pygame.transform.scale(white_knight, (90, 90)) #scales down knight's image into appropriate size for playing knight
white_knight_small = pygame.transform.scale(white_knight, (45, 45 )) #scales down knight's image into appropriate size for captured knight
white_pawn = pygame.image.load('chess_assets/white pawn.png') #loads pawn's image onto the board
white_pawn = pygame.transform.scale(white_pawn, (70, 70)) #scales down pawn's image into appropriate size for playing pawn
white_pawn_small = pygame.transform.scale(white_pawn, (35, 35)) #scales down pawn's image into appropriate size for captured pawn

#operational lists
white_images = [white_king, white_queen, white_rook, white_bishop, white_knight, white_pawn]
white_images_small = [white_king_small, white_queen_small, white_rook_small, white_bishop_small, white_knight_small, white_pawn_small]
black_images = [black_king, black_queen, black_rook, black_bishop, black_knight, black_pawn]
black_images_small = [black_king_small, black_queen_small, black_rook_small, black_bishop_small, black_knight_small, black_pawn_small]
piece_list = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

#check variables flashing counter
counter = 0
winner = ''
game_over = False

# Drawing chess board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light blue', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light blue', [700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'light green', [0, 800, width, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, width, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, height], 5)
        status_text = ['White: Select a piece!', 'White: Select a destination!',
                       'Black: Select a piece!', 'Black: Select a destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i , 800), 2)
        screen.blit(medium_font.render('FOREFEIT', True, 'black'), (810, 810))


# Drawing pieces on the board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_location[i][0] * 100 + 22, white_location[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_location[i][0] * 100 + 10, white_location[i][1] * 100 + 10))

        # highlighting white piece when selected
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'gold', [white_location[i][0] * 100 + 1, white_location[i][1] * 100 + 1, 100, 100], 2) 


    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_location[i][0] * 100 + 22, black_location[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_location[i][0] * 100 + 10, black_location[i][1] * 100 + 10))

        # highlighting black piece when selected
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'gold', [black_location[i][0] * 100 + 1, black_location[i][1] * 100 + 1, 100, 100], 2)


#function to check valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

#valid pawn moves
def check_pawn(position, colour):
    moves_list = []
    if colour == 'white':
        if (position[0], position[1] + 1) not in white_location \
            and(position[0], position[1] + 1) not in black_location and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
            if (position[0], position[1] + 2) not in white_location \
                and(position[0], position[1] + 2) not in black_location and position[1] == 1:
                moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_location:
            moves_list.append((position[0] + 1, position[1] + 1)) # attack vector
        if (position[0] - 1, position[1] + 1) in black_location:
            moves_list.append((position[0] -  1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_location \
            and(position[0], position[1] - 1) not in black_location and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
            if (position[0], position[1] - 2) not in white_location \
                and(position[0], position[1] - 2) not in black_location and position[1] == 6:
                moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_location:
            moves_list.append((position[0] + 1, position[1] - 1)) # attack vector
        if (position[0] - 1, position[1] - 1) in white_location:
            moves_list.append((position[0] -  1, position[1] - 1))
    return moves_list

#valid knight moves
def check_knight(position, colour):
    moves_list = []
    if colour == 'white':
        opponent_list = black_location
        ally_list = white_location
    else:
        opponent_list = white_location
        ally_list =black_location
    #check 8 squares as knights move in l-shape i.e 2squares in one direction, 1 square in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in ally_list and 0 <= target[0] <= 7 and 0 <= target[1] <=7:
            moves_list.append(target)
    return moves_list
        

# valid bishop moves 
def check_bishop(position, colour):
    moves_list =[]
    if colour  == 'white':
        opponent_list = black_location
        ally_list = white_location
    else:
        opponent_list = white_location
        ally_list = black_location
    for i in range(4): #up-right, down- right, up-left, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if(position[0] + (chain * x), position[1] + (chain * y))  not in ally_list and \
                0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in opponent_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list



#valid rook moves
def check_rook(position, colour):
    moves_list = []
    if colour == 'white':
        opponent_list = black_location
        ally_list = white_location
    else:
        opponent_list = white_location
        ally_list = black_location
    for i in range(4): #down, up , right left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if(position[0] + (chain * x), position[1] + (chain * y))  not in ally_list and \
                0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in opponent_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

#valid queen moves
def check_queen(position, colour):
    moves_list = check_bishop(position, colour)
    rook_list = check_rook(position, colour)
    for i in range(len(rook_list)):
        moves_list.append(rook_list[i])
    return moves_list

#valid king moves
def check_king(position, colour):
    moves_list = []
    if colour == 'white':
        opponent_list = black_location
        ally_list = white_location
    else:
        opponent_list = white_location
        ally_list = black_location
    #8 squares to check for king to move as it can move one square in any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in ally_list and 0 <= target[0] <= 7 and 0 <= target[1] <=7:
            moves_list.append(target)
    return moves_list

# drawing captured pieces on board
def draw_captured_pieces():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(black_images_small[index], (825, 5 + 50 *i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(white_images_small[index], (925, 5 + 50 * i))
    

#check for valid moves  for selected piece:
def check_moves_valid():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

# draw valid moves
def draw_valid(moves):
    if turn_step < 2:
        colour = 'gold'
    else:
        colour = 'gold'
    
    for i in range(len(moves)):
        pygame.draw.circle(screen, colour, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50),5)

# checks if king is in check mate
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_location[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_location[king_index][0] * 100 +1,\
                                                            white_location[king_index][1] * 100 + 1, 100, 100], 5)                   
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_location[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [black_location[king_index][0] * 100 +1,\
                                                            black_location[king_index][1] * 100 + 1, 100, 100], 5)
                        
#checks if game is over 
def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 500, 100])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))

#check en passant
def check_en_passant(old_coords, new_coords):
    if turn_step <= 1:
        index = white_location.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] -1)
        piece = white_pieces[index]
    else:
        index = black_location.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] + 1)
        piece = black_pieces[index]
    if piece == 'pawn' and abs(old_coords[1] - new_coords[1]) > 1:
        pass
    else:
        ep_coords(100, 100)
    return ep_coords

# main game loop C.N.C
black_options = check_options(black_pieces, black_location, 'black')
white_options = check_options(white_pieces, white_location, 'white')
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('teal') #Background colour
    draw_board()
    draw_pieces()
    draw_captured_pieces()
    draw_check()
    if selection != 1000:
        moves_valid = check_moves_valid()
        draw_valid(moves_valid)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coords = event.pos[0] // 100
            y_coords = event.pos[1] // 100
            click_coords = (x_coords, y_coords)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_location:
                    selection = white_location.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in moves_valid and selection != 1000:
                    white_location[selection] = click_coords
                    if click_coords in black_location:
                        black_piece = black_location.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_location.pop(black_piece)
                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')
                    turn_step = 2
                    selection = 1000
                    moves_valid = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_location:
                    selection = black_location.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in moves_valid and selection != 1000:
                    black_location[selection] = click_coords
                    if click_coords in white_location:
                        white_piece = white_location.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_location.pop(white_piece)
                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')
                    turn_step = 0
                    selection = 1000
                    moves_valid = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'] #white chess pieces on the board

                white_location = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                                (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)] #white chess pieces' position on the board

                black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'] #black chess pieces on the board

                black_location = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                                (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)] # black chess pieces' position on the board

                captured_pieces_white = [] # pieces that have been captured by white
                captured_pieces_black = [] # pieces that have been captured by black
                turn_step = 0
                selection = 1000
                moves_valid = []
                black_options = check_options(black_pieces, black_location, 'black')
                white_options = check_options(white_pieces, white_location, 'white')


    if winner != '':
        game_over = True
        draw_game_over()
    pygame.display.flip()
pygame.QUIT()