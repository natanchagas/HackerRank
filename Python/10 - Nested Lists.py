if __name__ == '__main__':
    
    scores = {}

    for _ in range(int(input())):
        name = input()
        score = float(input())

        scores[name] = score

    scores_list = [ scores[name] for name in scores ]

    for times in range(scores_list.count(min(scores_list))):
        scores_list.remove(min(scores_list))

    names = [ name for name in scores if scores[name] == min(scores_list) ]

    names.sort()

    [print(name) for name in names]