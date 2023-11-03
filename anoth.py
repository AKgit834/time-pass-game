import pygame as pg
import sys
from random import randint

class Snake:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen=pg.display.set_mode((600,600))
        self.background=pg.image.load('/home/aadityakaushik/Downloads/bg.jpg')
        self.background=pg.transform.scale(self.background,(600,600))
        self.snake_pos=pg.Vector2(300,300)
        self.point_pos=pg.Vector2(300,300)
        self.x_dir=0
        self.y_dir=0
        self.score=0
        self.clock=pg.time.Clock()
        self.dt=self.clock.tick(60)/1000
        self.speed=30
        self.snake_list=[]
        

    def draw(self):
        self.screen.blit(self.background,(0,0))	
#                                                                        width,height
        for i,j in self.snake_list:
            pg.draw.rect(self.screen,'red',(i,j,30,30))
        pg.draw.rect(self.screen,'green',(self.point_pos.x,self.point_pos.y,30,30))
        pg.display.flip()
        
    def get_input(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_a]:
            self.x_dir=-1
            self.y_dir=0
        if keys[pg.K_d]:
            self.x_dir=1
            self.y_dir=0
        if keys[pg.K_w]:
            self.y_dir=-1
            self.x_dir=0
        if keys[pg.K_s]:
            self.y_dir=1  
            self.x_dir=0   
        self.snake_pos.x+=self.speed*self.x_dir*self.dt
        self.snake_pos.y+=self.speed*self.y_dir*self.dt
        head=[]
        head.append(self.snake_pos.x)
        head.append(self.snake_pos.y)
        self.snake_list.append(head) 
        if len(self.snake_list)>self.score:
            del self.snake_list[0]  
        
    def point_generator(self):
        if self.collision_checker()==1:
            self.point_pos.x=randint(10,550)
            self.point_pos.y=randint(10,550)
            self.score+=30
            self.speed+=10
        
    def collision_checker(self):
        if self.snake_pos.x >= self.point_pos.x and self.snake_pos.x <= self.point_pos.x+30:
            if self.snake_pos.y >= self.point_pos.y and self.snake_pos.y <=self.point_pos.y+30:
                return 1
        if self.point_pos.x >= self.snake_pos.x and self.point_pos.x <= self.snake_pos.x+30:
            if self.point_pos.y >= self.snake_pos.y and self.point_pos.y <=self.snake_pos.y+30:
                return 1
        return 0
        
    def update(self):
        self.get_input()
        self.point_generator()
        self.draw()
        
    def runner(self):
        run=True
        while run:
            for e in pg.event.get():
                if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                    run=False
                    break
            self.update()
        pg.quit()
        

if __name__ == '__main__':
    obj=Snake()
    obj.runner()


