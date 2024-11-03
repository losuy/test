import requests
import time
from pathlib import Path
import yt_dlp 
import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog
import threading


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")
        self.title("PyLoader")
        self.resizable(0,0)
        
        '''Initializing the widget'''
        self.Main_frame=self.main_frame()
        self.entry_frame = self.Entry_frame()
        self.message_frame = self.Message_frame()
        self.button_frame=self.Button_frame()
        self.radio_frame = self.Radio_frame()
        self.link = tk.StringVar(value='')
        self.welcome_message = tk.StringVar(value='Welcome to PyLoader')
        self.error_message = tk.StringVar(value='')
        self.val = tk.IntVar(value=0)
        self.filepath = tk.StringVar()
        self.download = self.Download_button()
        self.error = self.Error_label() 
        self.frame_placement()
        self.button()
        self.radio()
        self.entry()
        self.directory()
        self.Welcome_label()
        self.thread = None
        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.__initialize_window()
        


    def main_frame(self):
        # Here we set the the frame where GUI will be created
        mframe = tk.Frame(self,bg="#ffe184",width=500,height=400)
        mframe.grid()
        return mframe
    
    def Entry_frame(self):
    #    This is the frame for taking link and specifying folder
       return tk.Frame(self,bg="#c6e2ff",width=500,height=100)
    
    def Message_frame(self):
    #    This is the frame for Displaying Error message
       return tk.Frame(self,bg="#c6e2ff",width=500,height=100)

    def Button_frame(self):
    #    Frame for download and Exit button
       return tk.Frame(self,bg="#dbfc00",width=500,height=30)
       
    
    def Radio_frame(self):
    #    This frame is for Audio and Video option
       return tk.Frame(self,bg="#171714",width=500,height=30)
    
    def entry(self):
        # Now we get to creating The Entry widget
        self.entry_frame.rowconfigure(0,weight=1)
        self.entry_frame.rowconfigure(1,weight=1)
        # Used ttk instead of standard tk due to its sleek design
        label=ttk.Label(self.entry_frame,text="Link:",style="C.TLabel")
        entry=ttk.Entry(self.entry_frame,textvariable=self.link,width=40,style="C.TEntry")
        ttk.Style().configure("C.TLabel",font=("Helvetica", 16))
        label.grid(column=0,row=0,sticky="nsew",pady=10,ipadx=10)
        entry.grid(column=1,row=0,columnspan=2,sticky="nsew",pady=10)
        

    def frame_placement(self):
        self.message_frame.place(relx=0.5,rely=0.2,anchor="center")
        self.entry_frame.place(relx=0.5,rely=0.5,anchor="center")
        self.radio_frame.place(relx=0.5,rely=0.7,anchor="center")
        self.button_frame.place(relx=0.5,rely=0.8,anchor="center")
        return None

    def directory(self):
        label=ttk.Label(self.entry_frame,text="Directory:",style="C.TLabel")
        entry=ttk.Entry(self.entry_frame,textvariable=self.filepath,width=40,style="TEntry")
        label.grid(column=0,row=1,sticky="nsew",pady=10,ipadx=10)
        entry.grid(column=1,row=1,columnspan=1,sticky="nsew",pady=10,ipady=4)
        ttk.Style().configure("C.TEntry")
        ttk.Button(self.entry_frame,text="...",command =self.get_directory).grid(column=3,row=1,
        sticky="nsew",padx=10,pady=10)
        
    def radio(self):
        self.radio_frame.columnconfigure(0, weight=1)
        self.radio_frame.columnconfigure(1, weight=1)
        # Creating The Video option
        ttk.Style().configure("C.TRadiobutton",font=("Helvetica", 16))
        button1=ttk.Radiobutton(self.radio_frame,text = "Video",
                       value=0,variable=self.val,style="C.TRadiobutton").grid(column=0,row=0,sticky="nsew",
                        padx=10)
        # Creating The Video option
        button2=ttk.Radiobutton(self.radio_frame,text = "Audio",
                       value=1,variable=self.val,style="C.TRadiobutton").grid(column=1,row=0,sticky="nsew",
                          padx=10)

    def Error_label(self):
        error =  ttk.Label(self.message_frame,text=self.error_message.get(),style="C.TLabel")
        return error

    def Welcome_label(self):
        self.message_frame.rowconfigure(0,weight=1)
        self.message_frame.rowconfigure(1,weight=1)

        self.error.grid(column=0,row=1)
        welcome = ttk.Label(self.message_frame,text=self.welcome_message.get(),style="C.TLabel")
        welcome.grid(column=0,row=0,pady=10)
        ttk.Style().configure("C.TLabel",font=("Helvetica", 16),background="#c6e2ff")


    def Download_button(self):
        '''How download works is it uses a seperate thread to call the function
            begin download'''
        ttk.Style().configure("C.Tbutton",padding =[20,10,20,10])
        ttk.Style().map("C.TButton",
        foreground=[('pressed', 'red'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'yellow')])
        return ttk.Button(self.button_frame,text="Download",
            command=lambda: threading.Thread(target=self.begindownload,daemon=True).start(),
            style="C.TButton")
    
    def button(self):
        return self.download.grid(column=1,row=0,sticky="nsew",ipadx=10,ipady=10)
        

    def get_directory(self):
        '''Using a tkinter function filedialog.askdirectory to ask for
            directory where we want to put downloaded file'''
        folder_name = filedialog.askdirectory(
            initialdir=Path.home() / 'Downloads',title="Dialog box")
        self.filepath.set(folder_name)

    def Error_update(self):
        self.error.configure(text=self.error_message.get())
        return

    def Reset_label(self):
        self.error_message.set("")
        self.error.configure(text=self.error_message.get())
        return 

    def link_detect(self):
        if self.link.get() != '':
            return True
        else:
            return False
        
    def exception_handle(self,start_time=time.time(),connection_time=30):
        try:
            request = requests.get(self.link.get())
            if request.status_code == 200:
                return True
            else:
                self.error_message.set("Link is not available")
                self.download.state(['disabled'])
                self.after(1000,func=self.after_click)
                self.after(1,func=self.Error_update)
                self.after(1500,func=self.Reset_label)
                return False
        except requests.exceptions.MissingSchema as exception:
            self.error_message.set("Invalid Input Provided")
            self.download.state(['disabled'])
            self.after(1000,func=self.after_click)
            self.after(1,func=self.Error_update)
            self.after(1500,func=self.Reset_label)
            return False 
        except requests.exceptions.ConnectionError as exception:
            self.error_message.set("Please check your Internet Connection")
            self.download.state(['disabled'])
            self.after(1000,func=self.after_click)
            self.after(1,func=self.Error_update)
            self.after(1500,func=self.Reset_label)
            return False
            
                
            

    def begindownload(self):
        # create an instance of Downloader Class for file to be downloaded(Class specified below)
        if self.link_detect():
            if self.exception_handle():        
                self.download.state(['disabled'])
                self.error_message.set("Downloading")
                self.after(1,self.Error_update)
                self.thread = threading.Thread(target=Downloader(self.link.get(),self.val.get(),
                    self.filepath.get()).downloaded(),daemon=True)
                self.error_message.set("Done")
                self.after(1,func=self.Error_update)
                self.after(1000,func=self.Reset_label)
                self.after(2,func=self.after_click)
                self.thread.start()
                self.thread.join()
   
                return True
        else:
            self.error_message.set("Please provide a link")
            self.download.state(['disabled'])
            self.after(1000,func=self.after_click)
            self.after(1,func=self.Error_update)
            # After 1000 millisecond change button state back
            self.after(1500,func=self.Reset_label)
            return False
        
    def after_click(self):
        # this will change the download button state to enabled
        return self.download.state(['!disabled'])
        
               
    def on_exit(self):
        # exit function called upon self.protocl
        if tk.messagebox.askyesno("Exit", "Do you want to quit the application?"):
            self.destroy()


    def __initialize_window(self):
        # a function to run the mainloop
        return self.mainloop()

class Downloader():
    '''Downloader Class takes 3 options, link,option(audio,video) and the folder'''
    def __init__(self,link,option,folder):
        self.link = link
        self.option = option
        self.folder = folder

    def downloaded(self):
        '''option is insitially set to 0 denoting Video as the standard Download
            option 1 is audio download'''
        if(self.option == 0):
            self.download_video()
        else:
            self.download_audio()

    def download_video(self):
        '''takes he link and folder and creates an instance of yt-dlp class wih the given option
            finally starts downloading video'''
        ytb_opt={'format':'besvideo/best','outtmpl':f'{self.folder}''/%(title)s.%(ext)s',
                 'ignoreerrors':False}
        with yt_dlp.YoutubeDL(ytb_opt) as ytb:
            ytb.download(self.link)

    
    def download_audio(self):
        '''takes he link and folder and creates an instance of yt-dlp class wih the given option
            finally starts downloading audio'''
        ytb_opt={'extract_audio':True,'format':'bestaudio/best',
                 'outtmpl':f'{self.folder}''/%(title)s.%(ext)s','ignoreerrors':False}
        with yt_dlp.YoutubeDL(ytb_opt) as ytb:
            ytb.download(self.link)

#  A cancel function was meant to be implemented which will abort the current operation(downloading)
# This will enable you to download another file without while cancelling the pevious download process
# Sadly i was not able to implement it as it was too complex and above my skill level
# Will certainly look into this in the future
# Any advice is most welcome


if __name__=="__main__":
    GUI()
     