d ={
    'a':"1",
    'b':'2',
    'c':'3'
}

aa = list(enumerate(d.items()))
a, (b, c) = aa[0]
print(a, b, c)