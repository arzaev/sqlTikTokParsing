with open('parsing.txt', 'r', encoding='utf-8') as f:
    file = f.read().split('\n')


count = 0
count_files = 1
list = []
for i in file:
    list.append(i)
    count += 1
    print(count)
    if count == 300:
        with open('parsing/{}'.format(str(count_files)), 'a', encoding='utf-8') as f:
            f.write("\n".join(list))
        count_files += 1
        list = []
        count = 0