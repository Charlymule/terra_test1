# exercice 1


# option 1
def somme (*args) : 
    s = 0
    for arg in args :
        s = s + arg

    return s
# print(somme)
print(somme(1,8,69,78))


# option 2
def somme(*args):
    return sum(args)

print(somme(3,5,9,8,7,5,54))



#exercice 2

def somme(a, b, c):
    return a + b +c

data = (5, 10, 7)
print(somme (*data))


# exercice 3

# a
def unDico(**kwargs):
    print(kwargs)
unDico(name = 'Christel', age = 33 )
unDico(name = 'Christel', age = 33, ville = 'Rouen', etude = 'ingé')

# b
dico = {'ville': 'Paris', 'age': 30, 'prenom': 'Harry'}
unDico(**dico)

# exercice 4 

# ce que j'ai fais mais ça donne pas ce qu'il faut
liste = [n for n in range(5) if n == (n + 3)]
print (liste)
# correction 
liste = [n + 3  for n in range(6)]
print (liste)

# exercice 5 
liste = [n for n in range(5) if n >= 2]
print (liste)

# exercice 6
alpha = "abc"
delta = "de"
liste = [lettre + ltr for lettre in alpha for ltr in delta]
print (liste) 

# exercice 7 
liste = sum([n for n in range(10)])
print (liste)



