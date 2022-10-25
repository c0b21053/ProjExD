import pygame as pg
import sys
from random import randint


def check_bound(obj_rct, scr_rct):
    
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or obj_rct.right > scr_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate



def main():
    font = pg.font.Font(None, 200)
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    ftori_img = pg.image.load("fig/8.png")
    ftori_img = pg.transform.rotozoom(ftori_img, 0, 3.0)
    ftori_rct = ftori_img.get_rect()
    ftori_rct.center = 800, 600

    bomb_sfc = pg.image.load("fig/bomb.png")   #爆弾画像
    bomb_sfc = pg.transform.rotozoom(bomb_sfc, 0, 0.1)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    drink_sfc = pg.image.load("fig/drink.png")   #ドリンク
    drink_sfc = pg.transform.rotozoom(drink_sfc, 0, 0.1)
    drink_rct = drink_sfc.get_rect()
    drink_rct.center = 100, 750

    vx, vy = +1, +1
    ms = 1
    
    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        clock = pg.time.Clock()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        smode = 0
        if smode == 0:
            scrn_sfc.blit(drink_sfc, drink_rct)
        
        
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:
            tori_rct.centery -= ms
        if key_states[pg.K_DOWN]:
            tori_rct.centery += ms
        if key_states[pg.K_LEFT]:
            tori_rct.centerx -= ms
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx += ms
        
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]:
                tori_rct.centerx += ms
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= ms
        
        if tate == -1:
            if key_states[pg.K_UP]:
                tori_rct.centery += ms
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= ms
        scrn_sfc.blit(tori_sfc, tori_rct)

        
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)

        if tori_rct.colliderect(drink_rct):
            ms += 0.1
            smode = 1


            

        if tori_rct.colliderect(bomb_rct):
            vx, vy = 0, 0
            scrn_sfc.fill((0, 0, 0))
            text = font.render("Game Over", True, (255, 0, 0))
            scrn_sfc.blit(text, [400, 300])
            scrn_sfc.blit(ftori_img, [700,600])


        pg.display.update()
        clock.tick(1000)
    

    pass

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()