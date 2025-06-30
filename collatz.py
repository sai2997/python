print("Name:A sai ganesh")
print("USN: 1AY24AI001")
print("Section: M")
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence
number = 6
print(collatz_sequence(number))
