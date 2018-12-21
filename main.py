from tkinter import Tk, Frame, Canvas, ALL


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main()
        self.mainloop()

    def main(self):
        self.Wscreen = self.master.winfo_screenwidth()
        self.Hscreen = self.master.winfo_screenheight()
        self.master.title("Particules")
        self.master.bind("<Escape>", lambda e: e.widget.quit())

        canvas = Canvas(
            self.master,
            width=self.Wscreen,
            height=self.Hscreen,
            bg="black")
        canvas.grid()
        self.setup(canvas)

    def setup(self, canvas):

        canvas.part = Particule(canvas, 100, 100, 3, 5)

        self.update(canvas)

    def update(self, canvas):
        canvas.delete(ALL)

        canvas.part.draw()

        self.after(20, lambda: self.update(canvas))


class Particule():
    def __init__(self, canvas, x, y, xspeed, yspeed):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.size = 10

    def draw(self):
        self.canvas.create_oval(
            self.x-self.size,
            self.y-self.size,
            self.x+self.size,
            self.y+self.size,
            fill="green")

        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed

        if (self.x > self.canvas.winfo_screenwidth()) | (self.x < 0):
            self.xspeed = self.xspeed * -1
        elif (self.y > self.canvas.winfo_screenheight()) | (self.y < 0):
            self.yspeed = self.yspeed * -1


if __name__ == "__main__":
    root = Tk()
    App(root)
