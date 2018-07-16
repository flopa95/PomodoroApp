import winsound, time, tkinter

popup = tkinter.Tk()
popup.overrideredirect(1)
popup.attributes('-topmost', True)

screen_width = popup.winfo_screenwidth()
popup.geometry('15x15+%d+0' % (screen_width/2))

canvas = tkinter.Canvas(popup, width = 15, height = 15, background = "red",highlightthickness=0)

for i in range(1):

    canvas.configure(background = "red")
    canvas.pack()
    popup.update()
    winsound.PlaySound('C:/Users/User/Documents/GitHub/PomodoroApp/Pomodoro_Go.wav', winsound.SND_ALIAS)
    print ('Time to be productive! Seek discomfort.')

    time.sleep(1500)
    canvas.configure(background = "green")
    canvas.pack()
    popup.update()
    winsound.PlaySound('C:/Users/User/Documents/GitHub/PomodoroApp/Pomodoro_Over.wav', winsound.SND_ALIAS)
    print ('Your 25 minute study period is over! Take a break, you earned it!')

    time.sleep(300)
    


input()
popup.mainloop()
