#ex1
name='Ram'
plc="Ayodhya"
print("{} belongds to {}".format(name,plc))
#ex2
print(format(50,'b'))
print(format(-45,'b'))
#ex2
#new_line='\n'
print(f'{name} is boy \n He lives in {plc}')
#ex3
new="Welcome to {pname} \n Our famous food is {fname}".format(pname="Baripada",fname="Mangsa Mudhi")
print(new)
#ex4
w="Welcome {} to {} India".format("hello",20)
print(w)
#ex5
s='Welcome {1} to {0} India'.format('hello',20) #1&0 refer the format index
print(s)
#ex6
d='Welcome {a} to {b} India'.format(a='hello',b='my')
print(d)
#ex7
e='Welcome {b:^15} to {a:>10} India'.format(a='hello',b='my')    # <left
print(e)                                                         # >right  # ^middle




