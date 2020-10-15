import tkinter
from tkinter import Frame, BOTH, Canvas
import random


#By Caleb Robinson
class Pong(Frame):
    player1 = 0
    player2 = 0
    ballX=50
    ballY=50
    ball = 0
    paddle1 = 0
    paddle2 = 0
    paddle1X = 2
    paddle1Y = 2
    paddle2X = 0
    paddle2Y = 2
    canvas = 0
    ballDX = 2
    ballDY = -2
    winHEIGHT = 0
    winWIDTH = 0
    paddleSpeed = 15
    player1Points = 0
    player2Points = 0
    textLabel = 0
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()

    def key(self, event):
        repr(event.char)
        if event.char == 'w':
            if self.canvas.coords(self.paddle1)[1]>=0:
                self.canvas.move(self.paddle1,0,-self.paddleSpeed)
        if event.char == 's':
            if self.canvas.coords(self.paddle1)[3]<=self.winHEIGHT:
                self.canvas.move(self.paddle1,0,self.paddleSpeed)
        if event.char == 'o':
            if self.canvas.coords(self.paddle2)[1]>=0:
                self.canvas.move(self.paddle2,0,-self.paddleSpeed)
        if event.char == 'l':
            if self.canvas.coords(self.paddle2)[3]<=self.winHEIGHT:
                self.canvas.move(self.paddle2,0,self.paddleSpeed)
        if event.char == 'q':
            self.parent.destroy()

    def tabula(self):
        self.textLabel = self.canvas.create_text(self.winWIDTH/2,self.winHEIGHT/2, text=str(self.player1Points)+" | "+str(self.player2Points),font=("Purisa", 200),fill="#B0B0B0")
        self.canvas.tag_lower(self.textLabel)

    

    def callback(self, event):
        self.focus_set()
        print ("clicked at",event.x,event.y), event.x, event.y

    def motion(self, event):
        coords1 = self.canvas.coords(self.paddle1)
        height1 = coords1[3]-coords1[1]
        coords1[1] = event.y
        coords1[3] = event.y+height1
        self.canvas.coords(self.paddle1,coords1[0],coords1[1],coords1[2],coords1[3])
        self.canvas.coords(self.paddle2,coords1[0]+self.winWIDTH-15,coords1[1],coords1[2]+self.winWIDTH,coords1[3]) 
        

    def Random_line(self):
        self.lineY={}
        self.lineX={}
        for i in range(1,6):
            self.randomWIDTH = random.randint(200,self.winWIDTH-200)
            self.randomHEIGHT = random.randint(50,self.winHEIGHT-50)
            self.lineY["ciara{0}".format(i)] = self.canvas.create_line(self.randomWIDTH,self.randomHEIGHT,self.randomWIDTH,self.randomHEIGHT+random.randint(35,70),width=3, fill="#143C76")
            self.randomWIDTH = random.randint(200,self.winWIDTH-200)
            self.randomHEIGHT = random.randint(50,self.winHEIGHT-50)
            self.lineX["ciara{0}".format(i)] = self.canvas.create_line(self.randomWIDTH,self.randomHEIGHT,self.randomWIDTH+random.randint(35,70),self.randomHEIGHT,width=3, fill="#143C76")

        

    def initUI(self):

        self.paddle2X = self.parent.winfo_screenwidth() - 15
        self.parent.title("Pong")        
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)
        self.winHEIGHT = self.parent.winfo_screenheight()
        self.winWIDTH = self.parent.winfo_screenwidth()
        self.ball = self.canvas.create_oval(0+self.ballX, 0+self.ballY, 10+self.ballX, 10+self.ballY, outline="black", fill="red", width=1)
        self.paddle1 = self.canvas.create_rectangle(0+self.paddle1X, 0+self.paddle1Y, 10+self.paddle1X, 50+self.paddle1Y, outline="#fb0", fill="#fb0")
        self.paddle2 = self.canvas.create_rectangle(0+self.paddle2X, 0+self.paddle2Y, 10+self.paddle2X, 50+self.paddle2Y, outline="#fb0", fill="#fb0")
        self.tabula()
        self.Random_line()
        self.parent.bind("<Key>", self.key)
        self.parent.bind("<Button-1>", self.callback)
        self.parent.bind("<Motion>", self.motion)
        self.canvas.pack(fill=BOTH, expand=1)
        self.after(10, self.doMove)


    def doCollide(self,coords1,coords2):
        height1 = coords1[3]-coords1[1]
        width1 = coords1[2]-coords1[0]
        height2 = coords2[3]-coords2[1]
        width2 = coords2[2]-coords2[0]
        return not (coords1[0] + width1 < coords2[0] or coords1[1] + height1 < coords2[1] or coords1[0] > coords2[0] + width2 or coords1[1] > coords2[1] + height2)


    def end(self):
        self.randomWIDTH = random.randint(200,self.winWIDTH-200)
        self.randomHEIGHT = random.randint(100,self.winHEIGHT-100)
        self.ballDX= random.choice([-1, 1])*self.ballDX
        self.canvas.coords(self.ball,self.randomWIDTH,self.randomHEIGHT,self.randomWIDTH+10,self.randomHEIGHT+10)

    def doMove(self):
        self.canvas.move(self.ball,self.ballDX, self.ballDY)
        if self.canvas.coords(self.ball)[1] <= 0:
            self.ballDY = -self.ballDY
        if self.canvas.coords(self.ball)[3] >= self.winHEIGHT or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.lineX["ciara1"])) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.lineX["ciara2"])) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.lineX["ciara3"])) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.lineX["ciara4"])) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.lineX["ciara5"])):
            self.ballDY = -self.ballDY
        if self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.paddle1)) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.paddle2)) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.lineY["ciara1"])) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.lineY["ciara2"])) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.lineY["ciara3"])) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.lineY["ciara4"])) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.lineY["ciara5"])):
            self.ballDX = -self.ballDX
        if self.canvas.coords(self.ball)[0] <= 0:
            self.end()
            self.player2Points+=1
            self.canvas.delete(self.textLabel)
            self.tabula()
        if self.canvas.coords(self.ball)[2] >= self.winWIDTH:
            self.end()
            self.player1Points+=1
            self.canvas.delete(self.textLabel)
            self.tabula()
        self.after(10, self.doMove)
        


def main():
  
    root = tkinter.Tk()
    ex = Pong(root)
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()  


if __name__ == '__main__':
    main()  