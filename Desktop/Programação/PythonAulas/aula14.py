a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a, b, c)
formato1 = 'a={nomeA} b={nomeB} c={numero:.2f}'.format(nomeA=a, nomeB=b, numero=c)
print(formato)
print(formato1)