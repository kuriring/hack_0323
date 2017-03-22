f =open('out.txt').read().split('\n')
for i in range(len(f)):
    print f[i].translate(None,"~!@#$%^&*()_+-=` ").swapcase()
