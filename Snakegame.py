## Part 1
import tkinter as tk, random 
class SnakeGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.canvas = tk.Canvas(self.win, width = 660, height = 660)
        self.canvas.pack()
        self.board = self.canvas.create_rectangle(30, 30, 630, 630)
        self.player_snake = Snake(330, 330, 'green', self.canvas)
        self.enemy_snake = Enemy(270, 300, 'purple', self.canvas)
        self.food()
        self.gameloop()
        self.win.bind('<Down>',self.player_snake.go_down)
        self.win.bind('<Right>', self.player_snake.go_right)
        self.win.bind('<Left>', self.player_snake.go_left)
        self.win.bind('<Up>', self.player_snake.go_up)
    def restart(self, event):
        self.canvas.delete(self.text)
        self.board = self.canvas.create_rectangle(30, 30, 630, 630)
        self.player_snake = Snake(330, 330, 'green', self.canvas)
        self.food()
        self.win.bind('<Down>',self.player_snake.go_down)
        self.win.bind('<Right>', self.player_snake.go_right)
        self.win.bind('<Left>', self.player_snake.go_left)
        self.win.bind('<Up>', self.player_snake.go_up)
        self.enemy_snake = Enemy(270, 300, 'purple', self.canvas)
        self.gameloop()
    def gameloop(self):
        if self.player_snake.end == False:
            snake_has_eaten = self.player_snake.move(self.food_x, self.food_y)
            if (snake_has_eaten == True):
                self.canvas.delete(self.pellet)
                self.food()
            enemy_has_eaten = self.enemy_snake.move(self.food_x, self.food_y)
            if (enemy_has_eaten == True):
                self.canvas.delete(self.pellet)
                self.food()
            for block in self.player_snake.segments:
                coord = self.canvas.coords(block)
                if coord != [] and  self.enemy_snake.x == coord[0] and self.enemy_snake.y == coord[1]:
                    self.player_snake.end = True
            for block2 in self.enemy_snake.segments:
                coords2 = self.canvas.coords(block2)
                if coords2 != [] and self.player_snake.x == coords2[0] and self.player_snake.y == coords2[1]:
                    self.player_snake.end = True
            self.canvas.after(100, self.gameloop)
        else:
            self.canvas.delete(tk.ALL)
            self.text = self.canvas.create_text(300,300, text = 'Game has ended')
            self.win.bind('r', self.restart)
    def food(self):
        self.food_x = 30*random.randint(1,20)
        self.food_y = 30*random.randint(1,20)
        self.pellet = self.canvas.create_oval(self.food_x, self.food_y, self.food_x + 30, self.food_y + 30, fill = 'red')
        return self.pellet
class Snake:
    def __init__(self, x, y, color, obj):
        self.x = x
        self.y = y
        self.color = color
        self.canvas = obj
        self.snake1 = self.canvas.create_rectangle(self.x, self.y, self.x + 30, self.y + 30, fill = self.color)
        self.segments = [self.snake1]
        self.vx = 0
        self.vy = 0
        self.end = False
    def move(self, food_x, food_y):
        self.x += self.vx
        self.y += self.vy
        self.grow = self.canvas.create_rectangle(self.x, self.y, self.x + 30, self.y + 30, fill = self.color)
        self.segments.insert(0, self.grow)
        remover = self.segments.pop()
        self.canvas.delete(remover)
        for part in self.segments[1:]:
            coords = self.canvas.coords(part)
            if self.x == coords[0] and self.y == coords[1] and self.x + 30 == coords[2] and self.y + 30 == coords[3]:
                self.end = True
        if (self.x == food_x and self.y == food_y):
            self.segments.insert(0, self.canvas.create_rectangle(self.x , self.y, self.x + 30 - self.vx, self.y + 30 - self.vy, fill = self.color))
            return True
        elif self.x - self.vx > 660 or self.y - self.vy > 660 or self.x + 30 < 0 or self. y + 30 < 0:
            self.end = True
    def go_down(self, event):
        self.vx = 0
        self.vy = 30
    def go_right(self, event):
        self.vx = 30
        self.vy = 0
    def go_left(self, event):
        self.vx = -30
        self.vy = 0
    def go_up(self, event):
        self.vx = 0
        self.vy = -30
class Enemy(Snake):
    def __init__(self, x, y, color, obj):
        Snake.__init__(self, x, y, color, obj)
        self.end = False
    def move(self, food_x, food_y):
        self.vx = 30
        self.vy = 30
        if self.x < food_x:
            self.x += self.vx
            self.vy = 0
        elif self.y < food_y:
            self.y += self.vy
            self.vx = 0
        elif self.x > food_x:
            self.x -= self.vx
            self.vy = 0
        elif self.y > food_y:
            self.y -= self.vy
            self.vx = 0
        self.grow = self.canvas.create_rectangle(self.x, self.y, self.x + 30, self.y + 30, fill = self.color)
        self.segments.insert(0, self.grow)
        remove = self.segments.pop()
        self.canvas.delete(remove)
        if (self.x == food_x and self.y == food_y):
            self.segments.insert(0, self.canvas.create_rectangle(self.x, self.y, self.x - self.vx + 30, self.y + 30 - self.vy, fill = self.color))
            return True
SnakeGUI()
tk.mainloop()
        
