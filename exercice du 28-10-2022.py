
# exercicxe 11 & 12 

#  exercice 11

animaux = ['lapin', 'chat', 'chien', 'chiot', 'dragon', 'ornithoynque']
print(animaux)

for animal in animaux :
    print(animal)


# exercice 12
animaux1 = ['lapin', 'chat', 'chien', 'chiot', 'dragon', 'ornithoynque']
animaux2 = animaux1.copy()
print(animaux2)

animaux2.reverse()
print(animaux2)


#autre méthode possible : 
print(animaux[::-1])


for animal in reversed(animaux):
    print(animaux)


# exercice 13 à 15

#exercice 13 ordre alphabétique

animaux = ['lapin', 'chat', 'chien', 'chiot', 'dragon', 'ornithoynque']
animaux.sort()          # animauxtrié = sorted(animaux)     permet de trier la liste tout en conservant l'ordre de la liste d'origine
print (animaux)


# exercice 14

animaux = ['lapin', 'chat', 'chien', 'chiot', 'dragon', 'ornithoynque']
animaux.append('troll')
print(animaux)

dom = [] 
for i in range(0,4):
    dom.append(animaux.pop(0))

print(dom)
print(animaux)


"""
ce que j'ai essayé mais qui n'a pas marché... 

animauxdom = del animaux.pop(animaux[0:4])
print(animauxdom) 

--> ce qu'il aurait fallu faire : 

dom = animaux[0:4]
del animaux[0:4]
print(dom , animaux)


"""


# exercice 15

animaux = ['lapin', 'chat', 'chien', 'chiot', 'dragon', 'ornithoynque']
for animal in animaux:
    print(len(animal))


# exercice 16

fichier = open("C:\\StageCAP\\texte.txt", "r")
texte = fichier.read()
print(texte) 


# exercice 17 

temperature = ['chaud', 'froid', 'tempéré', 'glacial', 'brulant']

with open("temperature.txt", "w", encoding="UTF8") as fichier :
    for mot in temperature : 
        fichier.write(mot + "\n")           # "\n"  => retour à la ligne 
        print(mot)




# exercice 18

temperature = ['chaud', 'froid', 'tempéré', 'glacial', 'brûlant']
tempenglish = ['hot', 'cold', 'moderate', "icy", "ardent"]

with open("temperature2.txt", "w", encoding= "UTF8") as fichier:
    for mot, word in zip(temperature, tempenglish):
        fichier.write(mot + ":" + word + "\n")



