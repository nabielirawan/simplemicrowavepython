from tkinter import *

root = Tk()
sec = [i for i in range(60001)]
jalan = True

e = Entry(root, width = 20, borderwidth = 5)
e.grid (row=0, column = 0, columnspan = 3, padx = 0, pady = 0)
main = e.get()

def display(display):
    global main
    e.delete(0, END)
    e.insert(0, int(str(main) + str(display)))

def click(mode):
    global jalan
    jalan = True
    if mode == "ayam":
        root.after(1000, moda, mode)
    elif mode == "ikan":
        root.after(1000, moda, mode)
    elif mode == "roti":
        root.after(1000, moda, mode)
    elif mode == "burger":
        root.after(1000, moda, mode)
    elif mode == "pizza":
        root.after(1000, moda, mode)
    elif mode == "popcorn":
        root.after(1000, moda, mode)
    elif mode == "cook":
        root.after(1000, moda, mode)
    elif mode == "reheat":
        root.after(1000, moda, mode)

def moda(argument):
    if argument == "ayam":
        e.delete(0, END)
        e.insert(0, "MODE: AYAM")
        root.after(2000, suhu, argument)
    elif argument == "ikan":
        e.delete(0, END)
        e.insert(0, "MODE: IKAN")
        root.after(2000, suhu, argument)
    elif argument == "roti":
        e.delete(0, END)
        e.insert(0, "MODE: ROTI")
        root.after(2000, suhu, argument)
    elif argument == "burger":
        e.delete(0, END)
        e.insert(0, "MODE: BURGER")
        root.after(2000, suhu, argument)
    elif argument == "pizza":
        e.delete(0, END)
        e.insert(0, "MODE: PIZZA")
        root.after(2000, suhu, argument)
    elif argument == "popcorn":
        e.delete(0, END)
        e.insert(0, "MODE: POPCORN")
        root.after(2000, suhu, argument)
    elif argument == "cook":
        e.delete(0, END)
        e.insert(0, "MODE: COOK")
        root.after(2000, suhu, argument)
    elif argument == "reheat":
        e.delete(0, END)
        e.insert(0, "MODE: REHEAT")
        root.after(2000, suhu, argument)

def suhu(argument):
    if argument == "ayam":
        e.delete(0, END)
        e.insert(0, "SUHU: 180 C")
        root.after(2000, waktu, argument)
    elif argument == "ikan":
        e.delete(0, END)
        e.insert(0, "SUHU: 90 C")
        root.after(2000, waktu, argument)
    elif argument == "roti":
        e.delete(0, END)
        e.insert(0, "SUHU: 300 C")
        root.after(2000, waktu, argument)
    elif argument == "burger":
        e.delete(0, END)
        e.insert(0, "SUHU: 60 C")
        root.after(2000, waktu, argument)
    elif argument == "pizza":
        e.delete(0, END)
        e.insert(0, "SUHU: 300 C")
        root.after(2000, waktu, argument)
    elif argument == "popcorn":
        e.delete(0, END)
        e.insert(0, "SUHU: 300 C")
        root.after(2000, waktu, argument)
    elif argument == "cook":
        e.delete(0, END)
        e.insert(0, "SUHU: 600 C")
        root.after(2000, waktu, argument)
    elif argument == "reheat":
        e.delete(0, END)
        e.insert(0, "SUHU: 180 C")
        root.after(2000, waktu, argument)

def waktu(argument):
    if argument == "ayam":
        e.delete(0, END)
        e.insert(0, "WAKTU : 150 S")
        root.after(1000, timer, 150)
    elif argument == "ikan":
        e.delete(0, END)
        e.insert(0, "WAKTU : 90 S")
        root.after(1000, timer, sec[90])
    elif argument == "roti":
        e.delete(0, END)
        e.insert(0, "WAKTU : 300 S")
        root.after(1000, timer, sec[300])
    elif argument == "burger":
        e.delete(0, END)
        e.insert(0, "WAKTU : 180 S")
        root.after(1000, timer, sec[180])
    elif argument == "pizza":
        e.delete(0, END)
        e.insert(0, "WAKTU : 100 S")
        root.after(1000, timer, sec[100])
    elif argument == "popcorn":
        e.delete(0, END)
        e.insert(0, "WAKTU : 150 S")
        root.after(1000, timer, sec[150])
    elif argument == "cook":
        e.delete(0, END)
        e.insert(0, "WAKTU : 180 S")
        root.after(1000, timer, sec[180])
    elif argument == "reheat":
        e.delete(0, END)
        e.insert(0, "WAKTU : 80 S")
        root.after(1000, timer, sec[80])


def start(waktu):
    global jalan
    jalan = True
    detik = sec[int(waktu)]
    if detik >= 0 and jalan == True:
        root.after(1000, timer, detik)
        jalan = True
    elif detik < 0 or jalan == False :
        e.delete(0, END)
        e.insert(0, "DONE")

def clear(waktu):
    main = e.get()
    e.delete(0, END)

def timer(display):
    global jalan
    if jalan == True:
        e.delete(0, END)
        e.insert(0, display-1)
        jalan = True
        if display > 0:
            display -= 1
            start(display)
        else:
            e.delete(0, END)
            e.insert(0, "DONE")
    else:
        e.delete(0, END)
        value = 0
        e.insert(0, "DONE")

def stop():
    global jalan
    e.delete(0, END)
    e.insert(0, "DONE")
    jalan = False

def clear(waktu):
    main = e.get()
    e.delete(0, END)


tombolayam = Button(root, padx = 20, pady = 20, text = "Ayam", command = lambda: click("ayam"), fg = "black", bg = "white")
tombolikan = Button(root, padx = 23, pady = 20, text = "Ikan", command = lambda: click("ikan"), bg = "black")
tombolroti = Button(root, padx = 23, pady = 20, text = "Roti", command = lambda: click("roti"), bg = "black")
tombolburger = Button(root, padx = 17, pady = 20, text = "Burger", command = lambda: click("burger"), bg = "black")
tombolpizza = Button(root, padx = 19, pady = 20, text = "Pizza", command = lambda: click("pizza"), bg = "black")
tombolpopcorn = Button(root, padx = 10, pady = 20, text = "Popcorn", command = lambda: click("popcorn"), bg = "black")
tombolcook = Button(root, padx = 21, pady = 20, text = "Cook", command = lambda: click("cook"), bg = "black")
tombolreheat = Button(root, padx = 13, pady = 20, text = "Reheat", command = lambda: click("reheat"), bg = "black")
tombolstart = Button(root, padx = 22, pady = 20, text = "Start", command = lambda: start(e.get()), bg = "black")
tombolstop = Button(root, padx = 20, pady = 20, text = "Stop", command = stop, bg = "black")
tombolclear = Button(root, padx = 19, pady = 20, text = "Clear", command = lambda: clear(e.get()), bg = "black")
displaymanual = Button(root, padx = 13, pady = 12, text = "Manual\n200 C", command = "", bg = "black")
tombol1 = Button(root, padx = 30, pady = 20, text = "1", command = lambda: display(1), bg = "black")
tombol2 = Button(root, padx = 30, pady = 20, text = "2", command = lambda: display(2), bg = "black")
tombol3 = Button(root, padx = 30, pady = 20, text = "3", command = lambda: display(3), bg = "black")
tombol4 = Button(root, padx = 30, pady = 20, text = "4", command = lambda: display(4), bg = "black")
tombol5 = Button(root, padx = 30, pady = 20, text = "5", command = lambda: display(5), bg = "black")
tombol6 = Button(root, padx = 30, pady = 20, text = "6", command = lambda: display(6), bg = "black")
tombol7 = Button(root, padx = 30, pady = 20, text = "7", command = lambda: display(7), bg = "black")
tombol8 = Button(root, padx = 30, pady = 20, text = "8", command = lambda: display(8), bg = "black")
tombol9 = Button(root, padx = 30, pady = 20, text = "9", command = lambda: display(9), bg = "black")
tombol0 = Button(root, padx = 30, pady = 20, text = "0", command = lambda: display(0), bg = "black")

tombolayam.grid(row = 1, column = 0)
tombolikan.grid(row = 1, column = 1)
tombolroti.grid(row = 1, column = 2)
tombolburger.grid(row = 2, column = 0)
tombolpizza.grid(row = 2, column = 1)
tombolpopcorn.grid(row = 2, column = 2)
tombolcook.grid(row = 3, column = 0)
tombolreheat.grid(row = 3, column = 2)
tombolstart.grid(row = 8, column = 0)
tombolstop.grid(row = 8, column = 1)
tombolclear.grid(row = 8, column = 2)
displaymanual.grid(row = 3, column = 1)
tombol0.grid(row = 7, column = 1)
tombol1.grid(row = 6, column = 0)
tombol2.grid(row = 6, column = 1)
tombol3.grid(row = 6, column = 2)
tombol4.grid(row = 5, column = 0)
tombol5.grid(row = 5, column = 1)
tombol6.grid(row = 5, column = 2)
tombol7.grid(row = 4, column = 0)
tombol8.grid(row = 4, column = 1)
tombol9.grid(row = 4, column = 2)

root.mainloop()
