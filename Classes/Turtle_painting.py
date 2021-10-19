# -*- coding: utf8 -*-
import turtle as turtle

text = 'помещение 4 forward 159 left 90 forward 181 Right 90 forward 1648 left 90' \
       ' forward 156 Right 90 forward 1420 Right 90 forward 144 left 90 forward 911' \
       ' оight 90 forward 1132 forward 1353 forward 1107 Right 90 forward 3972 Right 90' \
       ' forward 2602 left 90 forward 159 Right 90 forward 808'
turtle.pendown()
turtle.color("blue")  # Устанавливаем цвет черепашки

forwardlist = ['форвард', 'forward', 'форвард', 'fun Ward', 'forward ', 'форвардер', 'вперед', 'прямо']
rightlist = ['right', 'рейд']
leftlist = ['left', 'лифт', 'лофт', 'лет', 'лифта', 'левая', 'влево']
proemlisstart = ['начало проёма']
proemlistend = ['конец проёма', 'один конец проёма']
windowliststart = ['начало окна']
windowlistend = ['конец окна']
drawingstart = ['помещение']
celingheight = ['высота потолка', 'высота помещения']
doorheight = ['высота проёма']
windowheight = ['высота окна']
windowsillist = ['высота подоконника']

class TurtleDraw():
    def __init__(self,
                 measure: str = 'помещение 4 forward 159 left 90 forward 181 Right 90 forward 1648 left 90 forward 156 Right 90'
                                ' forward 1420 Right 90 forward 144 left 90 forward 911 right 90 forward 1132 forward 1353'
                                ' forward 1107 Right 90 forward 3972 Right 90 forward 2602 left 90 forward 159 Right 90 forward 808'):
        self.measure = measure

    def StartDrawing(self):
        print('Drawing Started')
        turtle.penup()
        turtle.goto(-350, 350)
        turtle.pendown()

    def Forward(self, x):
        n = 10
        turtle.pendown()
        turtle.forward(x / n)

    def Left(self, y):
        turtle.left(y)

    def Right(self, z):
        turtle.right(z)

    def FinishPainting(self):
        turtle.done()

    def Drawing(self):
        list_of_measures = {}
        big_list_of_measures = []
        list_of_measures = self.measure
        a = list_of_measures.split(' ')
        list_len = (len(a))  # Длина списка
        for n in range(0, list_len, 2):
            element = a[n:n + 2]
            big_list_of_measures.append(element)
        n = 0
        for elements in big_list_of_measures:
            n += 1
            word_to_look = (elements[0])
            if word_to_look.lower() in drawingstart:
                self.StartDrawing()
            elif word_to_look.lower() in forwardlist:
                val = int(elements[1])
                forwardvalue = (val)
                self.Forward(forwardvalue)

            elif word_to_look.lower() in leftlist:
                val2 = int(elements[1])
                self.Left(val2)
                print(f'turtle.left({val2})')
            elif word_to_look.lower() in rightlist:
                val3 = int(elements[1])
                self.Right(val3)
                print(f'turtle.right({val3})')
            else:
                # Пока так. Нужно добавить states с внесением новой команды в базу данных
                # и привязки к ней действия
                self.Right(90)
                continue



