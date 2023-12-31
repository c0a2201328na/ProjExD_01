import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#1
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_lis = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]#3
    bg_img1 = pg.transform.flip(bg_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = (tmr%3200)
        if tmr % 50 <= 25:
            num= 0
        else:
            num= 1

        
        screen.blit(bg_img, [-x, 0])#4 6
        screen.blit(bg_img1, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        #screen.blit(bg_img, [1600-x, 0])#6
        screen.blit(kk_lis[num], [300, 200])#5
    
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()