# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



a = 1+52+\
    2 + 2

print (a)

#%%


print (18)
#%%
a = True

b = False

print (a,b)

#%%

print (1>2)
print (1<2)


#%%

print (int(False), bool (0))

#%%


a = 2
b = 3
c = 1.32e+20
print (a ,b,c )

#%%
a = 4
b = 4
print (a**b)
a = 2
#%%
a = 1.0e-11
b = 2.435e-13
from numpy import abs  

print (abs(a-b)<1.e-9)
#%%
a = 1+2j
b = 3+1j
#%%


print (float(1), float(True))
#%%
print (int(1.3), bool(-1.5), bool(0))
#%%
a = 'String1'
b = 'String2'
c = '''Very long string
multi-line string
Русскоязычная строка'''

# Comment
"""

Some descritpion
"""
print (a)
print(b, c)

#%%

print (len(a),len(b), len(c))
#%%



print (a, a[2:4], a[4])
#%%

print(c.replace("\n", " ").split(" "))
#%%



print ("\"line\" with quotes")

#%%


c[3] = 'a'
#%%

print (str(None)+str(1)+str(1.0), str(1+2j))



#%%

print (int("123")+2)

print (bool("True"))

#%%
# в питоне работает сборщик мусора
# если нет ссылок на куски кода, то он удаляется


# КОРТЭЖИ  - комбинация безымянных полей

#%%

a = (1, "Str", True, 2, 3, 4)
print (a, a[1])














































