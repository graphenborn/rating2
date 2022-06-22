import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Вводим переменные
        id = "70174464"
        fio = "Серебряков Юрий Владимирович"
        y0 = 150
        x0 = 10
        header = tk.BooleanVar(False)
        colorName = tk.StringVar()
        colorName.set("blue")

        # Создаем фреймы
        colFrame = tk.Frame(self, borderwidth=1, relief=tk.GROOVE)
        colFrame.pack(side='right', anchor='n', fill='x', expand = 1, padx=10, pady=10)

        triFrame = tk.Frame(self)
        triFrame.pack(side='top', pady= (10, 0))

        x1y1Frame = tk.Frame(self)
        x1y1Frame.pack(side='left', anchor='s', expand=1, padx=10, pady=10)
        x2y2Frame = tk.Frame(self)
        x2y2Frame.pack(side='left', anchor='s', expand=1, padx=10, pady=10)
        x3y3Frame = tk.Frame(self)
        x3y3Frame.pack(side='left', anchor='s', expand=1, padx=10, pady=10)
        

        # Класс для создания кнопок
        class RBColor:
            def __init__(self, color):
                tk.Radiobutton(colFrame, text=color, variable=colorName, value=color, command=paint).pack(anchor='w')


        # Класс для создания полей ввода
        class TitEntry:
            def __init__(self, coord, framec, value):
                tk.Label(framec, text=coord).pack(anchor='w')
                self.coords = tk.StringVar()
                self.coords.set(value)
                self.coords.trace('w', inputPainting)
                self.entryEd = tk.Entry(framec, textvariable=self.coords, bd=3)
                self.entryEd.pack(expand=1)


        
        # Базовый заголовок
        self.title(fio)

        # Функция для смены заголовка
        def headerChange(event):
            header.set(not header.get())
            if (header.get() == False): self.title(fio)
            else: self.title(id)

        # Бинд смены заголовка по нажатию мыши
        self.bind('<Button-1>', headerChange)

        # Функция для рисования треугольника при задавании координат
        def inputPainting(a, b, c):
            for i in range (len(coordsList)):
                if coordsList[i].coords.get() != "":
                    startCoordsList[i] = coordsList[i].entryEd.get()
            canv.coords(rectangle, x0+int(startCoordsList[0]), y0-int(startCoordsList[1]),
                                    x0+int(startCoordsList[2]), y0-int(startCoordsList[3]), 
                                    x0+int(startCoordsList[4]), y0-int(startCoordsList[5]))

        # Создаем площадь для рисования фигур
        canv = tk.Canvas(triFrame, width=200, height=200)

        # Рисуем систему координат
        canv.create_line(15,160,15,10, width=2, arrow=tk.LAST, fill="red")
        canv.create_line(10,150,150,150, width=2, arrow=tk.LAST, fill="red")
        canv.create_text(20,170, text="(0; 0)", fill="red", font=("Helvectica", "10"))
        canv.create_text(25, 10, text="y", fill="red", font=("Helvectica", "10"))
        canv.create_text(150, 160, text="x", fill="red", font=("Helvectica", "10"))

        # Ищем координаты из ID
        x1 = int(id[2:4])
        x2 = int(id[4:6])
        x3 = int(id[6:8])
        yID = str(int(id)/3)
        y1 = int(yID[2:4])
        y2 = int(yID[4:6])
        y3 = int(yID[6:8])
        startCoordsList = [x1, y1, x2, y2, x3, y3]

        # Рисуем базовый треугольник
        rectangle = canv.create_polygon([x0+x1, y0-y1], [x0+x2, y0-y2], [x0+x3, y0-y3], fill=colorName.get())

        canv.pack()

        # Рисуем треугольник в зависимости от выбранного цвета
        def paint():
            canv.itemconfig(rectangle, fill=colorName.get())

        # Создаем кнопки
        RBColor('blue')
        RBColor('red')
        RBColor('green')
        RBColor('yellow')
        RBColor('orange')
        RBColor('pink')

        # Создаем поля
        x1Ed = TitEntry("x1:", x1y1Frame, x1)
        y1Ed = TitEntry("y1:", x1y1Frame, y1)
        x2Ed = TitEntry("x2:", x2y2Frame, x2)
        y2Ed = TitEntry("y2:", x2y2Frame, y2)
        x3Ed = TitEntry("x3:", x3y3Frame, x3)
        y3Ed = TitEntry("y3:", x3y3Frame, y3)
        coordsList = [x1Ed, y1Ed, x2Ed, y2Ed, x3Ed, y3Ed]

program = App()
program.mainloop()
