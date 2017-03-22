f=open('out.txt').read().split()
count =0
for i in range(len(f)):
    if(f[i].isalpha()==1):
        count +=1
        print f[i],
print
print "============================================="
print "count = "+str(count)
