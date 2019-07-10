import pygame
import sys
pygame.init()
icon = pygame.image.load('0.jpg')
pygame.display.set_icon(icon)

size = width,height = 600,400
screen = pygame.display.set_mode(size,pygame.RESIZABLE)     #窗体可变大小
print(screen)
pygame.display.set_caption('Pygame 壁球')

speed = [1,1]
BLACK = 0,0,0

ball = pygame.image.load('0.jpg')  #pygame 中导入的任何一个对象都是Surface对象
ballrect = ball.get_rect()      # 在pygame 中覆盖图像的矩形对象  rect对象有重要属性：top bottom left right width height 坐标值

fps = 1000
fcclock = pygame.time.Clock()   #创建一个时间对象

still = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) -1)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            elif event.key == pygame.K_ESCAPE:
                sys.exit()

        elif event.type == pygame.VIDEORESIZE:
            size = width,height = event.w,event.h
            screen = pygame.display.set_mode(size,pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                still = False
                ballrect = ballrect.move(event.pos[0] - ballrect.left,event.pos[1] - ballrect.top)      #move方法是两次运动的相对距离
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left,event.pos[1] - ballrect.top)


    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        if ballrect.right > width and ballrect.right + speed[0] > ballrect.right:
            speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
            speed[1] = -speed[1]

    if pygame.display.get_active() and not still:     # pygame.display.get_active() 当窗体最大化时为true
        ballrect = ballrect.move(speed[0], speed[1])
        print(ballrect)

    fcclock.tick(fps)       #调用Clock()类创建的对象中的tick()函数
    screen.fill(BLACK)  # 将背景填充为黑色，不然之前的图片颜色还是存在
    screen.blit(ball, ballrect)  # 将球放进矩形中
      # move函数包括速度方向和速度大小

    pygame.display.update()     # 只重绘变化部分的背景
