# ## Задание 3

# Написать программу которая:

# - При запуске выводит меню из которого человек выбирает следующие пункты (*по средствам ввода номера пункта*):
#     - Вывести все записи
#     - Вывести запись по полю
#     - Добавить запись
#     - Удалить запись по полю
#     - Выйти из программы
# - После выполнения пунктов меню (*кроме “выйти из программы”*) меню отображается снова
# - Все записи хранятся в виде `.json` файла (*любое название*)
# - Пункт “**Вывести все записи**” — выводит в форматированном виде все записи из файла
# - Пункт “**Вывести запись по полю**” — выводит одну запись по определённому полю (*поле `id`*), а так же ее позицию в словаре.
# - Пункт “**Добавить запись**” — запрашивает у пользователя нужные данные и добавляет запись в файл
# - Пункт “**Удалить запись по полю**” — удаляет запись из файла по определенному полю  (*поле `id`*)
# - Пункт “**Выйти из программы**” — завершает выполнение программы, но перед этим вводит на экран количество выполненных операций с записями
# - Пункты “**Вывести запись по полю**” и “**Удалить запись по полю**” должны выводить предупреждение если нужная запись не найдена
# - Использовать функции запрещено
# - Перед сдачей задание файл должен хранить 5 подготовленных записей

# ### Вариант 1

# Программа должна хранить записи о рыбах

# Структура записи:

# - `id` — номер записи
# - `name` — общее название рыбы
# - `latin_name` — латинское (научное) название рыбы
# - `is_salt_water_fish` — хранить булевый тип данных, указывает на то является ли рыба пресноводной.
# - `sub_type_count` — хранить количество подвидов рыбы (число, можно придумать самим)
import json 
with open("fish.json","r", encoding="utf-8") as file:
    read_file = json.load(file)
user_number=0
while(user_number<5):
 print("~~~~~~~~~~Меню~~~~~~~~~~~")
 print("1) Вывести все записи","2) Вывести запись по полю", "3) Добавить запись", "4) Удалить запись по полю","5) Выйти из программы",sep = "\n")
 
 user_number=int(input("Для выбора введите номер пункта:"))

 if user_number==1:
    for i in read_file:
      for key, value in i.items():
             if key =='id':
                 print(f"~~~~~~~~~~Номер записи:{value}~~~~~~~~~~~~")
             elif key=='name':
                 print(f"Название рыбы:{value}")
               
             elif key=='latin_name':
                 print(f"Латинское название рыбы:{value}")
             elif key=='is_salt_water_fish':
                 if value==True:
                     value="да"
                 else:
                     value="нет"
                 print(f"Является ли рыба пресноводной:{value}")
             elif key=='sub_type_count':
                 print(f"Количество подвидов рыб:{value}")
                 print()
 if user_number==2:
    user_id=int(input("Введите поле записи,которую необходимо вывести:"))
    find=False
    for i in read_file:
         for key, value  in i.items(): 
             if value == user_id:
                for key, value  in i.items(): 
                    if key =='id':
                       print(f"~~~~~~~~~~Номер записи:{value}~~~~~~~~~~~~")
                    elif key=='name':
                       print(f"Название рыбы:{value}")
                    elif key=='latin_name':
                        print(f"Латинское название рыбы:{value}")
                    elif key=='is_salt_water_fish':
                           if value==True:
                             value="да"
                           else:
                             value="нет"
                           print(f"Является ли рыба пресноводной:{value}")
                    elif key=='sub_type_count':
                      print(f"Количество подвидов рыб:{value}")
                      print()
                      find=True
    if not find:
        print("Запись не найдена!")

 if user_number==3:
         user=input("Введите номер рыбы:")
         user_name=input("Введите название рыбы:")
         user_Lname=input("Введите латинское название рыбы:")
         user_is_saltFish=input("Введите является ли рыба пресноводной:")
         if user_is_saltFish.lower() =='да':
            user_is_saltFish=True
         else:
          user_is_saltFish=False
         user_sub=input("Введите количество подвидов рыб")



         new_fish={"id": user, "name":user_name, 
               "latin_name": user_Lname,
               "is_salt_water_fish":user_is_saltFish,
               "sub_type_count":user_sub
               }
         read_file.append(new_fish)

         with open("fish.json","a") as f:
           json.dump(new_fish,f,ensure_ascii=False,indent=2)

 if user_number==4:
     user_remove=input("Введитие номер записи,котрую нужно удалить:")
     for i in read_file:
         for key, value  in i.items(): 
             if key =='id' and value == user_remove:
                 read_file.remove(key,value)