'''
           <--- Zoo Manager --->

    <---- Minimum PY Version [3.10.1] ---->

        <--- Created By JesusKian --->

        <--- Click On Link 👇👇 --->
          https://zil.ink/jesuskian
          https://zil.ink/jesuskian
          https://zil.ink/jesuskian
          https://zil.ink/jesuskian
'''



#                            <-------------------------- libraries -------------------------->

from os import system
from time import sleep, time

#                              <-------------------------- Funcs -------------------------->

def ValueError_error():
    system("cls")
    print("""
            \t\t    [-- Value Error --]
            \t\t --> Only Enter INT Number
            \t\t --> Don't Enter FLOAT Number
            \t\t --> Don't Enter Any Character
            \t\t --> Don't Enter Any Sentence
            """)
    return sleep(5)

def KeyboardInterrupt_error():
    system("cls")
    print("""
            \t\t            [-- Keyboard Error --]
            \t\t --> Please Don't Push Any Key On Your Keyboard
            """)
    return sleep(5)

def Invalied_error():
    system("cls")
    print("""
            \t\t    [-- Invalied Error --]
            \t\t [-- Please Contact Support --]
            """)
    return sleep(5)

def timer():
    sleep(3)
    system("cls")
    for i in range(4,0,-1):
        print(f"[🆗] Please Wait For {i} Second . . .")
        sleep(1)
        system("cls")
    system("cls")
    return 0
#                              <-------------------------- Vars -------------------------->

main_menu = 0
delete_animal_code = 0
animal_counter = 0
e_m = 0
animal_show = 0
get_admin_user = ' '
get_admin_password = ' '
y_n = ' '
animal_name = []
a_n = ' '
animal_skin_color = []
a_s_c = ' '
animal_weigh = []
a_w = 0
animal_gender = []
a_g = ' '
g_t = 0
random_code = []
r_c = 1

#      <------------------------------------------------------ Code ------------------------------------------------------>

#                              <-------------------------- Main Menu -------------------------->

while True:
    system("cls")
    print(f"\t\tAnimals in Zoo : {animal_show}")
    print("""
        
        1[🍺] Add Animal\t2[🍺] Delete Animal

        3[🍺] Edit Animal\t4[🍺] Show All Animals [❗Only Zoo Keeper❗]

                        0[🍺] EXIT
        """)

    try:
        main_menu = int(input("\n\t\t>>>"))

    except ValueError:
        print(ValueError_error())
        print(timer())

    except KeyboardInterrupt:
        print(KeyboardInterrupt_error())
        print(timer())

    except:
        print(Invalied_error())
        print(timer())

    else:
        system("cls")
        match main_menu:

#                              <-------------------------- Add Animal -------------------------->

            case 1:
                system("cls")
                print("[🥤] Enter Your Animal Name :")
                a_n = str(input("\n\t\t>>>"))
                animal_name.append(a_n)

                system("cls")
                print("[🥤] Enter Your Animal Skin Color :")
                a_s_c = str(input("\n\t\t>>>"))
                animal_skin_color.append(a_s_c)

                system("cls")
                print("[🥤] Enter Your Animal Weight :")
                try:
                    a_w = float(input("\n\t\t>>>"))

                except ValueError:
                    print(ValueError_error())
                    print(timer())

                except:
                    print(Invalied_error())
                    print(timer())

                else:
                    animal_weigh.append(a_w)


                    system("cls")
                    print("[🥤] Enter Your Animal Gender :")
                    a_g = str(input("\n\t\t>>>"))
                    animal_gender.append(a_g)
                
                    system("cls")
                    print(f"Your Code Is --> {r_c*2}")
                    random_code.append(r_c*2)
                    print(timer())

                    r_c+=1
                    animal_counter+=1
                    animal_show+=1

#                              <-------------------------- Delete Animal -------------------------->

            case 2:
                system("cls")
                try:
                    print("""
                        \t\t   - Delete Animal Menu -
                        [💥] Enter Your Animal Code :
                        """)
                    delete_animal_code = int(input("\n\t\t>>>"))

                except ValueError:
                    print(ValueError_error())
                    print(timer())

                except:
                    print(Invalied_error())
                    print(timer())

                else:
                    for i in range(0,animal_counter):

                        if random_code[i] == delete_animal_code:
                            animal_name[i] = None
                            animal_skin_color[i] = None
                            animal_weigh[i] = None
                            animal_gender[i] = None
                            animal_show-=1

                            print(timer())
                            break

                    else:
                        print("""
                            \t\t[-- Invalied Code --]
                            """)
                        print(timer())

#                              <-------------------------- Edit Animal -------------------------->

            case 3:
                try:
                    system("cls")
                    print("""
                        \t\t- Edit Animal Menu -

                        1[🎭] Animal Name\t\t2[🎭] Animal Skin Color
                        3[🎭] Animal Weight\t\t4[🎭] Animal Gender

                                   0[🎭] Exit Edit Menu
                        """)
                    e_m = int(input("Which Option Do U Want?"))

                except ValueError:
                    print(ValueError_error())
                    print(timer())

                except:
                    print(Invalied_error())
                    print(timer())

                else:

                    try:
                        system("cls")
                        delete_animal_code = int(input("\n\t\tEnter Your Animal Code :\n\n\t\t>>>"))

                    except ValueError:
                        print(ValueError_error())
                        print(timer())

                    except:
                        print(Invalied_error())
                        print(timer())

                    else:

                        if delete_animal_code in random_code:
                            match e_m:

                                case 1:
                                    for i in range(0,animal_counter):

                                        if random_code[i] == delete_animal_code:
                                            system("cls")
                                            a_n = str(input("[🧩] Enter Your New Animal Name\n\t\t>>>"))
                                            animal_name[i] = a_n
                                            print(timer())
                                            break

                                case 2:
                                    for i in range(0,animal_counter):
    
                                        if random_code[i] == delete_animal_code:
                                            system("cls")
                                            a_s_c = str(input("[🧩] Enter Your New Animal Skin Color\n\t\t>>>"))
                                            animal_skin_color[i] = a_s_c
                                            print(timer())
                                            break

                                case 3:
                                    for i in range(0,animal_counter):
    
                                        if random_code[i] == delete_animal_code:
                                            system("cls")
                                            a_w = int(input("[🧩] Enter Your New Animal Weight\n\t\t>>>"))
                                            animal_weigh[i] = a_w
                                            print(timer())
                                            break

                                case 4:
                                    for i in range(0,animal_counter):

                                        if random_code[i] == delete_animal_code:
                                            system("cls")
                                            a_g = str(input("[🧩] Enter Your New Animal Gender\n\t\t>>>"))
                                            animal_gender[i] = a_g
                                            print(timer())
                                            break

                                case 0:
                                    print(timer())
                                    break

                                case _:
                                    system("cls")
                                    print("""
                                        \t\t     [-- Invalied Option --]
                                        \t\t --> Only Select Number From 0 to 4
                                        """)
                                    print(timer())
                        else:
                            system("cls")
                            print("""
                                \t\t[-- Invalied Code --]
                                """)   
                            print(timer())

#                       <-------------------------- Show All Animal -------------------------->

            case 4:
                system("cls")
                get_admin_user = str(input("[💎] UserName\n\t\t>>>"))

                system("cls")
                get_admin_password = str(input("[💎] Password\n\t\t>>>"))

                if(get_admin_user=='JesusKian') and (get_admin_password=='8569'):
                    system("cls")

                    for i in range(6,0):
                        print("Welcome Boss !\ni will show list of zoo in\n\t\t{i}")
                        sleep(1)
                        system("cls")

                    for j in range(0,animal_counter):

                        if animal_name[j]==None and animal_skin_color[j]==None and animal_weigh[j]==None and animal_gender[j]==None:
                            print(f"""
                                <++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>
                                🧨<-----Animal Number {j} :
                                🎠>>> None !!!
                                """)
                            sleep(5)

                        else:
                            print(f"""
                                <++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>
                                🧨<----- Animal Number {j} :
                                🎠>>> Animal Name --> {animal_name[j]}
                                🎠>>> Animal Skin Color --> {animal_skin_color[j]}
                                🎠>>> Animal Weigh --> {animal_weigh[j]}
                                🎠>>> Animal Gender --> {animal_gender[j]}
                                """)
                            sleep(5)
                    else:
                        system("cls")
                        print("""
                            \t\t            [-- No Animal --]
                            \t\t[-- First Add Animal Then Come & See List --]
                            """)
                        print(timer())

                else:
                    system("cls")
                    print("UserName OR Password Is Wrong !!!")
                    print(timer())

            case 0:
                system("cls")
                for i in range(6,0,-1):
                    print(f"""
                        \t\t[😶] App Will Close In {i} . . .
                        """)
                    sleep(1)
                    system("cls")
                exit()

            case _:
                system("cls")
                print("""
                    \t\t     [-- Invalied Option --]
                    \t\t --> Only Select Number From 0 to 4
                    """)
                print(timer())