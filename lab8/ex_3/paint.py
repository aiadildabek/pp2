import pygame

def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)


pygame.init()
screen = pygame.display.set_mode((400, 300))
another_layer = pygame.Surface((400, 300))

done = False
clock = pygame.time.Clock()

x1 = 10
y1 = 10
x2 = 10
y2 = 10

w = 100
h = 100
color = (0, 128, 255)
isMouseDown = False
screen.fill((0, 0, 0))
radius = 10

mode = 'rectangle'

objects = []

class Button():
    def __init__(self, x, y, width, height, color, onclickFunction=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction

        self.fillColor = color

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        objects.append(self)
    
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColor)
        if self.buttonRect.collidepoint(mousePos):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.onclickFunction(self.fillColor)
        
        screen.blit(self.buttonSurface, self.buttonRect)

def myFunction(colar):
    global color
    color = colar

Button(110,7,15,15, (0,0,0), myFunction) # black
Button(110,35,15,15, (128, 128, 128), myFunction) #gray
Button(140,7,15,15, (255,0,0), myFunction) # red
Button(140,35,15,15, (0,255,0), myFunction) # green

screen.fill('white')
another_layer.fill('white')

while not done:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()

                    if not isMouseDown:
                        if keys[pygame.K_r]:
                            mode = "rectangle"
                        
                        if keys[pygame.K_c]:
                            mode = "circle"
                        
                        if keys[pygame.K_e]:
                            mode = "eraser"
                        
                        if keys[pygame.K_p]:
                            mode = "pen"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left click
                        x1 = event.pos[0]
                        y1 = event.pos[1]
                        
                        if y1 >= 50:
                            isMouseDown = True
                    
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        isMouseDown = False
                        another_layer.blit(screen, (0, 0))

                        
                if event.type == pygame.MOUSEMOTION:
                        if isMouseDown:
                            x2 = event.pos[0]
                            y2 = event.pos[1]

                            if y2 >= 50:
                                if mode == "rectangle":
                                    screen.blit(another_layer, (0, 0))
                                    pygame.draw.rect(screen, color, pygame.Rect(getRectangle(x1, y1, x2, y2)), 1)
                                elif mode == "eraser":
                                     pygame.draw.circle(screen, 'white', (x2, y2), radius)
                                elif mode == "circle":
                                     screen.blit(another_layer, (0, 0))
                                     pygame.draw.circle(screen, color,((x1 + x2) / 2, (y1 + y2) / 2), max(abs(x1 - x2), abs(y1 - y2)) // 2, 1)
                                elif mode == "pen":
                                     pygame.draw.circle(screen,color,(x2, y2), radius)
        

        for object in objects:
            object.process()
        
        pygame.display.flip()
        clock.tick(60)
