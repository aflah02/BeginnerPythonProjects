def sing(n):
    if n == 1:
        objects = 'bottle'
        objects_minus_one = 'bottles'
    elif n == 2:
        objects = 'bottles'
        objects_minus_one = 'bottle'
    else:
        objects = 'bottles'
        objects_minus_one = 'bottles'

    if n > 0:
        print(str(n) + " " + objects + " of beer on the wall, " + str(n) + " " + objects + " of beer.")
        print("Take one down and pass it around, " + str(n-1) + " " + objects_minus_one + " of beer on the wall.")
        print(" ")
    elif n == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    else:
        print("Error: Wheres the booze?")
bottles = 99

while bottles >= 0:
    sing(bottles)
    bottles -= 1
