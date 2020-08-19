# Enter your code here. Read input from STDIN. Print output to STDOUT
amount = int(input())

for num in range(0, amount):
    word = input()
    even = ''
    odd = ''
    for position in range(0, len(word)):
        if position % 2 == 0:
            even = even + word[position]
        else:
            odd = odd + word[position]

    print(even, odd)