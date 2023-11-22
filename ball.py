import turtle, random

class Ball:
    def __init__(self, color, size, x, y):
        self.__color = color
        self.__size = size
        self.__x = x
        self.__y = y

    @property
    def color(self):
        return self.__color

    @property
    def size(self):
        return self.__size

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def x_velo(self):
        return self.x_velo

    @property
    def y_velo(self):
        return self.y_velo
    
    def draw_circle(self):
        turtle.penup()
        turtle.color(self.__color)
        turtle.fillcolor(self.__color)
        turtle.goto(self.__x, self.__y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.__size)
        turtle.end_fill()
    
    def move_circle(self, canvas_width, canvas_height):
        __vx = random.randint(1, 0.01*canvas_width)
        __vy = random.randint(1, 0.01*canvas_height)
        self.__x += __vx
        self.__y += __vy
        if abs(self.__x + __vx) > (canvas_width - self.__size):
            __vx = -__vx
        if abs(self.__y + __vy) > (canvas_height - self.__size):
            __vy = -__vy