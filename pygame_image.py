import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton_img = pg.image.load("fig/3.png")#ex2:こうかとんの読み込み
    koukaton_img = pg.transform.flip(koukaton_img, True, False)#左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -(tmr % 3200)
        bg2_img=pg.transform.flip(bg_img, True, False)#ex7
        screen.blit(bg_img, [x, 0])#ex6, ex7:xで計算を代替
        screen.blit(bg2_img, [x + 1600 , 0])#ex7
        screen.blit(bg_img, [x + 3200, 0])#ex7
        screen.blit(koukaton_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)#ex5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()