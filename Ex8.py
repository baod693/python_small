num_start = int(input('Choose a number to start '))
num_end = int(input('Choose a number to end '))
print (f'Start from: {num_start}')
print (f'End on: {num_end}')

num = num_start
while num <= num_end:
    print (num)
    num += 1 