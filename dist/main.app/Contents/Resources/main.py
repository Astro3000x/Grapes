
from tkinter import *
import random
points = 0

'''
def move_up(event):
   canvas.move(playerig,0,-10)
def move_down(event):
   canvas.move(playerig,0,10)
'''

def move_left(event):
  canvas.move(playerig,-10,0)
  

def move_right(event):
  canvas.move(playerig,10,0)

def eat(event):
  
  lbs = random.randint(0, 100)
  colors = 'orange', 'purple', 'green'
  color = random.choice(colors)

  if lbs == 0:
    print("No grapes :(")
    
  elif lbs <= 10:
    print(f"You ate {lbs}lbs. of grapes.")
    print(color)
    if color == 'green':
      greengrapeig = canvas.create_image(330,0,image=greengrape,anchor=NW,state='normal')
    elif color == 'purple':
      purplegrapeig = canvas.create_image(320,0,image=purplegrape,anchor=NW,state='normal')
    else:
      orangegrapeig = canvas.create_image(310,0,image=orangegrape,anchor=NW,state='normal')

  elif lbs <= 99:
    bunches = lbs/0.84
    print(f"Whoa you just ate {int(bunches)} bunches of grapes!")
    if color == 'green':
      greengrapebunchig = canvas.create_image(330,0,image=greengrapebunch,anchor=NW,state='normal')
    elif color == 'purple':
      purplegrapebunchig = canvas.create_image(320,0,image=purplegrapebunch,anchor=NW,state='normal')
    elif color == 'orange':
      orangegrapebunchig = canvas.create_image(310,0,image=orangegrapebunch,anchor=NW,state='normal')

    print(color)
    
    
  elif lbs == 100:

    print("Whoa you just ate a crate of grapes!")
    if color == 'orange':
      orangegrapecrateig = canvas.create_image(330,0,image=orangecrate,anchor=NW,state='normal')
    elif color == 'purple':
      purplegrapecrateig = canvas.create_image(320,0,image=purplecrate,anchor=NW,state='normal')
    elif color == 'green':
      greengrapecrateig = canvas.create_image(310,0,image=greencrate,anchor=NW,state='normal')
    
    print(color)
  elif lbs > 100:
    print("Hacker! Turn off hacks or get banned")
  l = Label(text = "Eat Those Grapes!")
def start(event):
  opening_screenig = canvas.create_image(state='hidden')


window = Tk()
window.title("Grapes")
window.geometry("1600x1200")
'''
window.bind("<w>",move_up)
window.bind("<s>",move_down)
'''
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<t>",eat)
window.bind("<x>",start)


canvas = Canvas(window,width=1600,height=1200)
canvas.pack()

player = PhotoImage(file='beanidle.png')
playerig = canvas.create_image(0,200,image=player, anchor=NW)

greengrape = PhotoImage(file='greengrape.png')
greengrapeig = canvas.create_image(300,0,image=greengrape,anchor=NW,state='hidden')

purplegrape = PhotoImage(file='purplegrape.png')
purplegrapeig = canvas.create_image(300,0,image=purplegrape,anchor=NW,state='hidden')
orangegrape = PhotoImage(file='orangegrape.png')
orangegrapeig = canvas.create_image(300,0,image=orangegrape,anchor=NW,state='hidden')



purplegrapebunch = PhotoImage(file='purplegrapebunch.png')
purplegrapebunchig = canvas.create_image(300,0,image=purplegrapebunch,anchor=NW,state='hidden')
greengrapebunch = PhotoImage(file='greengrapebunch.png')
purplecrate = PhotoImage(file='purplecrate.png')
purplegrapebunchig = canvas.create_image(300,0,image=purplecrate,anchor=NW,state='hidden')


greencrate = PhotoImage(file='greengrapecrate.png')
purplecrate = PhotoImage(file='purplecrate.png')
orangecrate = PhotoImage(file='orangegrapecrate.png')
greengrapebunchig = canvas.create_image(300,0,image=greengrapebunch,anchor=NW,state='hidden')
orangegrapebunch = PhotoImage(file='orangegrapebunch.png')
orangegrapebunchig = canvas.create_image(300,0,image=orangegrapebunch,anchor=NW,state='hidden')
opening_screen = PhotoImage(file='openingscreen.png')
opening_screenig = canvas.create_image(0,0,image=opening_screen,anchor=NW,state='normal')
window.mainloop()
