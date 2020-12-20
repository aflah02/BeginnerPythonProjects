k = int(input("How many sets do you want to check?"))
for i in range(k):
    ls = list(map(int, input("Enter the 3 side lengths separated by spaces").split()))
    lar = max(ls)
    sma = min(ls)
    ls2 = ls.copy()
    ls2.remove(lar)
    ls2.remove(sma)
    if pow(ls2[0], 2) + pow(sma, 2) == pow(lar, 2):
        print("The triangle is a Pythagorean Triple")
    else:
        print("The triangle is not a Pythagorean Triple")
