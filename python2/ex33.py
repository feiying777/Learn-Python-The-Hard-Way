
numbers = []

def add_numbers(n):
    i = 0
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i

print "How many numbers do you want to add? "
n = int(raw_input("> "))

add_numbers(n)
        
print "The Numbers: "

for num in numbers:
    print  num