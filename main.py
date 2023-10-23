import pygame as pg
import random
import sys
import math

def collision_for_object(player_pos_x,player_pos_y,object_pos_x,object_pos_y):
	#finding distances for collision detection.
	dx_sq=(player_pos_x-object_pos_x)**2

	dy_sq=(player_pos_y-object_pos_y)**2

	distance_btw_centeres = math.sqrt(dx_sq+dy_sq)

	if(distance_btw_centeres <= 25):
		return 1
	return 0
	

pg.init()

screen=pg.display.set_mode((600,600))
player_pos=pg.Vector2(screen.get_height()/2,screen.get_width()/2)
fruit_pos=pg.Vector2(200,200)
clock=pg.time.Clock()
dt=clock.tick(60)/1000
dirx=0
diry=0
running=True
speed=15
background = pg.image.load('/home/aadityakaushik/Downloads/hacker.jpeg') 
snake_dict=[]
font=pg.font.SysFont(None,30)

length=1
while running:
	screen.fill('black')
	screen.blit(background,(0,0))
	sctxt=font.render("Score:"+str(len(snake_dict)),True,"red")
	screen.blit(sctxt,[20,20])
#	pg.display.set_caption('Score:'+str(len(snake_dict)))
	pg.draw.circle(screen,'red',(player_pos.x,player_pos.y),15)	
	#for the real working comment the below code.
	for i in range(length):
			rn=random.randint(0,20)
			if(rn<5):
				pg.draw.circle(screen,'red',(player_pos.x+length,player_pos.y+length),15)	
			elif(5<rn and rn<10):
				pg.draw.circle(screen,'red',(player_pos.x-length,player_pos.y+length),15)	
			elif(10<rn and rn<15):
				pg.draw.circle(screen,'red',(player_pos.x+length,player_pos.y-length),15)
			else:
				pg.draw.circle(screen,'red',(player_pos.x-length,player_pos.y-length),15)


	for i in snake_dict[:len(snake_dict)-1]:
		pg.draw.circle(screen,'red',(i[0],i[1]),15)
		if collision_for_object(player_pos.x,player_pos.y,i[0],i[1]) == 1:
			print('GAME OVER !!')
			running=False
			sys.exit()
	

	keys = pg.key.get_pressed()
	if keys[pg.K_w]:
		dirx=0
		diry=-1
	elif keys[pg.K_s]:
		dirx=0
		diry=1
	elif keys[pg.K_a]:
		diry=0
		dirx=-1
	elif keys[pg.K_d]:
		diry=0
		dirx=1


	#drawing fruit.
	pg.draw.circle(screen,'green',fruit_pos,10)
	

		
	#setting boundaries.
	if(player_pos.x-15 <= 0):
		player_pos.x=15
	elif(player_pos.x+15 >= 600):
		player_pos.x=585
	if(player_pos.y-15 <= 0):
		player_pos.y=15
	elif(player_pos.y+15 >= 600):
		player_pos.y=585
	
	if collision_for_object(player_pos.x,player_pos.y,fruit_pos.x,fruit_pos.y) == 1:
		fruit_pos.x=random.randint(10,590)
		fruit_pos.y=random.randint(10,590)
		if [fruit_pos.x,fruit_pos.y] in snake_dict:
			fruit_pos.x=random.randint(10,590)
			fruit_pos.y=random.randint(10,590)
		speed+=2
		length+=1
		snake_dict.append([player_pos.x,player_pos.y])
	

	

	player_pos.x+=speed*dt*dirx
	player_pos.y+=speed*dt*diry

	pg.display.update()
	for e in pg.event.get():
		if e.type == pg.QUIT or(e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
			running=False
			sys.exit()

		

pg.quit()
