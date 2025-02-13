# a=90
# print(type(a))

# a=-3 + 4 * 2
# print(a)

# print( max(1,7,4,3,9,2,0,))
# print( min(1,7,4,3,9,2,0,))

# print(int(23.345))
# print(float(1234.345))
# print(int('234') * 2)

# import turtle
# from turtle import *
# turtle.title("rainbow spiral")
# speed(100)
# bgcolor("black")
# r ,g, b = 255, 0,0
# for i in range (255*2):
#   colormode(255)
#   if i<255//3:
#     g+=3

#   elif i<255*2//3:
#     r-=3
#   elif i<255:
#     b+=3
#   elif i<255*4//3:
#     g-=3
#   elif i<255*5//3:
#     r+=3
#   else:
#     b-=3
#   fd(50+i)
#   rt(91)
# pencolor(r,g,b)
  


##############-------PROMODORO TIMER----------#################

# import time

# def countdown(minutes):
#     seconds = minutes * 60
#     while seconds > 0:
#         mins, secs = divmod(seconds, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         seconds -= 1
#     print("00:00", end="\r")

# def pomodoro_timer():
#     cycles = 4
#     work_duration = 25  # in minutes
#     short_break_duration = 5  # in minutes
#     long_break_duration = 30  # in minutes

#     for _ in range(cycles):
#         print("Work session started!")
#         countdown(work_duration)
#         print("Work session ended! Take a short break.")
#         time.sleep(1)  # to ensure "Work session ended!" is visible before the break

#         print("Short break started!")
#         countdown(short_break_duration)
#         print("Short break ended! Time to get back to work.")

#     print("Great job! You've completed 4 cycles. Take a long break.")
#     countdown(long_break_duration)
#     print("Long break ended. Ready to start another round?")

# if __name__ == "__main__":
#     pomodoro_timer()



