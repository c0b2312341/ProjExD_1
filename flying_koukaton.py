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
    koukaton_rect = koukaton_img.get_rect()#ex8:rectにする
    koukaton_rect.center = 300, 200#ex8:centerとして座標を指定
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        koukaton_x = 0 #演習2:x軸判定用
        koukaton_y = 0 #演習2:y軸判定用

        key_lst = pg.key.get_pressed()#ex8:押下検知
        # if key_lst[pg.K_UP]:
        #     koukaton_rect.move_ip(0, -1)
        #     # print("A")
        # elif key_lst[pg.K_DOWN]:
        #     koukaton_rect.move_ip(0, 1)
        # elif key_lst[pg.K_RIGHT]:
        #     koukaton_rect.move_ip(1, 0)
        # elif key_lst[pg.K_LEFT]:
        #     koukaton_rect.move_ip(-1, 0)
        # else:
        #     koukaton_rect.move_ip(-1, 0) #演習1:elseに左向きの移動
        if key_lst[pg.K_UP]:
            koukaton_y -= 1
        if key_lst[pg.K_DOWN]: #演習2:elifの場合単一の方向のみだが、ifでは同時に複数
            koukaton_y += 1
        if key_lst[pg.K_RIGHT]: #演習2:元の加速度と動作を考慮し、押下時に2の加速度
            koukaton_x += 2
        if key_lst[pg.K_LEFT]:
            koukaton_x -= 1
        koukaton_rect.move_ip(-1 + koukaton_x, 0 + koukaton_y)

        x = -(tmr % 3200)
        bg2_img=pg.transform.flip(bg_img, True, False)#ex7
        screen.blit(bg_img, [x, 0])#ex6, ex7:xで計算を代替
        screen.blit(bg2_img, [x + 1600 , 0])#ex7
        screen.blit(bg_img, [x + 3200, 0])#ex7
        # screen.blit(koukaton_img, [300, 200])
        screen.blit(koukaton_img, koukaton_rect)#ex8:貼り付け

        pg.display.update()
        tmr += 1        
        clock.tick(200)#ex5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()