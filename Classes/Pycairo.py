import cairo
import math

WIDTH = 30
HEIGHT = 25
PIXEL_SCALE = 100
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                             WIDTH * PIXEL_SCALE,
                             HEIGHT * PIXEL_SCALE)
ctx = cairo.Context(surface)
ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

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

text = 'помещение 4 forward 159 left 90 forward 181 right 90 forward 1648 left 90' \
       ' forward 156 right 90 forward 1420 right 90 forward 144 left 90 forward 911' \
       ' right 90 forward 3592 right 90 forward 3972 right 90' \
       ' forward 2602 left 90 forward 159 right 90 forward 808'

list_of_lenth = [1.59 / 2, 1.81 / 2, 16.48 / 2, 1.56 / 2, 14.20 / 2, 1.44 / 2, 9.11 / 2, 35.92 / 2, 39.72 / 2,
                 26.02 / 2, 1.59 / 2, 8.08 / 2]
list_of_angels = [0, -90, 90, -90, 90, 90, -90, 90, 90, 90, -90, 90]


class PycairoPaint():

    def __init__(self,
                 measure: str,
                 curent_x: int = 5, curent_y: int = 5, scale: int = 200, lengh: int = 0, index: int = 0, angel: int = 0,
                 path: str = 'plan_final'):
        self.measure = measure  # Вводная информация
        self.curent_x = curent_x  # Текущие координаты по x
        self.curent_y = curent_y  # Текущие координаты по y
        self.scale = scale  # масштаб на который делится расстояние
        self.angel = angel
        self.lengh = lengh  # длина отрезка
        self.start_x = 1
        self.start_y = 1
        self.index = index
        self.path = path

    def StartDrawing(self):

        WIDTH = 50
        HEIGHT = 35
        PIXEL_SCALE = 100
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                                     WIDTH * PIXEL_SCALE,
                                     HEIGHT * PIXEL_SCALE)
        ctx = cairo.Context(surface)
        ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

        ctx.rectangle(0, 0, WIDTH, HEIGHT)
        ctx.set_source_rgb(1, 1, 1)
        ctx.fill()

    def radians(self):
        return math.radians(self.angel)

    def Forwardlist(self):
        big_list_of_measures = []
        forwardValuesList = []
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
                val = elements[1]
                forwardValuesList.append(val)

        # print (forwardValuesList)
        # print(f'len forwardValuesList {len(forwardValuesList)}')
        return forwardValuesList

    def CurentAngel(self):

        def List_of_angels():

            rightlist = ['right', 'рейд', 'Right']
            leftlist = ['left', 'лифт', 'лофт', 'лет', 'лифта', 'левая', 'влево']

            big_list_of_measures = []
            list_of_add_angels = [0]
            list_of_measures = self.measure
            a = list_of_measures.split(' ')
            list_len = (len(a))  # Длина списка
            for n in range(0, list_len, 2):
                element = a[n:n + 2]
                big_list_of_measures.append(element)
            n = 0
            # print (big_list_of_measures)
            for elements in big_list_of_measures:
                n += 1
                word_to_look = (elements[0])

                if word_to_look.lower() in leftlist:
                    val = int(elements[1])
                    self.Resize_minus(val)
                    list_of_add_angels.append(self.angel)

                elif word_to_look.lower() in rightlist:
                    val2 = int(elements[1])
                    self.Resize_plus(val2)
                    list_of_add_angels.append(self.angel)

            return list_of_add_angels

        a = List_of_angels()
        # print(a)
        self.angel = 0
        return (a)

    def Calc_x(self):
        fwdlst = self.Forwardlist()
        carentang = self.CurentAngel()
        return self.curent_x + (float(fwdlst[self.index]) / float(self.scale)) * math.cos(
            math.radians(float(carentang[self.index])))

    def Calc_y(self):
        # Достать словарик с длиной:
        fwdlst = self.Forwardlist()
        carentang = self.CurentAngel()
        return self.curent_y + (float(fwdlst[self.index]) / float(self.scale)) * math.sin(
            math.radians(float(carentang[self.index])))

    def Drawing(self):
        big_list_of_measures = []
        forwardValuesList = []
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
                val = elements[1]
                forwardValuesList.append(val)
        self.StartDrawing()
        len_FVL = len(forwardValuesList)
        # print (f'len of forwards:{len_FVL}')
        # print(f'forward_list:{forwardValuesList}')
        counter = 0
        final_coords_dict = {}
        for values in range(0, len_FVL):
            # ctx.move_to(self.curent_x, self.curent_y)
            # ctx.line_to(self.Calc_x(), self.Calc_y())
            self.index = counter
            self.lengh = forwardValuesList[self.index]
            self.curent_x = self.Calc_x()
            self.curent_y = self.Calc_y()
            final_coords_dict[counter] = [self.curent_x, self.curent_y]
            counter += 1
            # print(final_coords_dict)
            # print (final_coords_dict[0][0])
            ctx.move_to(5, 5)
            ctx.line_to(float(final_coords_dict[0][0]), float(final_coords_dict[0][1]))  # 1 линия
            ctx.move_to(float(final_coords_dict[0][0]), float(final_coords_dict[0][1]))
            for i in range(1, (len(final_coords_dict))): #+1
                ctx.line_to(float(final_coords_dict[i][0]), float(final_coords_dict[i][1]))  # 1 линия
                ctx.move_to(float(final_coords_dict[i][0]), float(final_coords_dict[i][1]))
    def FinishDrawing(self):

        try:
            ctx.set_source_rgb(1, 0, 0)  # задается цвет линии
            ctx.set_line_width(0.1)  # задается толщина линии
            ctx.stroke()  # Команда "рисовать"
            surface.write_to_png(f'/home/pi/Scripts/aiogram-dogbot/PHOTO/{self.path}.png')  # Сохранение в файл
        except Exception as e:
            print(e)

    def Resize_minus(self, val):
        self.angel -= val

    def Resize_plus(self, val):
        self.angel += val

#todo потестировать как следует