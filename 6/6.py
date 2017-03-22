f =open('out.txt').read().split('\n')
f1=[]
for i in range(len(f)):
	for j in f[i].split(' ')[::-1]:
		print j[::-1],
	print
