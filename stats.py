def stats(fileName):
    f = open(fileName)
    total = f.read()
    print("Line count", total.count('\n'))
    print("Word count", len(total.split()))
    print("Character count", len(total))
stats('stats.py')
