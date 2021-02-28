from tkinter import *
import datetime


def showFrame(frame):
    frame.tkraise()


window = Tk()

# window.state("zoomed")              #to make full screen
window.geometry("400x400")
window.rowconfigure(0, weight=1)  # permission to show up on the window
window.columnconfigure(0, weight=1)


frame1 = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")
    frame.config(background="black")
###########==============Frame1==========###########
frame1Title = Label(frame1, justify=LEFT, text=r"""
           ______
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`""", fg="red", bg="black")

frame1Title.pack(fill="x")
frame1Button = Button(frame1, text="Türkçe", padx=82, pady=200,
                      command=lambda: showFrame(frame2), fg="red", bg="black")
frame1Button.pack(side=LEFT)
frame1Button2 = Button(frame1, text="English", padx=82, pady=200,
                       command=lambda: showFrame(frame3), fg="red", bg="black")
frame1Button2.pack(side=RIGHT)
###########==============Frame2==========###########

box1 = Entry(frame2, font=("MS Sans Serif", 14),
             bg="azure4", fg="red", justify=CENTER)
box1.place(x=100,
           y=200,
           width=200,
           height=57)


answer = Label(frame2, text=" ", bg="azure4", fg="red")
answer.pack(pady=20)


def calculations():
    year = datetime.date.today().year
    date = int(box1.get())
    left = 79 - (int(year) - int(date))  # average human lifespan is 79
    totalMonth = left * 12
    totalWeek = left * 52
    totalDay = left * 365
    totalHour = totalDay * 24

    try:
        if date < year-100 or date > year:
            answer.config(text="Geçerli bir yıl giriniz.")
        else:
            answer.config(
                text=f"{left} yıl / {totalMonth} ay / {totalWeek} hafta / {totalDay} gün / {totalHour} saat.")

    except ValueError:

        answer.config(text="Sayı olarak giriniz.")


frame2Title = Label(
    frame2, text="Ortalama insan ömrü 79 yıl olarak baz alınmıştır.", fg="red", bg="black")
frame2Title.pack(fill="x", pady=100)
frame2Button = Button(frame2, text="Enter", command=calculations,
                      padx=82, pady=200, fg="red", bg="black")
frame2Button.pack(side=BOTTOM)

###########==============Frame3==========###########
box2 = Entry(frame3, font=("MS Sans Serif", 14),
             bg="azure4", fg="red", justify=CENTER)
box2.place(x=100,
           y=200,
           width=200,
           height=57)


answer2 = Label(frame3, text=" ", bg="azure4", fg="red")
answer2.pack(pady=20)


def calculations2():
    year = datetime.date.today().year
    date = int(box2.get())
    left = 79 - (int(year) - int(date))  # average human lifespan is 79
    totalMonth = left * 12
    totalWeek = left * 52
    totalDay = left * 365
    totalHour = totalDay * 24

    try:

        if date < year-100 or date > year:
            answer2.config(text="Enter a valid year.")
        else:
            answer2.config(
                text=f"{left}years / {totalMonth}months / {totalWeek}weeks / {totalDay} days / {totalHour} hours.")

    except ValueError:

        answer2.config(text="Enter a valid year.")


frame3Title = Label(
    frame3, text="based on average human lifespan 79 years.", fg="red", bg="black")
frame3Title.pack(fill="x", pady=100)
frame3Button = Button(frame3, text="Enter", command=calculations2,
                      padx=82, pady=200, fg="red", bg="black")
frame3Button.pack(side=BOTTOM)


showFrame(frame1)

window.mainloop()
