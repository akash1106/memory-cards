################################
#-----------------------memory card------------------------------#
#--------------------------done by---------------------------------#
# --------------------------akash-----------------------------------#
################################

import pygame   #importing pygame,random,time and math
import random
import time
import math

na=input("enter your name")

##########  seting the pygame function############
pygame.init()

########## creating screen###################
screen=pygame.display.set_mode((1300,700))
pygame.display.set_caption(" memory cards")     #seting name for the game


clock = pygame.time.Clock()              #use to control speed

icon=pygame.image.load(".\img\icon.png")   # seting icon
pygame.display.set_icon(icon)

font1=pygame.font.Font('freesansbold.ttf',32)  #font
font2=pygame.font.Font('freesansbold.ttf',75)


########-----------------------def function--------------------##########
def font(msg,x,y,col,font=font1):         # function for displaying font
    global score
    screen.blit(font.render(msg,True,col),(x,y))
def img():    # function for appending image into the list
    global card_image
    card_image.append(pygame.image.load('.\img\d1.png'))
    card_image.append(pygame.image.load('.\img\d2.png'))
    card_image.append(pygame.image.load('.\img\d3.png'))
    card_image.append(pygame.image.load('.\img\d4.png'))
    card_image.append(pygame.image.load('.\img\d5.png'))
    card_image.append(pygame.image.load('.\img\d6.png'))
    card_image.append(pygame.image.load('.\img\d7.png'))
    card_image.append(pygame.image.load('.\img\d8.png'))
    card_image.append(pygame.image.load('.\img\d9.png'))
    card_image.append(pygame.image.load('.\img\d10.png'))
    card_image.append(pygame.image.load('.\img\d11.png'))
    card_image.append(pygame.image.load('.\img\d12.png'))
    card_image.append(pygame.image.load('.\img\d13.png'))
    card_image.append(pygame.image.load('.\img\h1.png'))
    card_image.append(pygame.image.load('.\img\h2.png'))
    card_image.append(pygame.image.load('.\img\h3.png'))
    card_image.append(pygame.image.load('.\img\h4.png'))
    card_image.append(pygame.image.load('.\img\h5.png'))
    card_image.append(pygame.image.load('.\img\h6.png'))
    card_image.append(pygame.image.load('.\img\h7.png'))
    card_image.append(pygame.image.load('.\img\h8.png'))
    card_image.append(pygame.image.load('.\img\h9.png'))
    card_image.append(pygame.image.load('.\img\h10.png'))
    card_image.append(pygame.image.load('.\img\h11.png'))
    card_image.append(pygame.image.load('.\img\h12.png'))
    card_image.append(pygame.image.load('.\img\h13.png'))
    card_image.append(pygame.image.load('.\img\c1.png'))
    card_image.append(pygame.image.load('.\img\c2.png'))
    card_image.append(pygame.image.load('.\img\c3.png'))
    card_image.append(pygame.image.load('.\img\c4.png'))
    card_image.append(pygame.image.load('.\img\c5.png'))
    card_image.append(pygame.image.load('.\img\c6.png'))
    card_image.append(pygame.image.load('.\img\c7.png'))
    card_image.append(pygame.image.load('.\img\c8.png'))
    card_image.append(pygame.image.load('.\img\c9.png'))
    card_image.append(pygame.image.load('.\img\c10.png'))
    card_image.append(pygame.image.load('.\img\c11.png'))
    card_image.append(pygame.image.load('.\img\c12.png'))
    card_image.append(pygame.image.load('.\img\c13.png'))
    card_image.append(pygame.image.load('.\img\s1.png'))
    card_image.append(pygame.image.load('.\img\s2.png'))
    card_image.append(pygame.image.load('.\img\s3.png'))
    card_image.append(pygame.image.load('.\img\s4.png'))
    card_image.append(pygame.image.load('.\img\s5.png'))
    card_image.append(pygame.image.load('.\img\s6.png'))
    card_image.append(pygame.image.load('.\img\s7.png'))
    card_image.append(pygame.image.load('.\img\s8.png'))
    card_image.append(pygame.image.load('.\img\s9.png'))
    card_image.append(pygame.image.load('.\img\s10.png'))
    card_image.append(pygame.image.load('.\img\s11.png'))
    card_image.append(pygame.image.load('.\img\s12.png'))
    card_image.append(pygame.image.load('.\img\s13.png'))
    

def ran():          #createing board cards
    global piece, board
    while piece<53:
        ab=random.choice(card_list)  #take the card randomly from the set
        if not ab in board:   
            board.append(ab)
            piece+=1
        
def check():       # chechingfor match
    global check1,check2,see,score
    num1=check2[0]
    num2=check2[1]
    nu1=board[num1]
    nu2=board[num2]
    n1=card_dict[nu1]
    n2=card_dict[nu2]
    if n1==n2:    # if both values are same
        dis[num1]=2
        dis[num2]=2
        check1=[]
        check2=[]
        score+=2
        see=False
    if not n1==n2:   # if both values are not same
        dis[num1]=0
        dis[num2]=0
        check1=[]
        check2=[]
        see=False
def show():   # for dispalying the card  back side image
    global card_image
    x,y=0,0
    q=0
    for i in range(4):
        for j in range(13):
            if dis[q]==0:
                screen.blit(cad,(x,y))
            q+=1
            x+=100
        x=0
        y+=150
def display(x,y,num):   # for displaying the card image
    pygame.draw.rect(screen,(255,255,255),(x,y,100,150))
    c=board[num]
    d=carddict[c]
    dis[num]=1
    screen.blit(card_image[d-1],(x,y))
def check_end():    # for checking for the end
    global end,dis,se1
    end=True
    for i in range (52):
        if dis[i]==0:
            end=False
def check_time():  # setting timer
    global sec,time_,end
    if not end:
        new_sec=time.time()
        if sec<new_sec and new_sec-sec>1:
            time_+=1
            sec=new_sec
def button1(msg,x,y,w,h,ic,ac,fun):
    global me,hi,run,game,cr
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                run=False
                quit
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1:
            if fun==1:
                me=hi=cr=False
                run=game=True
            if fun==2:
                me=cr=game=False
                run=hi=True
            if fun==3:
                me=hi=game=False
                cr=run=True
            if fun==4:
                me=hi=game=run=cr=False
            if fun==5:
                me=run=True
                hi=game=cr=False
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    font(msg,x,y,(0,0,0),font1)
def menu():
    global me,hi,run,game,cr
    while me:
        screen.fill((0,0,254))
        font("memory cards",150,275,(255,0,0),font2)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=me=game=hi=cr=False
        button1("play",750,140,150,50,(0,150,0),(0,255,0),1)
        button1("high",750,280,150,50,(0,150,0),(0,255,0),2)
        button1("credits",750,420,150,50,(0,150,0),(0,255,0),3)
        button1("quit",750,560,150,50,(0,150,0),(0,255,0),4)
        pygame.display.update()
def high():
    global hi,me,run,game,cr
    screen.fill((135,206,235))
    f=open("abc.txt","r")
    lis=f.readlines()
    data1=[]
    for i in lis:
        data1.append(eval(i[:-1]))
    data1.sort(key = lambda x: x[1])
    data1.reverse()
    while hi:
        over=font1.render("name",True,(255,0,0))
        screen.blit(over,(100,50))
        over=font1.render("time",True,(255,0,0))
        screen.blit(over,(350,50))
        a=100
        clock.tick(45)
        for row in data1:
            n=row[0]
            s=str(row[1])
            over=font1.render(n,True,(255,0,0))
            screen.blit(over,(100,a))
            over=font1.render(s,True,(255,0,0))
            screen.blit(over,(350,a))
            a+=50
        button1("back",650,450,100,50,(150,150,0),(200,200,0),5)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               run=hi=False
def cre():
    global hi,run,me,cr,game
    screen.fill((135,206,235))
    while cr:
        clock.tick(45)
        font("done by:",100,100,(200,0,0),font1)
        font("AKASH",100,200,(200,0,0),font1)
        font("12 th",125,300,(200,0,0),font1)
        font("thank you",150,400,(200,0,0),font1)
        button1("back",650,450,100,50,(150,150,0),(200,200,0),5)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                cr=False
        pygame.display.update()

def mys():
    global check_
    check_+=1
    file=open("abc.txt","a")
    val=(na,time_)
    file.write(str(val)+"\n")

######-------------main programme------------######
check_=0
run=True
hi=False
me=True
cr=False
game=False
see=False
end=False
while run:
    menu()
    high()
    cre()
    score=0

    card_list=['d1','d2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13',
               'h1','h2','h3','h4','h5','h6','h7','h8','h9','h10','h11','h12','h13',
               'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13',
               's1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13']               #card list
    card_dict={'d1':1,'d2':2,'d3':3,'d4':4,'d5':5,'d6':6,'d7':7,'d8':8,'d9':9,'d10':10,'d11':11,'d12':12,'d13':13,
               'h1':1,'h2':2,'h3':3,'h4':4,'h5':5,'h6':6,'h7':7,'h8':8,'h9':9,'h10':10,'h11':11,'h12':12,'h13':13,
               'c1':1,'c2':2,'c3':3,'c4':4,'c5':5,'c6':6,'c7':7,'c8':8,'c9':9,'c10':10,'c11':11,'c12':12,'c13':13,
               's1':1,'s2':2,'s3':3,'s4':4,'s5':5,'s6':6,'s7':7,'s8':8,'s9':9,'s10':10,'s11':11,'s12':12,'s13':13}            #card values
    carddict={'d1':1,'d2':2,'d3':3,'d4':4,'d5':5,'d6':6,'d7':7,'d8':8,'d9':9,'d10':10,'d11':11,'d12':12,'d13':13,
               'h1':14,'h2':15,'h3':16,'h4':17,'h5':18,'h6':19,'h7':20,'h8':21,'h9':22,'h10':23,'h11':24,'h12':25,'h13':26,
               'c1':27,'c2':28,'c3':29,'c4':30,'c5':31,'c6':32,'c7':33,'c8':34,'c9':35,'c10':36,'c11':37,'c12':38,'c13':39,
               's1':40,'s2':41,'s3':42,'s4':43,'s5':44,'s6':45,'s7':46,'s8':47,'s9':48,'s10':49,'s11':50,'s12':51,'s13':52}         #card number
    dis=[0,0,0,0,0,0,0,0,0,0,0,0,0, 
         0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0]      #displaying board palce
    check1=[]
    check2=[]
    piece=1
    cad=pygame.image.load('.\img\cad2.png')
    board=[]
    card_image=[]
    time_=0
    card=0
    ran()
    img()
    sec=time.time()
    while game:    # looping
        screen.fill((255,255,255))
        show()
        check_time()
        clock.tick(60)   # for speed 
        font("card remaining:  "+ str(52-score),150,600,(202,158,204))  # for diplaying the no of remaining card
        font("time:  "+str(time_),1000,600,(202,158,204))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:   # to quit
                game=run=me=cr=hi=False
            if not end:
                if event.type==pygame.MOUSEBUTTONDOWN:  # take the position value
                    posx=event.pos[0]
                    posy=event.pos[1]
                    x_=int(math.floor(posx/100))
                    y_=int(math.floor(posy/150))
                    num=x_+(y_*13)
                    if dis[num]==0:   
                        check1.append([x_,y_])  # appending the values into the list
                        check2.append(num)
                        see=True
        if see:
            display(check1[0][0]*100,check1[0][1]*150,check2[0])
            if len(check1)==2:
                display(check1[1][0]*100,check1[1][1]*150,check2[1])
                pygame.display.update()
                time.sleep(1)  # to show the playing card image
                check()
        check_end()
        if end:
            screen.fill((255,0,0))
            font("you win!!!!...",500,300,(0,0,0),font2)
            font("In "+str(time_)+"sec",500,400,(0,0,0),font2)
            if check_==0:
                mys()
            time.sleep(3)
            me=True
            game=False
        pygame.display.update()
pygame.quit()
quit
#############---------------------------------------END---------------------------------------##########
