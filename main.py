import winsound, time

for i in range(1):

    winsound.PlaySound('C:/Users/User/Documents/GitHub/PomodoroApp/Pomodoro_Go.wav', winsound.SND_ALIAS)

    time.sleep(1500)
    winsound.PlaySound('C:/Users/User/Documents/GitHub/PomodoroApp/Pomodoro_Over.wav', winsound.SND_ALIAS)
    print ('Your 25 minute study period is over! Take a break, you earned it!')

    time.sleep(300)
    winsound.PlaySound('C:/Users/User/Documents/GitHub/PomodoroApp/Pomodoro_Go.wav', winsound.SND_ALIAS)
    print ('Your 25 minute break is over! Get back to work :)')


input()