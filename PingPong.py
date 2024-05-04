from pygame import *
#Игровая сцена:
win_widgh, win_height = 700, 500
window = display.set_mode((win_widgh, win_height))
display.set_caption('Maze')
game = True

background = transform.scale(image.load('Обои.jpg'), (win_widgh, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, sixe_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, sixe_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = sixe_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < win_height - 155:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < win_height - 155:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        
font.init()
font = font.Font(None, 70)

#Персонажи:
player1 = Player('Raketka1.png', 5, 150, 40, 150, 4)
player2 = Player('Raketka2.png', win_widgh - 45, 150, 40, 150, 4)
ball = GameSprite('Ball.png', 300, 200, 50, 50, 1)

speed_x = 5
speed_y = 3

score_1, score_2 = 0, 0

player1_win = font.render('Player 1 win!', True, (19, 203, 240))
player2_win = font.render('Player 2 win!', True, (240, 19, 30))

#Частота смены кадров:
clock = time.Clock()
FPS = 60

#Игровой цикл:
while game:
    window.blit(background, (0, 0))

    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False

    if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
        speed_x *= -1
    
    if ball.rect.x < 0:
        score_2 += 1
        ball.rect.x = 300
        ball.rect.y = 200
        speed_x = 5
        speed_y = 3
    if ball.rect.x > win_widgh - ball.size_x:
        score_1 += 1
        ball.rect.x = 300
        ball.rect.y = 200
        speed_x = -5
        speed_y = 3
    
    score = font.render(f'Score: < {score_1} >< {score_2} >', True, (195, 28, 214))
    window.blit(score, (180, 5))

    if score_2 >= 5:
        window.blit(player2_win, (220, 200))
    elif score_1 >= 5:
        window.blit(player1_win, (220, 200))
        
    if ball.rect.y < 0 or ball.rect.y > win_height - ball.size_y:
        speed_y *= -1
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    player1.reset()
    player2.reset()
    ball.reset()

    player1.update1()
    player2.update2()

    key_pressed = key.get_pressed()
    display.update()