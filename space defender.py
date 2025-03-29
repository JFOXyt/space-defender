import random,pygame,sys

pygame.init()

altura=480
largura=640

def tiro():
    pygame.draw.rect(tela,(255,255,0),(xtiro,ytiro,5,15))

xnave=largura/2
ynave=300
xtiro=xnave+20
ytiro=ynave
xalien=random.randint(30,610)
yalien=30
clock=pygame.time.Clock()

tela=pygame.display.set_mode((largura,altura))

while True:

    tela.fill((0,0,20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()

    nave=pygame.draw.rect(tela,(255,155,0),(xnave,ynave,40,40))
    alien=pygame.draw.rect(tela,(0,200,0),(xalien,yalien,40,40))

    if pygame.key.get_pressed()[pygame.K_a]:
        xnave-=5
    if pygame.key.get_pressed()[pygame.K_d]:
        xnave+=5
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        tiro()


    yalien+=2
    ytiro-=2

    if yalien==480:
        yalien=30
        xalien=random.randint(30,610)

    clock.tick(60)
    pygame.display.update()