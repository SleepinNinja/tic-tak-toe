def display_board(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


def user_input():
    repeat_index_check = False
    global allowed_indices
    repeat_index = 0
    num = 0
    user_inp = "wrong"
    user_index = False
    accepted_indices = range(1,10)
    
    while user_inp.isnumeric() == False or user_index == False or repeat_index_check == False:
        user_inp = input("Enter the cell number :")
        
        if user_inp.isnumeric():
            if int(user_inp) in accepted_indices:
                user_index = True
                if int(user_inp) in allowed_indices:
                    num = int(user_inp)
                    for number in allowed_indices:
                        repeat_index = allowed_indices.index(num)
                        repeat_index_check = True
                    allowed_indices.pop(repeat_index)                
                else:
                    print("Entered cell number that is taken already")
                    
            else:
                print("Enter value does not match to any of the cell number")
        else:
            print("Entered number is not a digit !")
    
    return int(user_inp)



def user_choice():
    user_cho = ""
    
    while user_cho not in ["X","O"]:
        user_cho = input("Enter X or O :")
    
        if user_cho not in ["X","O"]:
            print("Please enter either X or O")
    
    return user_cho


def replace_values(lst1,lst2,lst3,index,updated_value):
    index_locator = 0

    if index in [1,2,3]:
        index_locator = index - 1
        lst1[index_locator] = updated_value
        return lst1

    elif index in [4,5,6]:
        index_locator = index - (2*2)
        lst2[index_locator] = updated_value
        return lst2

    elif index in [7,8,9]:
        index_locator = index - (2*3+1)
        lst3[index_locator] = updated_value
        return lst3

def win_lose(a1,a2,a3):
    stop = True
    if a1[0] == a2[0] == a3[0] == "X" or a1[1] == a2[1] == a3[1] == "X":
         print("X Won")
         stop = False
    elif a1[2] == a2[2] == a3[2] == "X" or a1[0] == a1[1] == a1[2] == "X":
         print("X Won")
         stop = False
    elif a2[0] == a2[1] == a2[2] == "X" or a3[0] == a3[1] == a3[2] == "X":
         print("X Won")
         stop = False
    elif a1[0] == a2[1] == a3[2] == "X" or a1[2] == a2[1] == a3[0] == "X":
         print("X Won")
         stop = False
    elif a1[0] == a2[0] == a3[0] == "O" or a1[1] == a2[1] == a3[1] == "O":
         print("O Won")
         stop = False
    elif a1[2] == a2[2] == a3[2] == "O" or a1[0] == a1[1] == a1[2] == "O":
         print("O Won")
         stop = False
    elif a2[0] == a2[1] == a2[2] == "O" or a3[0] == a3[1] == a3[2] == "O":
         print("O Won")
         stop = False
    elif a1[0] == a2[1] == a3[2] == "O" or a1[2] == a2[1] == a3[0] == "O":
         print("O Won")
         stop = False
    elif counter == 8:
         stop = False
    return stop
     


def check_game_on(still_on):
    global list1,list2,list3
    global counter
    global allowed_indices
    game_on_choice = ''
    play_ahead = True
    if counter < 9 and still_on == True:
        counter += 1
        if counter == 8 and still_on == False :
            print("Game Over")
            
    if still_on == False:
        print("Game over")
        print("\n")
        while game_on_choice not in ["Y","N"] :
            game_on_choice = input("Do you want to play again ? Y=yes, N=no :")
            if game_on_choice not in ["Y","N"]:
                print("Please enter Y or N")

        if game_on_choice == "N":
            play_ahead = False
            
        elif game_on_choice == "Y":
            play_ahead = True
            counter = 0
            allowed_indices = [1,2,3,4,5,6,7,8,9]
            list1 = [' ',' ',' ']
            list2 = [' ',' ',' ']
            list3 = [' ',' ',' ']
       
    return play_ahead 
            

print("The indices of the cells are as follows")
print(['1','2','3'])
print(['4','5','6'])
print(['7','8','9'])

list1 = [' ',' ',' ']
list2 = [' ',' ',' ']
list3 = [' ',' ',' ']
counter = 0
index = 0
character = ''
allowed_indices = list(range(1,10))
play_furht = True

while play_furht:
   # display_board(list1,list2,list3)
    cell = user_input()
    character = user_choice()
    if cell in [1,2,3]:
        list1 = replace_values(list1,list2,list3,cell,character)
    elif cell in [4,5,6]:
        list2 = replace_values(list1,list2,list3,cell,character)
    elif cell in [7,8,9]:
        list3 = replace_values(list1,list2,list3,cell,character)
    print("\n")
    print("\n ")
    display_board(list1,list2,list3)
    check_game_over = win_lose(list1,list2,list3)
    play_furht = check_game_on(check_game_over)
    
    
    

        

    
