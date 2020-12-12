n = int(input())
name_numbers = [input().split() for contact in range(n)]
phone_book = {key: value for key, value in name_numbers}

while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break