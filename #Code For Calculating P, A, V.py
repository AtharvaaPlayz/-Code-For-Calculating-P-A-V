#Code For Calculating P, A, V

MainQ = input("What do you want to find Options: Perimeter, Area, Volume: ")

if(MainQ == 'perimeter'):
    L = int(input("length: "))
    B = int(input("Breadth: "))
    Perimeter = (L + B) * 2
    print(Perimeter)
elif(MainQ == 'area'):
    L = int(input("length: "))
    B = int(input("Breadth: "))
    Area = L * B
    print(Area)
elif(MainQ == 'volume'):
    L = int(input("length: "))
    B = int(input("Breadth: "))
    H = int(input("height: "))
    Volume = L * B * H 
    print(Volume)