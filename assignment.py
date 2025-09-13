import turtle as t

def draw_C(center=(0, 0), size=200, color="red"):
    
    x, y = center
    radius = size / 2

    t.pensize(8)
    t.color(color)

    t.penup()
    t.goto(x, y + radius)
    t.setheading(-180) 
    t.pendown()

    t.circle(radius, 270)


def draw_A(center=(0, 0), size=200, color="red"):
    
    x, y = center
    width = size * 0.6       
    cross_y = y + size * 0.5  

    t.pensize(8)
    t.color(color)
  
    t.penup()
    t.goto(x - width/2, y)
    t.pendown()
    t.goto(x, y + size)

    t.penup()
    t.goto(x + width/2, y)
    t.pendown()
    t.goto(x, y + size)

    t.penup()
    t.goto(x - width/4, cross_y)
    t.pendown()
    t.goto(x + width/4, cross_y)


print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for letter A, 2 for letter C)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 1:
            draw_A(center=(0, 0), size=200, color="red")
        elif a == 2:
            draw_C(center=(0,0),size=300,color="red")    
        else:
            print("Please input the value in [1,2]")
    except:
        print("Please input the value in [1,2]")
