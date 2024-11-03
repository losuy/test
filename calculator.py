from tkinter import *

FOREGROUND = "#ffffff"
BACKGROUND = "#000000"

EXPRESSION_LABEL_FONT = "Arial 14 bold"
LABEL_FONT = "Arial 40 bold"
BUTTON_FONT = "Opensans 20 bold"

root = Tk()

root.title("Caculator")
root.geometry("370x600")
root.resizable(0,0)
root.iconbitmap('C:/Users/lol/Pictures/download.ico')


display_frame = Frame(root, height="200",bg = "red")
display_frame.pack(fill = BOTH,expand = TRUE)

button_frame = Frame(root,bg = "yellow")
button_frame.pack(fill = BOTH,expand = TRUE)

expression_value = ""
current_value = ""

expression_label = Label(display_frame,text = expression_value,
font=EXPRESSION_LABEL_FONT,fg=FOREGROUND,bg=BACKGROUND, anchor=E)
expression_label.pack(fill=BOTH,expand= TRUE)
label = Label(display_frame, text = current_value,font=LABEL_FONT,fg=FOREGROUND,
bg=BACKGROUND, anchor=E)
label.pack(fill=BOTH,expand= TRUE)


for x in range(0,4):
    button_frame.columnconfigure(x,weight=1)

for x in range(0,5):
    button_frame.rowconfigure(x,weight=1)    

def update_current_value():
    global label
    label.config(text = current_value[:12])

def evaluate(operator):
    global current_value
    global expression_value

    expression_value += current_value
    update_expression_value()
    try:
        current_value = str(eval(expression_value))
    except ZeroDivisionError:
        current_value = "Math Error"
    except SyntaxError:
        current_value = "Syntax Error"
    finally:
        update_current_value()

def add_to_expression(num):
    global current_value
    current_value += num
    update_current_value()

def update_expression_value():
    global expression_label
    expression_label.config(text = expression_value)


def add_operator(operator):
    global current_value
    global expression_value
    if(operator == "AC"):
        current_value = ""
        update_current_value()
        expression_value = ""
        update_expression_value()
    else:    
        current_value += operator
        expression_value += current_value
        current_value = "" 
        update_expression_value()
        print("hello1")

    return 0

def enter(event):
    btn = event.widget
    btn['bg'] = FOREGROUND
    btn['fg'] = BACKGROUND


def operator_leave(event):
    btn = event.widget
    print(btn)

    btn['bg'] = "#2e2e2e"
    btn['fg'] = FOREGROUND

def number_leave(event):
    btn = event.widget
    btn['bg'] = "#5b5b5b"
    btn['fg'] = FOREGROUND



def sqrt():
    global current_value
    current_value = str(eval(f"{current_value} ** 0.5"))
    update_current_value()   

def sqrt_button():
    b = Button(button_frame,text="\u221ax",
    command=sqrt,font=BUTTON_FONT,bg="#2e2e2e",fg=FOREGROUND,borderwidth = 0)
    b.bind("<Enter>",enter)
    b.bind("<Leave>",lambda a: b.config(background="#2e2e2e",foreground=FOREGROUND))
    b.grid(row = 0,column=3,
    sticky= NSEW)

def equal():
    b = Button(button_frame,text="=",
    command=lambda x= "=": evaluate(x),
    font=BUTTON_FONT,foreground = FOREGROUND,background="#f39700",borderwidth = 0)
    b.bind("<Enter>",enter)
    b.bind("<Leave>",lambda a: b.config(background="#f39700",foreground = FOREGROUND))
    b.grid(row = 3,column=3,
    rowspan =2,sticky= NSEW)
 
def clear():
    b = Button(button_frame,text="AC",
    command=lambda x="AC": add_operator(x),
    font=BUTTON_FONT,background= "#2e2e2e",fg=FOREGROUND,borderwidth = 0)
    b.bind("<Enter>",enter)
    b.bind("<Leave>",lambda a: b.config(background="#2e2e2e",foreground = FOREGROUND))

    b.grid(row = 0,column= 0,
    sticky= NSEW)


def create_operators(list, gridrow = 0,gridcolumn = 0,verticalcreate = False,firstleave = False):
    
    global button_list
    grid_row = gridrow
    grid_column = gridcolumn
    
    for i in range(len(list)):
        if(verticalcreate):
            if (list[i] == "0"):
                pass
            else:
                b = Button(button_frame,text=list[i],
                command=lambda x=i: add_operator(list[x]),
                font=BUTTON_FONT,bg="#2e2e2e",fg = FOREGROUND,borderwidth = 0)

                button_list.append(b)
                b.grid(row = grid_row,column= grid_column,
                sticky= NSEW)
                grid_row += 1 
        
        else:
            if(list[i] == "="):
                pass
            elif (list[i] == "0"):
                b = Button(button_frame,text=list[i],
                command=lambda x=i: add_operator(list[x]),
                font=BUTTON_FONT,bg="#5b5b5b",fg = FOREGROUND,borderwidth = 0)

                button_list.append(b)
                b.grid(row = grid_row,column= grid_column,
                sticky= NSEW)
                grid_column += 1  
            else:
                b = Button(button_frame,text=list[i],
                command=lambda x=i: add_operator(list[x]),
                font=BUTTON_FONT,bg="#2e2e2e",fg = FOREGROUND,borderwidth = 0)
                
                button_list.append(b)
                b.grid(row = grid_row,column= grid_column,
                sticky= NSEW)
                grid_column += 1
        
        if(firstleave):
            b.config(bg ="#5b5b5b" )
            b.bind("<Leave>",number_leave)
        else:
            b.bind("<Leave>",operator_leave)


    return 0

    

def numcreator():

    global button_list
    grid_row = 1
    grid_column = 2
    update_value = 10
    for i in range(9,0,-1):
        if i < update_value - 3:
            grid_row += 1
            grid_column = 2 - 1 
            b = Button(button_frame,text = str(i),
            command=lambda x=str(i): add_to_expression(x),
            font=BUTTON_FONT,bg="#5b5b5b",fg = FOREGROUND,borderwidth = 0)
            b.bind("<Leave>",number_leave)

            button_list.append(b) 
            b.grid(row = grid_row,column = grid_column + 1,sticky= NSEW)
            update_value = i + 1
        
        else:
            b = Button(button_frame,text = str(i),
            command=lambda x=str(i): add_to_expression(x),
            font=BUTTON_FONT,bg="#5b5b5b",fg = FOREGROUND,borderwidth = 0)
            b.bind("<Leave>",number_leave)

            button_list.append(b)
            b.grid(row = grid_row,column = grid_column,sticky= NSEW)
            grid_column -= 1
    
    return 0


def animate_buttons():
    
    global button_list
    for i in range(len(button_list)):
        button_list[i].bind("<Enter>",enter )

button_list = []   
operator = ["*","/"]
create_operators(operator,gridrow=0,gridcolumn=1)
operator = ["+","-"]
create_operators(operator,gridrow=1,gridcolumn=3,verticalcreate = True)
operator = ["%","0","."]
create_operators(operator,gridrow= 4,gridcolumn= 0,verticalcreate=False,firstleave=True)

clear()
equal()
sqrt_button()
numcreator()
animate_buttons()


root.mainloop()
# the most bloated sht i have written(dont know what the word mean)
# NEVER FUCKING USE 0TH COLUMN IN A LIST