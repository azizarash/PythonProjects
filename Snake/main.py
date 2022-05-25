import turtle
import time
import random

# global variable

window = None
snake = []
head = None

direction = 'down'
delay_time = 0.1

food = None
food_color = ''

TURTLE_SIZE = 20
WIDTH = 600
HEIGHT = 600

X_RANGE = (WIDTH - TURTLE_SIZE) / 2
Y_RANGE = (HEIGHT - TURTLE_SIZE) / 2

pen = None
score = 0
high_score = 0

shapes = {
    0: 'circle',
    1: 'square',
    2: 'triangle'
}

colors = {
    0: 'gold',
    1: 'lime green',
    2: 'dark magenta',
    3: 'red',
    4: 'dark orange',
    5: 'deep sky blue',
    6: 'deep pink',
    7: 'light sea green'
}
food_color = ''




# function to set up the main screen

def set_screen():
    """Sets the main screen."""

    global window

    window = turtle.Screen()
    window.title('Snake Game')
    window.bgcolor('grey')
    window.setup(width=WIDTH, height=HEIGHT)
    window.tracer(0)  # False


# function to listen screen events

def listen_events():
    window.listen()
    window.onkeypress(set_up_direction, 'Up')
    window.onkeypress(set_down_direction, 'Down')
    window.onkeypress(set_left_direction, 'Left')
    window.onkeypress(set_right_direction, 'Right')


# keyboard functions

def set_up_direction():
    global direction
    if direction != 'down':
        direction = 'up'


def set_down_direction():
    global direction
    if direction != 'up':
        direction = 'down'


def set_left_direction():
    global direction
    if direction != 'right':
        direction = 'left'


def set_right_direction():
    global direction
    if direction != 'left':
        direction = 'right'


# create the head

def create_head(is_initial=True):
    """Creates the snake head."""

    global head, snake

    # create the head
    head = turtle.Turtle()
    head.shape(shapes[1])  # 20 x 20
    head.speed(0)
    head.penup()

    # start at a higher position
    if is_initial:
        head.goto(0, 200)

    snake.append(head)


# create the score

def create_score():
    global pen

    # create the pen turtle
    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    pen.goto(0, Y_RANGE - 2 * TURTLE_SIZE)
    pen.color('black')

    # initialize the score
    update_score(0)


# update the score

def update_score(score_increment, is_reset=False):
    global score, high_score

    if is_reset:
        score = 0
    else:
        score += score_increment

    if score > high_score:
        high_score = score

    pen.clear()

    pen.write("Score: {0}  |  High Score: {1}".format(score, high_score),
              align='center',
              font=('Arial', 16, 'normal'))


# function to update screen

def update_screen():
    while window._RUNNING:
        # side collisions
        check_border_collisions()

        # body collisions
        check_body_collisions()

        # move the head
        move()

        # delay
        delay(delay_time)

        # create the food
        add_food()

        # eat the food
        eat_food()

        # get rid of upate error
        window.update()


# function for border collisions

def check_border_collisions():
    # if the head position (x, y) is out the ranges (X_RANGE, Y_RANGE) -> we collide

    x = head.xcor()
    y = head.ycor()

    if x <= -X_RANGE or x >= X_RANGE or y <= -Y_RANGE or y >= Y_RANGE:
        # set direction
        global direction
        direction = 'stop'

        # reset screen after 1 second
        delay(1)
        reset()


# body collisions

def check_body_collisions():
    # if the distance betwwen the head and any of the segments is less than the TURTLE_SIZE
    # then this means we collide

    for i, t in enumerate(snake):

        # exclude head
        if i > 0:

            if head.distance(t) < TURTLE_SIZE - 1:
                # set direction
                global direction
                direction = 'stop'

                # reset screen after 1 second
                delay(1)
                reset()


# reset screen fn

def reset():
    # hide the segments of snake
    for t in snake:
        t.goto(40000, 4000)

    # clear the snake
    snake.clear()

    # create a new head
    create_head(is_initial=False)

    # reset the score
    update_score(0, is_reset=True)


# move function

def move():
    if window._RUNNING:

        # move only if the direction is not stop
        if direction != 'stop':
            # move the segments
            move_segments()

            # move the head
            move_head()


# fn to move the head

def move_head():
    # get current coordinate
    x = head.xcor()
    y = head.ycor()

    if direction == 'up':
        head.sety(y + TURTLE_SIZE)
    elif direction == 'down':
        head.sety(y - TURTLE_SIZE)
    elif direction == 'left':
        head.setx(x - TURTLE_SIZE)
    elif direction == 'right':
        head.setx(x + TURTLE_SIZE)


# fn to move segments

def move_segments():
    # move each segment in reverse order -> from last segment
    # move each segment into the position of the previous one
    # ignore the head
    # start from the last one -> len(snake)-1
    # up to head -> 0
    # backwards -> -1

    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)


# delay function

def delay(duration):
    time.sleep(duration)


# create food

def add_food():
    if window._RUNNING:

        global food

        # create a turtle -> single -> Singleton Pattern
        if food == None:
            food = turtle.Turtle()
            food.shape(get_shape())
            food.shapesize(0.5, 0.5)
            food.speed(0)
            food.penup()

            # color
            food.color(get_color())

            # move the food
            move_food(food)


# function to move the food

def move_food(food):
    # x coordinate
    x = random.randint(-X_RANGE, X_RANGE)

    # y coordinate
    y = random.randint(-Y_RANGE, Y_RANGE - 2 * TURTLE_SIZE)

    # replace the food
    food.goto(x, y)


# function to eat the food

def eat_food():
    # check the distance between the head and the food
    if head.distance(food) < TURTLE_SIZE - 1:
        # move the fodd
        move_food(food)

        # change the food shape
        food.shape(get_shape())

        # create a segment for the snake
        create_segment()

        # change the fodd color
        food.color(get_color())

        # update score
        update_score(10)


# function to create segment

def create_segment():
    """Creates a new segment for snake."""

    global snake

    # create a segment
    segment = turtle.Turtle()
    segment.shape(shapes[1])
    segment.speed(0)
    segment.color(food_color)
    segment.penup()

    # position the segment
    x, y = get_last_segment_position()
    segment.goto(x, y)

    # add this segment into snake list
    snake.append(segment)


# last segment position

def get_last_segment_position():
    # last element -> snake[-1]
    x = snake[-1].xcor()
    y = snake[-1].ycor()

    # direction
    # if direction is up -> same x, y is TURTLE_SIZE less
    if direction == 'up':
        y = y - TURTLE_SIZE

    # if direction is up -> same x, y is TURTLE_SIZE more
    elif direction == 'down':
        y = y + TURTLE_SIZE

    # if direction is right -> same y, x is TURTLE_SIZE less
    elif direction == 'right':
        x = x - TURTLE_SIZE

    # if direction is left -> same y, x is TURTLE_SIZE more
    elif direction == 'left':
        x = x + TURTLE_SIZE

    return (x, y)


# %%
# get a random shape

def get_shape():
    index = random.randint(0, len(shapes) - 1)

    return shapes[index]


# get a random color

def get_color():
    global food_color

    index = random.randint(0, len(colors) - 1)
    color = colors[index]

    food_color = color

    return color


set_screen()

# listen keyboard events
listen_events()

create_head()

create_score()

update_screen()

# the last line

turtle.mainloop()
