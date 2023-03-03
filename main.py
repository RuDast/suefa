from tkinter import Tk, Label, Button, PhotoImage
from random import choice

win = Tk()
win.geometry("500x330")
win.title("Камень, ножницы, бумага")


def Restart() -> None:
    lbl_4.place_forget()
    lbl_5.place_forget()
    btn_restart.place_forget()
    lbl_result.place_forget()
    img_4.place_forget()
    img_5.place_forget()

    lbl_1.place(x=50, y=80)
    lbl_2.place(x=185, y=80)
    lbl_3.place(x=350, y=80)

    lbl_title.config(text="Выберите:")
    lbl_title.place(x=190, y=30)

    btn_1.place(x=70, y=150)
    btn_2.place(x=215, y=150)
    btn_3.place(x=370, y=150)


def Play(number: int, image: PhotoImage) -> None:
    array = choice([[1, image_1], [2, image_2], [3, image_3]])
    choiced = array[0]
    if number == choiced:
        result = "Ничья"
    elif (choiced == 1 and number == 2) \
            or (choiced == 2 and number == 3) \
            or (choiced == 3 and number == 1):
        result = "Вы проиграли"
    else:
        result = "Вы выиграли"

    ResultPrint(result, image, array[1])


def ResultPrint(result: str, image_4: PhotoImage, image_5: PhotoImage) -> None:
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()

    lbl_1.place_forget()
    lbl_2.place_forget()
    lbl_3.place_forget()

    lbl_title.config(text="Результат:")

    lbl_4.place(x=50, y=80)
    lbl_5.place(x=250, y=80)

    global img_4, img_5
    img_4 = Label(win, image=image_4)
    img_4.place(x=75, y=120)
    img_5 = Label(win, image=image_5)
    img_5.place(x=310, y=120)
    global lbl_result
    lbl_result = Label(win,
                       width=20,
                       justify="center",
                       text=result,
                       font=("Arial", 28))

    lbl_result.place(x=35, y=200)

    btn_restart.place(x=160, y=250)


def Start() -> None:
    btn_start.place_forget()
    img_1.place_forget()
    img_2.place_forget()
    img_3.place_forget()

    lbl_1.place(x=50, y=80)
    lbl_2.place(x=185, y=80)
    lbl_3.place(x=350, y=80)

    lbl_title.config(text="Выберите:")
    lbl_title.place(x=190, y=30)

    btn_1.place(x=70, y=150)
    btn_2.place(x=215, y=150)
    btn_3.place(x=370, y=150)


image_1 = PhotoImage(file="img's\\2.png")
image_2 = PhotoImage(file="img's\\1.png")
image_3 = PhotoImage(file="img's\\3.png")

img_1 = Label(win, image=image_1)
img_2 = Label(win, image=image_2)
img_3 = Label(win, image=image_3)

btn_start = Button(win,
                   text="Начать игру",
                   font=("Arial", 20),
                   command=Start)

lbl_title = Label(win,
                  text="Камень, ножницы, бумага",
                  font=("Arial", 18))

lbl_1 = Label(win,
              text="Камень",
              font=("Arial", 24))
lbl_2 = Label(win,
              text="Ножницы",
              font=("Arial", 24))
lbl_3 = Label(win,
              text="Бумага",
              font=("Arial", 24))

lbl_4 = Label(win,
              text="Ваш выбор:",
              font=("Arial", 16))
lbl_5 = Label(win,
              text="Выбор противника:",
              font=("Arial", 16))

btn_1 = Button(win,
               image=image_1,
               command=lambda: Play(1, image_1))
btn_2 = Button(win,
               image=image_2,
               command=lambda: Play(2, image_2))
btn_3 = Button(win,
               image=image_3,
               command=lambda: Play(3, image_3))

btn_restart = Button(win,
                     text="Играть снова",
                     font=("Arial", 20),
                     command=Restart)

lbl_title.place(x=100, y=30)
btn_start.place(x=160, y=200)

img_1.place(x=110, y=70)
img_2.place(x=210, y=70)
img_3.place(x=320, y=70)

win.mainloop()
