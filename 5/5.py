f =open('out.txt').read().split('\n')
f1 =[]
a =''
for i in range(len(f)):
	f1.append(f[i].split(' '))
for i in range(len(f1)):
	print ' '.join(f1[i])
