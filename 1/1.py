f = open("out.txt").read()
a = f.split('\n')[::-1]
print '\n'.join(a)
