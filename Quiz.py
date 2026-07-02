import pgzrun 

WIDTH = 870
HEIGHT = 650

question_file = "Quizmaster/questions.txt" 
marquee_message = "" 
score = 0
time_left = 20 
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

    marquee_message = marquee_message + f"Q:{question_index} of {question_count}"
    
    skip_message = "Skip"
    screen.draw.textbox(marquee_message,marquee_box, color = "white")
    screen.draw.textbox(str(time_left),timer_box,color = "white")
    screen.draw.textbox(skip_message, skip_box, color = "white", angle = -90)
    screen.draw.textbox(question[0].strip(), question_box, color = "white") 
    index = 1
    for answer_box in answer_boxes: 
        screen.draw.textbox(question[index].strip(), answer_box, color = "white" ) 
        index = index + 1 
def update(): 
    move_marquee()


def read_questionfile(): 
    global question_count
    global questions 
    q_file = open(question_file, "r",)
    for question in q_file: 
        questions.append(question)
        question_count = question_count + 1 
    q_file.close()
def move_marquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0: 
        marquee_box.left = WIDTH 
def read_next_question():
    global question_index
    question_index = question_index + 1 
    return questions.pop(0).split(",")
def on_mouse_down(pos):  
    index = 1 
    for box in answer_boxes:
        if box.collidepoint(pos): 
            if index is int(question[5]): 
                correct_answer() 
            else: 
                game_over()
        index = index + 1 
    if skip_box.collidepoint(pos): 
        skip_question()
def skip_question(): 
    global question, time_left 
    if questions and not is_game_over: 
        question = read_next_question()
        time_left = 20 
    else:
        game_over()
def correct_answer():
    global score, question, time_left, questions 
    score = score + 1 
    if questions: 
        question = read_next_question()
        time_left = 20
    else:
        game_over()
def game_over(): 
    global question, time_left, is_game_over
    time_left = 0
    is_game_over = True 
    message = f"Game Over\n You Got {score} Questions Correct." 
    question = [message,"-","-","-","-",5]
def update_timer(): 
    global time_left
    if time_left: 
        time_left = time_left - 1 
    else:
        game_over()  











read_questionfile()
question = read_next_question() 
clock.schedule_interval(update_timer, 1)
pgzrun.go()
