import tkinter as tk
#Christian Marquardt
win = tk.Tk()
frame = tk.Canvas(win, width = "500", height = "500", bg="green")
win.geometry("500x500")
frame.pack()
win.title("Dice Roller")
win.mainloop

def Eyes():
    wonkeyEye = [270, 200, 320, 250] #coordinates for eye change
    if(frame.coords(eye2) == wonkeyEye):
        frame.coords(eye2, 300, 180, 250, 230) #Normal Eye
        
    else:
        frame.coords(eye2, wonkeyEye) #Wonkey Coords
        
def Mouth():
    if(frame.coords(smileT) == frame.coords(smileB)): #mouth movement
        frame.coords(smileB, 230, 320, 260, 320)
        frame.coords(smileL, 230, 320, 210, 300)
        frame.coords(smileR, 280, 300, 260, 320)
    else: 
        frame.coords(smileL, frame.coords(smileT)) #regular mouth
        frame.coords(smileB, frame.coords(smileT))
        frame.coords(smileR, frame.coords(smileT))
          
def close_window(): #To leave program
    win.destroy()
#Button for eyes
b = tk.Button(win, text ="Eyes", highlightbackground="black", highlightcolor="black", highlightthickness=1, command= Eyes)
b.place(relx=.4, rely=.9, anchor="c")
#Button for mouth
c = tk.Button(win, text ="Mouth", highlightbackground="black", highlightcolor="black", highlightthickness=1, command= Mouth)
c.place(relx=.6, rely=.9, anchor="c")
#Button for exit
d = tk.Button(win, text ="Quit", highlightbackground="black", highlightcolor="black", highlightthickness=1, command= close_window)
d.place(relx=.5, rely=.1, anchor="c")
#The Left eye
eye1 = frame.create_oval(180, 180, 230, 230, width=2)
#The Right eye
eye2 = frame.create_oval(300, 180, 250, 230, width=2)
#The head
head = frame.create_oval(140, 140, 350, 350, width=2)
#Top, Bottom, Left, Right for the mouth
smileT= frame.create_line(210, 300, 280, 300, width=2)
smileB= frame.create_line(210, 300, 280, 300, width=2)
smileL= frame.create_line(210, 300, 280, 300, width=2)
smileR= frame.create_line(210, 300, 280, 300, width=2)
