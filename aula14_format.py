a = 'A'
b = 'B'
c = 1.1
#string = 'a={} b={} c={:.2f}'
#string = 'b={1} a={0} c={2:.2f}'
#string = 'b={1} a={0} c={nome3:.2f}'
string = 'b={nome2} a={nome1} c={nome3:.2f}'
#formato = string.format(a, b, c)
#formato = string.format(a, b, nome3=c)
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)