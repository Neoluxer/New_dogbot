# -*- coding: utf8 -*-
import psycopg2
import transliterate
import os
import pickle5 as pickle


class Dog():

    def __init__(self, name="Дружок", breed="Дворняга", weight=7, age=1):
        self.name = name
        self.breed = breed
        self.weight = weight
        self.age = age

    def latinica(self):
        words_list = []
        latin_name = (transliterate.translit(self.name, reversed=True))
        bin_path = f'{latin_name.lower()}'
        word = self.name
        words = word.split()
        print(type(words))
        for items in words:
            words_list.append(items)
        if (len(words_list)) >= 2:
            bin_path1 = f'{words_list[0]}_{words_list[1]}'
            bin_path2 = bin_path1.lower()
            bin_path = f'{(transliterate.translit(bin_path2, reversed=True))}'
            return bin_path
        else:
            pass
        return bin_path


# def Dictionary_from_directory(path):
#     global last_picture
#     conn = psycopg2.connect(dbname='dogs', user='postgres',
#                             password='IlonMask@Python', host='localhost')
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM dogs')  # Каталог из которого будем брать файлы
#     directory = '/home/pi/Scripts/aiogram-dogbot/BIN/'
#     directory = path
#     conn.commit()
#     print(conn.encoding)
#     conn.set_client_encoding('UTF8')
#     # with open(r'E:\PycharmProjects\tmp\dog_book.bin', 'rb') as f:
#
#     # Получаем список файлов в переменную files
#     files = os.listdir(directory)
#     images = filter(lambda x: x.endswith('.bin'), files)
#     path2 = "/home/pi/Scripts/aiogram-dogbot/BIN/"
#     Path_list = []
#     Names_list = []
#     List_of_path = []
#
#     # extension = '.bin'
#     for d in images:
#         # print(d)
#         Path_list.append(d)
#
#     print(Path_list)
#     sch = 1
#     for items in Path_list:
#         n = items[0:-4]
#         picture_path = f'PHOTO\\{n}\\'
#         picture_url = f'https://www.neoluxe.ru/photo/{n}/'
#         files_pictures = os.listdir(picture_path)
#         print(files_pictures)
#         dog_images = filter(lambda x: x.endswith('.JPG'), files_pictures)
#
#         for d in dog_images:
#             print(f'{type(d)},{d}')
#             List_of_path.append(d)
#
#             last_picture = List_of_path[-1]
#         full_path_of_image = f'{picture_path}{last_picture}'
#         full_url_of_image = f'{picture_url}{last_picture}'
#         way = path2 + n + '.bin'
#         with open(way, 'rb') as f:
#             loaded_data = pickle.load(f)
#             new_name_Capitalise = loaded_data.name.title
#             print(
#                 f'{sch}). \nИмя: "{new_name_Capitalise()}"\nПорода: {loaded_data.breed}\nВес: {loaded_data.weight} кг.\nДата рождения: {loaded_data.age}')
#             cursor.execute('INSERT INTO dogs VALUES (%s, %s, %s, %s,default ,%s,%s,%s)',
#                            (new_name_Capitalise(), loaded_data.breed, loaded_data.weight, loaded_data.age, n,
#                             full_path_of_image, full_url_of_image))
#
#             print('')
#             sch += 1
#             Names_list.append(new_name_Capitalise())
#             conn.commit()
#     return Names_list


# Dictionary_from_directory('/home/pi/Scripts/aiogram-dogbot/BIN/')
# new_dog = Dog(name='Вова Кандалов', breed='человек', weight=82, age=42)
# print(new_dog.latinica())
