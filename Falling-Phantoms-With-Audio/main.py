import turtle
# Note: turtle supports gif images only
# Note: turtle coordinates have (0,0) in the center
import random
# Import the Audio
from replit import audio
# Audio => audio.play_file("filename.wav")
gems = 0
lives = 5
level = 1

wn = turtle.Screen()
wn.title("Falling Phantoms")
wn.bgcolor("black")
wn.bgpic("lost_ruins.gif")

wn.setup(width = 800, height = 600)
wn.tracer(0)

# player - 2 Sprites avaliable (Add fox_)
S = "rest.gif"
R = "right.gif"
L = "left.gif"
wn.register_shape(R)
wn.register_shape(L)
wn.register_shape(S)

# guys
wn.register_shape("gems.gif")
wn.register_shape("phantom.gif")

# Player
player = turtle.Turtle()
player.speed(0)
player.shape(S)
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Create a list of good guys
coins = []
gem = "gems.gif"
# Add the good guys
for _ in range(10):
    coin = turtle.Turtle()
    coin.speed(0)
    coin.shape(gem)
    coin.penup()
    coin.goto(-200, 400)
    coin.speed = random.randint(2, 5)
    coins.append(coin)

# Create = list of bad guys
phantoms = []

# Add the bad guys
for _ in range(8):
    phantom = turtle.Turtle()
    phantom.speed(0)
    phantom.shape("phantom.gif")
    phantom.penup()
    phantom.goto(200, 400) # Change this create variable for coordinates
    phantom.speed = random.uniform(1, 4)
    phantoms.append(phantom)
    

# Make the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)
font = ("Courier", 24, "normal")
pen.write("Level:{}  Gems:{}  Lives:{}".format(level, gems, lives), align = "center", font = font)

# Definitions

  # Game Over
def game_over():
  pen = turtle.Turtle()
  pen.hideturtle()
  pen.color("white")
  pen.penup()
  pen.goto(0, -25)
  font = ("Courier", 50, "normal")
  pen.write("GAME OVER", align = "center", font = font)
  audio.play_file('game_over.wav')

  # You Win
def you_win():
  pen = turtle.Turtle()
  pen.hideturtle()
  pen.color("white")
  pen.penup()
  pen.goto(0, -25)
  font = ("Courier", 50, "normal")
  pen.write("YOU WIN", align = "center", font = font)
  audio.play_file('you_win.wav')

  # Level up Audio - Audio Glitch
#def lvl_audio():
  #audio.play_file('up.wav')

# Functions
def left():
  player.direction = "left"
  player.shape(L)
  
def right():
  player.direction = "right"
  player.shape(R)
 
def stop():
  player.direction = "stop"
  player.shape(S)

# Keyboard Binding
wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(stop, "Down")

#Main game loop
running = True
while running:
  # Update screen
  wn.update()

  # Move the player
  if player.direction == "left":
    x = player.xcor()
    x -= 1.5
    player.setx(x)
  
   # Check player not off screen
  elif player.xcor() <= -360:
      player.goto(-360, -250)
  elif player.xcor() >= 360:
      player.goto(360, -250)

  if player.direction == "right":
    x = player.xcor()
    x += 1.5
    player.setx(x)
  
  # Check player not off screen
  elif player.xcor() <= -360:
      player.goto(-360, -250)
  elif player.xcor() >= 360:
      player.goto(360, -250)

  # Move the good guys
  for coin in coins:
      y = coin.ycor()
      y -= coin.speed
      coin.sety(y)
      # good_guy.sety(good_guy.ycor() - good_guy.speed)

      # Check if off the screen
      if y < -300:
        x = random.randint(-380, 380)
        y = random.randint(300, 400)
        coin.goto(x, y)

      # Check for a collision with the player
      if coin.distance(player) < 40: 
        # Change collision based on size of player image
        # Play gem sound
        audio.play_file('gems.wav')
        x = random.randint(-380, 380)
        y = random.randint(300, 400)
        coin.goto(x, y)
        gems += 10
        pen.clear()
        pen.write("Level:{}  Gems:{}  Lives:{}".format(level, gems, lives), align = "center", font = font)

  # Move the bad guy1s
  for phantom in phantoms:
      y = phantom.ycor()
      y -= phantom.speed
      phantom.sety(y)

      # Check if off the screen
      if y < -300:
        x = random.randint(-380, 380)
        y = random.randint(300, 400)
        phantom.goto(x, y)

      # Check for a collision with the player
      if phantom.distance(player) < 37:
        # Lose Life Audio
        audio.play_file('lose_life.wav')
        x = random.randint(-380, 380)
        y = random.randint(300, 400)
        phantom.goto(x, y)
        gems -= 10
        lives -= 1
        pen.clear()
        pen.write("Level:{}  Gems:{}  Lives:{}".format(level, gems, lives), align = "center", font = font)

  # Levels: Level audio is glitchy & will crash if added
 
  if gems == 200:
    #lvl_audio()
    level = 2
  if gems == 300:
    #lvl_audio()
    level = 3
  if gems == 400:
    #lvl_audio()
    level = 4
  if gems == 500:
    #lvl_audio()
    level = 5
  if gems == 600:
    #lvl_audio()
    level = 6
  if gems == 700:
    #lvl_audio()
    level = 7
  if gems == 800:
    #lvl_audio()
    level = 8
  if gems == 900:
    #lvl_audio()
    level = 9
  if gems == 990:
    #lvl_audio()
    level = 10
  # Winning objective
  if gems == 1000:
    you_win()
    break
  # Game over
  if lives == 0:
    game_over()
    break

wn.mainloop()
