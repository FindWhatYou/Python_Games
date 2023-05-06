import pygame

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the dimensions of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Initialize the Pygame library
pygame.init()

# Create the game window
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# Set the title of the game window
pygame.display.set_caption("Ping Pong")

# Set the starting position and velocity of the ball
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_dx = 5
ball_dy = 5

# Set the starting position of the paddles
left_paddle_y = WINDOW_HEIGHT // 2 - 50
right_paddle_y = WINDOW_HEIGHT // 2 - 50

# Set the dimensions of the paddles
paddle_width = 10
paddle_height = 100

# Set the speed of the paddles
paddle_speed = 10

# Set the score for both players to 0
left_player_score = 0
right_player_score = 0

# Set the font and font size for the score display
font = pygame.font.Font(None, 48)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce the ball off the top and bottom of the screen
    if ball_y <= 0 or ball_y >= WINDOW_HEIGHT:
        ball_dy = -ball_dy

    # Bounce the ball off the left paddle
    if ball_x <= paddle_width and left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
        ball_dx = -ball_dx

    # Bounce the ball off the right paddle
    if ball_x >= WINDOW_WIDTH - paddle_width and right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
        ball_dx = -ball_dx

    # Handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s]:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP]:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        right_paddle_y += paddle_speed

    # Keep the paddles on the screen
    if left_paddle_y < 0:
        left_paddle_y = 0
    if left_paddle_y > WINDOW_HEIGHT - paddle_height:
        left_paddle_y = WINDOW_HEIGHT - paddle_height
    if right_paddle_y < 0:
        right_paddle_y = 0
    if right_paddle_y > WINDOW_HEIGHT - paddle_height:
        right_paddle_y = WINDOW_HEIGHT - paddle_height

    # Check for scoring
    if ball_x <= 0:
        right_player_score += 1
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2
    if ball_x >= WINDOW_WIDTH:
        left_player_score += 1
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2

    # Clear the screen
    screen
