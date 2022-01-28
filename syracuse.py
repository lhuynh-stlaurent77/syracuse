#!/usr/bin/env python
# coding: utf-8

# # Programme Syracuse
# Lucas H.
# Killian K.

# In[9]:


#On appelle n le nombre entier entre, t le temps de vol et a l'altitude de vol.

from matplotlib.pyplot import *

def syra(n):
    a=0
    t=0
    u=[n,]
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        u.append(n)
        t=t+1
        if a<n:
            a=n
    print("le temps de vol est de",t)
    print("L'altitude est de",a)
    print(u)
    return u

def syraplot(n):
    matplotlib.pyplot.plot(syra(n),"ro")
    matplotlib.pyplot.show()

n=int(input('Entrez un nombre entier naturel different de zero : '))
syraplot(n)


# In[ ]:




