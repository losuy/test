#Import the required Libraries
from tkinter import *
import random
import time
#Create an instance of Tkinter frame
win= Tk()

win.title('Photographic memory Analyzer')
#Set the geometry of Tkinter frame
win.geometry("750x250")




def check(sequence, ans, rndm, digit, new_windows):
    new_windows.destroy()

    # ans
    # answer = int(ans.get())

    flag = False
    
    if sequence[int(rndm)] == ans:
        flag = True
    else:
        flag = False

    final_windows = Tk()
    final_windows.title('Photographic memory Analyzer')

    final_windows.geometry("750x250")
    
    if flag:
        Label(final_windows, text='Congrats!!').pack()
    else:
        Label(final_windows, text='Better Luck Next Time').pack()

    Label(final_windows, text='Sequence').pack()
    
    for i in range(0,digit):
        Label(final_windows, text = sequence[i]).pack()
    
    

def input_answer(sequence, digit, windows):
    windows.destroy()
    new_windows = Tk()

    new_windows.title('Photographic memory Analyzer')

    new_windows.geometry("750x250")


    rndm = str(random.randint(0,digit-1))
    Label(new_windows, text = 'Enter The Value at Index Number ' + rndm).pack()
    global ans
    ans = Entry(new_windows)
    ans.pack()
    
    Button(new_windows, text = 'Next', command = lambda:check(sequence, int(ans.get()), rndm, digit, new_windows)).pack()

def play(digit):
    win.destroy()
    windows = Tk()

    windows.title('Photographic memory Analyzer')
    windows.geometry("750x250")
    Label(windows, text = 'guess the number').pack()
    
    sequence = []
    for i in range(0, digit):
        sequence.append(random.randint(0,9))
        num = str(sequence[i])
        Label(windows, text = 'At Index number ' + str(i) + '---[' + num + ']').pack()
    
    Button(windows, text = 'Done memorising', command = lambda:input_answer(sequence, digit, windows)).pack()
    


def begin():
    digit = int(d.get())
    play(digit)
    

Label(win, text = "How many digits would you like to guess?").pack()
d = Entry(win)
d.pack()


Button(win, text = 'okay', command =lambda:begin()).pack()


win.mainloop()