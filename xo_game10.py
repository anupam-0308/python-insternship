import pygame_10 
pygame_10.init()
screen = pygame_10.display.set_mode((600,600))
pygame_10.display.set_caption("X O Game")
WHITE = (255,255,255)
BLACK = (0,0,0)
size = 200
board = [["","",""],
         ["","",""],
          ["","",""]]
player = "x"
font = pygame_10.font.Font(None, 100)
run = True
while run:
    screen.fill(WHITE)
    pygame_10.draw.line(screen,BLACK,(200,0),(200,600),5)
    pygame_10.draw.line(screen,BLACK,(400,0),(400,600),5)
    pygame_10.draw.line(screen,BLACK,(0,200),(600,200),5)
    pygame_10.draw.line(screen,BLACK,(0,400),(600,400),5)
    for row in range (3):
        for col in range(3):
            if board [row][col] != "":
                text = font.render(board[row][col],True,BLACK)
                screen.blit(text,(col * size +70),(row * size +50))
    for event in pygame_10.event.get():
        if event.type == pygame_10.QUIT:
            run = False
            if event.type==pygame_10.MOUSEBUTTONDOWN:
                mouse_x , mouse_y = pygame_10.mouse.get_pos()
                row = mouse_y //200
                col = mouse_x //200
                if board[row][col]== "":
                    board[row][col]== player
                    if player == "x":
                        player == "o"
                    else:
                        player = "x"
    pygame_10.display.update()
pygame_10.quit()
