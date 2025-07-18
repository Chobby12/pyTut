even_numbers = [2,4,6,8,10]
print(even_numbers)

new_even_numbers = [i for i in range(100) if i%2==0]
print(new_even_numbers)

def get_even_numbers(start, end):
    numbers = []
    msg = f'The even numbers from {start} to { end}'
    print(msg.upper())
    for i in range(start, end+1):
        print(i)
        if i%2!=0: 
            numbers.append(i)
    return numbers

print(get_even_numbers(100,400))


apt = 'on'

print(apt.upper())
# hue = []

# hue.append(2)
# hue.append(45)
# print(dir(hue))
# print(hue)