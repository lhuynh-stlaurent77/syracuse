#On appelle n le nombre entier entré, t le temps de vol et a l'altitude de vol.

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
    print(t, a)
    print(u)
    return u

def syraplot(n):
    matplotlib.pyplot.plot(syra(n),"ro")
    matplotlib.pyplot.show()

n=int(input('Entrez un nombre entier naturel : '))
syra(n)
syraplot(n)
    
