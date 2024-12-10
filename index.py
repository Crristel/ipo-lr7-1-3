import json
def num1(read_file):
    for i in read_file:
            for key, value in i.items():
                if key =='id':
                    print(f"Номер записи:{value}".center(36,"~"))
                elif key=='name':
                    print(f"Название рыбы:{value}")
               
                elif key=='latin_name':
                    print(f"Латинское название рыбы:{value}")
                elif key=='is_salt_water_fish':
                    # если value равно true, то присваиваем ему значение "да"
                    if value==True: 
                        value="да"
                    else:
                        value="нет"
                    print(f"Является ли рыба пресноводной:{value}")
                elif key=='sub_type_count':
                    print(f"Количество подвидов рыб:{value}")
                    print()
    return 1
   
def num2(read_file):

    user_id=int(input("Введите поле записи,которую необходимо вывести:"))
    find=False
    for i in read_file:
        if i['id'] == user_id:
            for key, value  in i.items(): 
                if key =='id':
                    print(f"Номер записи:{value}".center(36,"~"))
                        
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
                    return 1
    if not find:
        print()
        print("Запись не найдена!")
        print()
    return 0
        
def num3(read_file):
            with open("fish.json", "r", encoding="utf-8") as file:
                read_file = json.load(file)
            id=0
            if read_file:
                id = max(item.get('id', 0) for item in read_file) + 1 
            else:
                id=1
            
            user_name=input("Введите название рыбы:")
            user_Lname=input("Введите латинское название рыбы:")
            user_is_saltFish=input("Введите является ли рыба пресноводной:")
            if user_is_saltFish.lower() =='да':
                user_is_saltFish=True
            else:
                user_is_saltFish=False
            while True: #цикл для проверки введено ли число в пременную user_sub
                user_sub = input("Введите количество подвидов рыб: ")
                if user_sub.isdigit():
                    user_sub = int(user_sub)
                    break
                else:
                    print("Это должно быть число!")
                    return 0

#создаём из полученных данных множество 
            new_fish={"id": id, "name":user_name, 
               "latin_name": user_Lname,
               "is_salt_water_fish":user_is_saltFish,
               "sub_type_count":user_sub
               }
         #добавляем к наши загруженным данным множество new_fish
            read_file.append(new_fish)
            with open("fish.json", 'w', encoding='utf-8') as out_file:
                json.dump(read_file, out_file,ensure_ascii=False,indent=2)
                print("Рыба успешно добавлена!")
                return 1
            
def num4(read_file):
    user_remove = int(input("Введите номер для удаления: "))
    find=False
    for i in read_file:
        if i['id'] == user_remove:
            read_file.remove(i)
            with open("fish.json", "w",encoding="UTF-8") as new_file:
                json.dump(read_file, new_file, ensure_ascii = False, indent=4)
                find=True
                print("Рыба успешно удалена!")
                return 1
    if not find:
        print()
        print("Запись не найдена!")
        print()
    return 0

def main():
    operation_count = 0
    with open("fish.json", "r", encoding="utf-8") as file:
        read_file = json.load(file)
    while True:
        while True:
            print("Меню".center(24,"~"))
            print("1) Вывести все записи","2) Вывести запись по полю", "3) Добавить запись", "4) Удалить запись по полю","5) Выйти из программы",sep = "\n")
            user_number=input("Для выбора введите номер пункта:")#если введённое с клавиатуры число равно 1, то выполняем первый пункт 
            if user_number.isdigit():
                user_number= int(user_number)
                break
            else:
                print("Это должно быть число!")
    
        if user_number == 1:
            operation_count+=num1(read_file)
            
        elif user_number==2:
            operation_count+=num2(read_file)

        elif user_number==3:
            operation_count+=num3(read_file)

        elif user_number==4:
            operation_count+=num4(read_file)

        elif user_number == 5:
            print(f"Количество выполненных операций:",operation_count)
            exit()
        else:
            print("ERROR! please try again!")
main()
