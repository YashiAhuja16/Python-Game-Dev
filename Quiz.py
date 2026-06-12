import pgzrun 

WIDTH = 870
HEIGHT = 650

question_file = "questions.txt" 
marquee_message = "" 
score = 0
time_left = 10 
is_game_over = False
question_count = 0
question_index = 0  


marquee_box = Rect(0,0,880,80)

question_box = Rect(20,100,650,150)

answer_box1 = Rect(20,270,300,150)
answer_box2 = Rect(360,270,300,150)
answer_box3 = Rect(20,450,300,150)
answer_box4 = Rect(360,450,300,150)


answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []


skip_box = Rect(690,270,150,330)
timer_box = Rect(688,100,150,150)

def draw(): 
    global marquee_message
    screen.fill(color= "black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "navyblue")
    screen.draw.filled_rect(answer_box1, "darkorange")
    screen.draw.filled_rect(answer_box2, "darkorange")
    screen.draw.filled_rect(answer_box3, "darkorange")
    screen.draw.filled_rect(answer_box4, "darkorange")
    screen.draw.filled_rect(skip_box, "darkgreen")
    screen.draw.filled_rect(timer_box, "navyblue")
    marquee_message = "Welcome to Quizmaster!"
    skip_message = "Skip"
    screen.draw.textbox(marquee_message,marquee_box, color = "white")
    screen.draw.textbox(str(time_left),timer_box,color = "white")
    screen.draw.textbox(skip_message, skip_box, color = "white", angle = -90)
    screen.draw.textbox(questions(0), question_box, color = "white") 



def read_questionfile(): 
    global question_count
    global questions 
    q_file = open(question_file, "r",)
    for question in q_file: 
        questions.append(question)
        question_count = question_count + 1 
    q_file.close()




pgzrun.go()