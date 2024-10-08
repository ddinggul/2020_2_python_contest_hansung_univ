#최준서_2011051
import turtle, random, winsound

#이미지 등록 코드 - 리스트를 활용하여 나타내었음
img_1 = ["hansung_bar.gif", "boogie.gif", "grass.gif", "space_1.gif", "space_2.gif", "space_3.gif", "space_4.gif" ]
img_2 = ["hansung_festival.gif", "hansung_night.gif", "hansung_sangsang_1.gif", "hansung_sangsang_2.gif", "hansung_sangsang_3.gif", "hsel_all.gif", "hsel_night.gif", "find_boogie.gif"]
win = turtle.Screen()
win.addshape(img_1[0])
win.addshape(img_1[1])
win.addshape(img_1[2])
win.addshape(img_1[3])
win.addshape(img_1[4])
win.addshape(img_1[5])
win.addshape(img_1[6])

win.addshape("find_boogie.gif")
win.addshape("life.gif")

#게임 제목 설정 코드
win.title("부기를 받아줘!")


#배경 이미지 설정
bgpic_num = 0
win.addshape(img_2[bgpic_num])
win.bgpic(img_2[bgpic_num])
#게임 창 크기 설정 코드
win.setup(1000,800)

win.tracer(0,0)

#공 객체 생성 및 공 이미지 설정 코드
ball=turtle.Turtle()
ball.shape(img_1[1])
ball.up()
ball.goto(0,0)

#처음 시작 시 방향 랜덤 설정 코드
random_choice=[-1,1]
r1=random.choice(random_choice)
r2=random.choice(random_choice)

#코드 처음 실행 시 움직이지 않도록 설정하는 코드
speed = 0
ball.mx=speed
ball.my=speed

#패드, 말풍선 객체 생성 및 위치 조정 코드
pad_1 = turtle.Turtle()
pad_1.shape(img_1[0])
pad_1.up()
pad_1.goto(0,330)

pad_2 = turtle.Turtle()
pad_2.shape(img_1[2])

pad_2.up()
pad_2.goto(0,-330)

space_1 = turtle.Turtle()
space_1.shape(img_1[3])
space_1.up()
space_1.goto(-30,150)

space_2 = turtle.Turtle()
space_2.shape(img_1[4])
space_2.up()
space_2.goto(0,-430)
space_2.ht()

space_3 = turtle.Turtle()
space_3.shape(img_1[5])
space_3.up()
space_3.goto(0,0)
space_3.ht()

space_4 = turtle.Turtle()
space_4.shape(img_1[6])
space_4.up()
space_4.goto(0,0)
space_4.ht()

#점수 표시 텍스트 생성 코드
score_num = 0
score = turtle.Turtle()
score.speed(0)
score.up()
score.color("green")
score.setposition(-50,350)
scorestring = "SCORE: %s"%score_num
score.write(scorestring, align="left", font = (" Arial", 20, "bold"))
score.ht()

#난이도 선택 창 생성 코드
level_list = [0.3, 0.8, 1.3]
level_choice = int(turtle.textinput("난이도 선택", "난이도 '1, 2, 3' 중 하나를 입력하세요(1 = 쉬움, 2 = 중간, 3 = 어려움)")) -1
level = level_list[level_choice]

#시작을 할 때 실행시키는 함수 - 난이도 선택 후 그 속도에 맞춰 게임이 시작되도록 설정함, 게임 설명 말풍선 숨겨지게 설정함
def start():
    speed = level
    ball.mx=speed
    ball.my=speed
    space_1.ht()
    space_3.ht()

#게임을 잠시 중지하고 싶을 때 실행시키는 함수 - 정지 후 다시 실행시켰을 때 원래 가던 방향으로 이동할 수 있도록 설정함
def stop():
    speed = 0
    ball.mx=speed
    ball.my=speed

#터틀 그래픽 상 하단에 있는 패드를 왼쪽으로 움직일 수 있는 함수 
def pad_left(): 
    x_location = pad_2.xcor()
    if x_location<-410:
        x_location+=0
    else:
        x_location+=-20
    pad_2.setx(x_location)

#터틀 그래픽 상 하단에 있는 패드를 오른쪽으로 움직일 수 있는 함수 
def pad_right():
    x_location = pad_2.xcor()
    if x_location>410:
        x_location+=0
    else:
        x_location+=20
    pad_2.setx(x_location)

#키보드를 눌렀을 때 해당하는 함수를 실행시켜 이벤트를 발생시키는 코드
win.listen()
win.onkeypress(start,"space")
win.onkeypress(stop,"x")
win.onkeypress(pad_left,"Left")
win.onkeypress(pad_right,"Right")

#터틀 그래픽 상 하단에 있는 생명(하트)모양을 나타내는 객체를 생성하는 코드
life_1 = turtle.Turtle()
life_1.shape("life.gif")
life_1.up()
life_1.goto(350,-350)
life_2 = turtle.Turtle()
life_2.shape("life.gif")
life_2.up()
life_2.goto(400,-350)
life_3 = turtle.Turtle()
life_3.shape("life.gif")
life_3.up()
life_3.goto(450,-350)
count = 0

#반복문을 활용해 공이 이동하도록 하는 코드
while True:
    win.update()
    ball.setx(ball.xcor()+ball.mx*r1)
    ball.sety(ball.ycor()+ball.my*r2)
    # 터틀 그래픽 상 상단에 있는 패드를 공의 위치에 맞춰 움직일 수 있도록 하는 코드
    pad_1.setx(ball.xcor())
    
    #공이 터틀 그래픽 상 창의 벽면에 부딪혔을 때 공의 방향을 바꾸도록 설정하는 코드 (162줄부터 200줄까지)
    if ball.xcor()>490:
        ball.setx(490)
        winsound.PlaySound("sweep.wav",winsound.SND_ASYNC)
        r1*=-1
        
    if ball.xcor()<-490:
        ball.setx(-490)
        winsound.PlaySound("sweep.wav",winsound.SND_ASYNC)
        r1*=-1
           
    if ball.ycor()>390:
        ball.sety(390)
        winsound.PlaySound("sweep.wav",winsound.SND_ASYNC)
        r2*=-1
        
    if ball.ycor()<-390:
        ball.sety(-390)
        winsound.PlaySound("break.wav",winsound.SND_ASYNC)
        r2*=-1
    #터틀 그래픽 상 하단 벽면에 부딪혔을 때 생명이 하나씩 깎일 수 있도록 하는 코드 (181줄부터 190줄까지)
        count+=1
    if count == 1:
        life_1.ht()
    elif count == 2:
        life_2.ht()
    # 생명이 다 없어졌을 경우 게임이 멈추며 특정 말풍선이 나타나도록 하는 코드
    elif count == 3:
        life_3.ht()
        space_3.st()
        stop()

    if (ball.ycor()<pad_1.ycor()+10 and ball.ycor()>pad_1.ycor()-10) and (ball.xcor()>pad_1.xcor()-50 and ball.xcor()<pad_1.xcor()+50):
        ball.sety(320)
        r2*=-1
        space_2.ht()
        winsound.PlaySound("jump.wav",winsound.SND_ASYNC)
        
    if (ball.ycor()<pad_2.ycor()+10 and ball.ycor()>pad_2.ycor()-10) and (ball.xcor()>pad_2.xcor()-50 and ball.xcor()<pad_2.xcor()+50):
        ball.sety(-320)
        r2*=-1
        winsound.PlaySound("button.wav",winsound.SND_ASYNC)
        
        #공이 터틀 그래픽 상 하단 패드에 부딪혔을 때마다 배경화면의 이미지가 바뀌도록 설정하는 코드 
            #bg_pic의 숫자가 리스트 범위를 벗어나지 않도록 하기 위해 리스트의 마지막 숫자인 7이 되었을 경우 -1로 설정함
            #그 이유 - -1로 설정해야 패드에 부딛혔을 때 0이 되어 정상적으로 처음으로 돌아가기 때문
        bgpic_num+= 1
        win.bgpic(img_2[bgpic_num])
        if bgpic_num==7:
            bgpic_num = -1
        
        #공이 터틀 그래픽 상 하단 패드에 부딪혔을 때마다 터틀 그래픽 상 상단의 점수가 바뀌도록 설정하는 코드
        score_num+= 20
        #점수가 100점을 달성하였을 시에 게임을 정지하고 축하 말풍선을 띄우도록 설정하는 코드
        if score_num==100:
            winsound.PlaySound("finish.wav",winsound.SND_ASYNC)
            stop()
            space_4.st()

        scorestring = "SCORE: %s"%score_num
        score.clear()
        score.write(scorestring, align="left", font = (" Arial", 20, "bold"))

