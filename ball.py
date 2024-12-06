import turtle


class Ball:
    def __init__(self, size, x, y, vx, vy, color, dt):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.mass = 100 * size ** 2
        self.count = 0
        self.dt = dt
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]


    def draw_ball(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x,self.y-self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_ball(self,i):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.x[i] += self.vx[i]*self.dt
        self.y[i] += self.vy[i]*self.dt

    def update_ball_velocity(self, i, canvas_width, canvas_height):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.x[i]) > (canvas_width - self.size):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.y[i]) > (canvas_height - self.size):
            self.vy[i] = -self.vy[i]





