side = int(input("Enter a number  : "))
i = 0
print(f'How big is the square? {side}') 

while(i < side):
    a = 0
    while(a < side):      
        a = a + 1
        print('*', end = ' ')
    i = i + 1
    print('')