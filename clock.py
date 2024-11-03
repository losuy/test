from tkinter import *
import time

class GUI(Tk):
    def __init__(self):
        super().__init__()

        # here the window layout is made
        self.geometry("600x600")
        self.title("Digital Clock")
        self.resizable(0,0)
        

        # Here the clock window is made
        self.frame= self.create_frame()
        self.canvas = self.create_canvas()

        # creating the clock
        self.create_circle(300,300,200)
        self.text1= self.create_time_text()
        self.text2= self.create_rest_text()
        self.update_clock()
         
    def create_frame(self):
        frame= Frame(self,bg="#000000")
        frame.pack(fill=BOTH,expand=TRUE)
        return frame


    def create_canvas(self):
        canvas = Canvas(self.frame,bg = "#000000",relief=FLAT)
        canvas.pack(fill=BOTH,expand=TRUE)
        return canvas
    
    
    def update_time(self):

        time_text = time.strftime("%I:%M:%S %p")
        self.canvas.itemconfigure(self.text1,
        text=time_text)
        self.canvas.after(1000, self.update_time)

    def update_rest(self):

        time_text = time.strftime("%A  %x")
        self.canvas.itemconfigure(self.text2,
        text=time_text)
        self.canvas.after(1000, self.update_rest)
    
    def update_clock(self):
        self.update_time()
        self.update_rest()

    def create_circle(self,x, y, r): 
        
        
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        self.canvas.create_oval(x0, y0, x1, y1,width=10,
        fill="#000000",outline="#ffff00")
    

    def create_time_text(self):
        
        text = self.canvas.create_text(300,300,text="",
               font="Helvica 42 bold",fill="#ffffff")
        return text
           

    def create_rest_text(self):
        
        text = self.canvas.create_text(300,370,text="",
               font="Helvica 12 bold",fill="#ffffff")
        return text
    

    def run(self):
        self.mainloop()

if __name__=="__main__":
    root = GUI()
    root.run()


    # yes i created it myself