import pygame


def hash(value, total):
    def subhash(v, n):
        if n == 0: return v
        a = v * 13
        b = v % 19
        c = (a * b + subhash(a, n-1)) % total
        return c
    return subhash(value, 3)

def softwrite_pixel(c, value, index):
    cord = (int(index % dims[0]), (index // dims[0]) % dims[1])
    color = screen.get_at(cord)
    if c == 0 and color[c] >= value: color[2] = 255
    color[c] = max(color[c], value)
    screen.set_at(cord, color)


pygame.init()
dims = (1000, 500)
screen = pygame.display.set_mode(dims)
print("hi")
running = True
clock = pygame.time.Clock()
i = 0
while running:
    #clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                i = 0
                screen.fill((0,0,0))
    
    ind = hash(i, dims[0]*dims[1])
    softwrite_pixel(0, 255, ind)
    softwrite_pixel(1, 50, i)
    i += 1
    pygame.display.flip()