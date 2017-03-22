f =open('out.txt').read().split('\n')
f1 =[]
for i in range(len(f)):
	f1.append(f[i].split(' '))
print f1
