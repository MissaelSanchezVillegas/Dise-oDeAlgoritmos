#candy
from random import randint
from random import choice
import pygame,sys
from pygame.locals import *

class caristas:
	def __init__(self,origen,destino,existe):
		self.existe=existe
		self.origen=origen
		self.destino=destino

class fruta(pygame.sprite.Sprite):
	def __init__(self, posx, posy, image,id):
		pygame.sprite.Sprite.__init__(self)
		
		self.nombre=image
		self.imagen=pygame.image.load(image)
		self.rect=self.imagen.get_rect()
		self.rect.top=posy
		self.rect.left=posx
		self.id=id

	def dibujar(self,ventana):
		ventana.blit(self.imagen, self.rect)

#funcion que verifica todos los vecinos conectados
def vecinos(nodo,arista,frutas):
	vec=set()
	for a,b in arista.items():
		for k,v in b.items():
			if(a==nodo.id and v==True):
					for i in range(0,8):
						for j in range(0,len(frutas[i])):
							if(frutas[i][j].id==k):
								vec.add(frutas[i][j])
	return vec

def fruitcrush():
	pygame.init()
	pygame.mixer.music.load("intro.mp3")
	pygame.mixer.music.play(10)
	sonido=pygame.mixer.Sound("navi.wav")
	mifuente=pygame.font.Font(None,150)
	fuentescore=pygame.font.Font(None,60)
	mitexto=mifuente.render("GAME OVER",0,(255,0,0))
	score=0
	scoretexto=fuentescore.render("score: "+str(score),0,(0,0,0))
	ventana=pygame.display.set_mode((700,550))
	pygame.display.set_caption("Fruit")

	#fondo de pantalla
	fondo=pygame.image.load("fondo.png")
	#letras
	letras=["manzana.png","coco.png","naranja.png","piña.png","sandia.png"]
	#matriz con frutas
	count=0
	frutas = {}
	for i in range(0,8):
		frutas[i]=list()
		for j in range(0,8):
			frutas[i].append(fruta(109+i*62,91+j*49,letras[randint(0,4)],count))
			count+=1

	arista = {}
	for x in range(0,8):
		for y in range(0, len(frutas[x])):
			arista[frutas[x][y].id]={}
			if(x!=0):		
				if(frutas[x][y].nombre==frutas[x-1][y].nombre):
					arista[frutas[x][y].id][frutas[x-1][y].id]=True
					arista[frutas[x-1][y].id][frutas[x][y].id]=True
				else:
					arista[frutas[x][y].id][frutas[x-1][y].id]=False
					arista[frutas[x-1][y].id][frutas[x][y].id]=False
			if(y!=0):
				if(frutas[x][y].nombre==frutas[x][y-1].nombre):
					arista[frutas[x][y].id][frutas[x][y-1].id]=True
					arista[frutas[x][y-1].id][frutas[x][y].id]=True
				else:
					arista[frutas[x][y].id][frutas[x][y-1].id]=False
					arista[frutas[x][y-1].id][frutas[x][y].id]=False


	while True:
		ventana.blit(fondo,(0,0))
		for x in range(0,8):
			for y in range(0, len(frutas[x])):
				if(x!=0 and y<len(frutas[x-1])):
					if(frutas[x][y].nombre==frutas[x-1][y].nombre):
						arista[frutas[x][y].id][frutas[x-1][y].id]=True
						arista[frutas[x-1][y].id][frutas[x][y].id]=True
					else:
						arista[frutas[x][y].id][frutas[x-1][y].id]=False
						arista[frutas[x-1][y].id][frutas[x][y].id]=False
				if(y!=0):
					if(frutas[x][y].nombre==frutas[x][y-1].nombre):
						arista[frutas[x][y].id][frutas[x][y-1].id]=True
						arista[frutas[x][y-1].id][frutas[x][y].id]=True
					else:
						arista[frutas[x][y].id][frutas[x][y-1].id]=False
						arista[frutas[x][y-1].id][frutas[x][y].id]=False
				


		for i in range(0,8):
			for j in range(0,len(frutas[i])):
				frutas[i][j].dibujar(ventana)

		for evento in pygame.event.get():
			if(evento.type==QUIT):
				pygame.quit()
				sys.exit()
			if(evento.type==pygame.MOUSEBUTTONDOWN):
				mouse=pygame.mouse.get_pos()
				for i in range(0,8):
					for j in range(0,len(frutas[i])):

						if (frutas[i][j].rect.left+50>mouse[0]>frutas[i][j].rect.left and frutas[i][j].rect.top+45>mouse[1]>frutas[i][j].rect.top):
							#conjunto de elementos marcados
							sonido.play()
							marcados=set()
							#pila
							pila=[]
							#DFS
							nodo_inicial=frutas[i][j]
							marcados.add(nodo_inicial)
							pila.append(nodo_inicial)
							while(len(pila)>0):
								veci=vecinos(pila[-1],arista,frutas)
								veci=list(veci-marcados)
								verif=list(pila)
								if(len(veci)>0):
									visitado=choice(veci)
									marcados.add(visitado)
									pila.append(visitado)
								else:
									pila.pop()
							score=score+(len(marcados)+10)*len(marcados)
							scoretexto=fuentescore.render("score: "+str(score),0,(0,0,0))
							indices=set()		
							for a in range(0,8):
								for b in range(0,len(frutas[a])):
									if (frutas[a][b] in marcados):
										indices.add(b)
								if(len(indices)>0):
									del frutas[a][min(indices):max(indices)+1]
									if(len(frutas[a])>0):
										for x in range(min(indices),len(frutas[a])):
											frutas[a][x].rect.top=frutas[a][x].rect.top-(len(indices))*49
									indices.clear()
							marcados.clear()
							verif.clear()
							veci.clear()
							for x in arista:
								for y in arista[x]:
									arista[x][y]=False

							
							break
		ventana.blit(scoretexto,(5,500))
		m=0
		for l in range(0,8):
			if(len(frutas[l])==0):
				m=m+1
		if(m==8):
			ventana.blit(mitexto,(40,255))
		pygame.display.update()

fruitcrush()
