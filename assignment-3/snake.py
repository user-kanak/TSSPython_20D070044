import pygame, sys, time, random

#initial game variables

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
change_to = direction

#Parameters for food
food_pos = [0,0]
food_spawn = False

score = 0


# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))



# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()

#defining colors
red = (255,0,0)
green = (0,255,0)
white = (0,0,0)
black = (255,255,255)


def check_for_events():
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
                if direction != 'LEFT':
                    update_snake(True, change_to, snake_pos, snake_body)

            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
                if direction != 'RIGHT':
                    update_snake(True, change_to, snake_pos, snake_body)

            elif event.key == pygame.K_UP:
                change_to = 'UP'
                if direction != 'DOWN':
                    update_snake(True, change_to, snake_pos, snake_body)

            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
                if direction != 'UP':
                    update_snake(True, change_to, snake_pos, snake_body)


def update_snake(snake_turn, direction, snake_pos, snake_body):
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    # Code for making the snake move in the expected direction
    if snake_turn:
        direction = change_to
        snake_turn = False
    
    elif not snake_turn:
        if direction == 'RIGHT':
            snake_pos += [10,0]
            for i in range(len(snake_body)):
                snake_body[i] += [10,0]
        elif direction == 'LEFT':
            snake_pos += [-10,0]
            for i in range(len(snake_body)):
                snake_body[i] += [-10,0]
        elif direction == 'UP':
            snake_pos += [0,10]
            for i in range(len(snake_body)):
                snake_body[i] += [0,10]
        elif direction == 'DOWN':
            snake_pos += [0,-10]
            for i in range(len(snake_body)):
                snake_body[i] += [0,-10]

            
    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.
    if snake_pos == food_pos:
        if direction == 'RIGHT':
            snake_pos += [10,0]
        elif direction == 'LEFT':
            snake_pos += [-10,0]
        elif direction == 'UP':
            snake_pos += [0,10]
        elif direction == 'DOWN':
            snake_pos += [0,-10]
        food_spawn = True
        snake_body.insert(0,snake_pos)
        create_food()
        

    # End the game if the snake collides with the wall or with itself.
    if snake_pos[0] == 0 or snake_pos[0] == frame_size_x or snake_pos[1] == 0 or snake_pos[1] == frame_size_y:    #collide with wall
        game_over()
    for i in range(1,len(snake_body)):
        if snake_pos == snake_body[i]:                                                                         #head collides with body
            game_over()
    
    update_screen()

    
def create_food():
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    if food_spawn:
        food_pos = [random.randrange(10,frame_size_x,10), random.randrange(10,frame_size_y,10)]
        score += 1
        food_spawn = False

        
def show_score(color, font, size):
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    score_img = pygame.font.SysFont(str(font), size).render("Score: " + str(score), True, color)
    game_window.blit(score_img, (80, 30))

    
def update_screen():
    """
    Draw the snake, food, background, score on the screen
    """
    #snake
    for i in range(len(snake_body)):
        pygame.draw.rect(game_window, green, [snake_body[i][0], snake_body[i][1], 10, 10])
    #food
    pygame.draw.rect(game_window, white, [food_pos[0], food_pos[1], 10, 10])
    #score
    show_score(white, 'Times New Roman', 20)
    

def game_over():
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    game_over_img = pygame.font.SysFont(None, 48).render("YOU DIED", True, red)
    score_img = pygame.font.SysFont(str(font), size).render("Score: " + str(score), True, color)
    game_window.blit(score_img, (80, 30))
    game_window.blit(game_over_img, (360, 100))
    
    
    fps_controller.tick(300)
    sys.exit()


# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run
    update_snake(False, 'RIGHT', snake_pos, snake_body)
    check_for_events()
    # To set the speed of the screen
    fps_controller.tick(25)