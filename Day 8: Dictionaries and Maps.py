# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phonebook = {}
for i in range(n):
    stream = input()
    inpp = stream.split()
    phonebook[inpp[0]] = inpp[1]

'''
while True:
    query = input()
    if query in phonebook:
        print('{0}={1}'.format(query,phonebook[query]))
    else:
        print('Not found')
'''
while True:
    try:
        name = input()
        if name in phonebook:
            print('%s=%s' % (name, phonebook[name]))
        else:
            print('Not found')
    except:
        break
