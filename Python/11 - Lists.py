if __name__ == '__main__':
    N = int(input())

    elements = []

    for _ in range(N):
        command = input().split(' ')

        if 'append' in command:
            elements.append(int(command[1]))
        elif 'insert' in command:
            elements.insert(int(command[1]), int(command[2]))
        elif 'pop' in command:
            elements.pop()
        elif 'print' in command:
            print(elements)
        elif 'remove' in command:
            elements.remove(int(command[1]))
        elif 'reverse' in command:
            elements.reverse()
        elif 'sort' in command:
            elements.sort()