import turtle
from ball import Ball
from seven import SevenSegments

class RunBall:
    def __init__(self):
        self.num_balls = 5
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.t = 0.0
        self.pq = []
        self.HZ = 4
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        self.ball = Ball(self.num_balls, self.ball_radius, self.canvas_width, self.canvas_height)
        seven_turtle = turtle.Turtle()
        self.my_seven = SevenSegments(seven_turtle)

    def draw_seven(self):
        for i in range(0, 10):
            self.my_seven.clear()
            self.my_seven.draw(i)
            self.my_seven.my_delay()
            turtle.update()

    def run(self):
        # seven = self.seven
        while True:
            turtle.clear()
            self.ball.draw_border()
            for i in range(self.num_balls):
                self.ball.draw(i)
                self.ball.move_ball(i)
                self.ball.update_ball_velocity(i, self.canvas_width, self.canvas_height)
            turtle.update()
            self.draw_seven()

runball = RunBall()
runball.run()