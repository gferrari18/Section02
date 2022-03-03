

def word(x):
    add = 0
    for y in x:
        if y.isnumeric():
            f = int(y)
            add = add + f
    return add

fas = input("nice: ")
print(word(fas))