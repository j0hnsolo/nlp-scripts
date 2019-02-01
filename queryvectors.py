f1 = open('keyfile.txt', 'r')
f2 = open('vectorfile.txt', 'r')
f3 = open('output.csv', 'a')

for word in f1.readlines():
    for line in f2.readlines():
        if line != '\n' and word.strip() == line.strip().split()[0]:
            f3.write(line)
    f2.seek(0)

f1.close()
f2.close()
f3.close()