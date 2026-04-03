import random 
top_of_the_range = input("enter the number; ")
if top_of_the_range.isdigit():
    top_of_the_range = int(top_of_the_range)

    if top_of_the_range <= 0:
        print('please type a number next time.')
        quit()

    random_number = random.randint(0,top_of_the_range)
print(r)