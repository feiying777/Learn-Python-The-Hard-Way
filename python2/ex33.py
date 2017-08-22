
numbers = []

def add_numbers(n, step):
    """ add numbers from 0 to n, increments by step """
    i = 0
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i

print "Now we will add numbers to a list, starts at 0"
print "Enter the max number you want to add in the list "
n = int(raw_input("> "))

print "How much you want the numbers increments by?"
step = int(raw_input("> "))
add_numbers(n, step)
        
print "The Numbers: "

for num in numbers:
    print  num