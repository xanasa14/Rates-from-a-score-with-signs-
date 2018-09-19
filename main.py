
# (*)(*)(+)(-)(-)    so this is 50
#(*) means 20 
#(+) equals 10 
#(-) equans 0, none, zero, nada 
while True:
    try:
        lista = []
        refilling = True
        score = int(input("Please enter your score "))
        if score <= 100 and score>=0:
            a, b = divmod(score, 20)
            while (a!=0):
                lista.append("*")
                a-=1
            if b>5:
                lista.append("+")
        else:
            print ("the score has to be between zero and one hundred")
            refilling = False
        refill = 5 - len(lista)
        while (refill!=0) and (refilling):
            refill-=1
            lista.append("-")

        print (lista)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


