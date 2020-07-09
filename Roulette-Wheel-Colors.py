
pocket_num = int(input("Please enter a pocket number: "))

if pocket_num < 0 or pocket_num > 36:
    print("enter a number in the range from 0 to 36")
else:
    if pocket_num == 0:
        print("The pocket is green")
    elif pocket_num < 11:
        if pocket_num % 2 != 0:
            print("The pocket is red")
        elif pocket_num %2 == 0:
            print("The pocket is black")
    elif pocket_num < 19:
        if pocket_num % 2 != 0:
            print("The pocket is black")
        elif poclet_num %2 == 0:
            print("The pocket is red")
    elif pocket_num < 29:
        if pocket_num % 2 != 0:
            print("The pocket is red")
        elif pocket_num % 2 == 0:
            print("The pocker is black")
    else:
        if pocket_num % 2 != 0:
            print("The pocket is black")
        elif pocket_num % 2 == 0:
            print("The pocker is red")
