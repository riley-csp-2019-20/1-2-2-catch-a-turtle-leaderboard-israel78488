
# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
turtleshape = "classic"
turtlesize = 12
turtlecolor = "purple"
score = 0
colors = ["black", "navy", "blue", "red", "orange"]
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False

leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("enter your name")


#-----initialize turtle-----
laahthawahda = trtl.Turtle(shape=turtleshape)
laahthawahda.color(turtlecolor)
laahthawahda.shapesize(turtlesize)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-370, 270)
score_writer.hideturtle()
font_setup = ("Arial", 30, "bold")
score_writer.write(score, font=font_setup)



counter =  trtl.Turtle()
counter.hideturtle()

#-----game functions--------
def turtle_clicked(x,y):
    print("laahthawahda got clicked")
    change_position()
    update_score()


def change_position():
    print("laahthawahda got cicked")
    laahthawahda.penup()
    laahthawahda.ht()
    if not timer_up:
        laahthawahdax = rand.randint(-400,400)
        laahthawahday = rand.randint(-300,300)
        laahthawahda.goto(laahthawahdax, laahthawahday)
        laahthawahda.st()


def spot_clicked(x,y):
  global timer_up
  if (not timer_up):
    update_score()
    change_position()
  else:
    laahthawahda.hideturtle()


def update_score():
    global score
    score+=1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()

  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global laahthawahda

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, laahthawahda, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, laahthawahda, score)



#-----events----------------


wn = trtl.Screen()
wn.bgcolor("gold")
laahthawahda.onclick(turtle_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()

