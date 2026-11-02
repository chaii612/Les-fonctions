#Job 1
def my_print_hello():
    return ("Hello world!")

message = my_print_hello()
print(message)







#Job 2
def my_print_name(name):
    print (name)

my_print_name("John")
my_print_name("Jane")
my_print_name("Alice")
my_print_name("Bob")

#ou 
def my_print_name(name):
    return name

print(my_print_name("John"))
print(my_print_name("Jane"))
print(my_print_name("Alice"))
print(my_print_name("Bob"))







#Job 3
def add(a, b):
    return a + b

print("La somme est:", add(5, 10))
print("La somme est:", add(3, 15))
print("La somme est:", add(2, 8))


#ou 
def add(a, b):
    print("La somme est:", a + b)

add(5, 10)
add(3, 15)
add(2, 8)





#Job 4
def gethello():
    return("Hello la Plateforme")

print(gethello())






#Job 5
def calcule(num1,operator,num2):
    num1=int(num1)
    operator=str(operator)
    num2=int(num2)  

    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        if num2 == 0 :
            return ("Division par 0 impossible")
        else :
            return num1/num2
    elif operator=="%":
        return num1%num2
    else:
        return "Opérateur non valide"

print(calcule(2,"/",5))












#Job 6
def n(nombre):
    if nombre>0:
        print(f"Le {nombre} est positif")
    else:
        print(f"Le {nombre} est négatif")

n(5)
n(7)
n(0)
n(-5)

#ou 
def n(nombre):
    if nombre>0:
        return(f"Le {nombre} est positif")
    else:
        return(f"Le {nombre} est négatif")

print(n(5))
print(n(7))
print(n(0))
print(n(-5))








#Job 7
def l(langage):
    langage=str(langage)

    if langage=="javascrip":
        print("Tu es un développeur web")
    elif langage=="python":
        print("Tu es un développeur IA")
    elif langage=="java":
        print("Tu es un développeur logiciel")
    elif langage=="reactjs":
        print("Tu es un développeur mobile")
    else :
        print("Un jour, je serai le meilleur développeur...")

l("java")












#Job 8
def jsp(type,saison):
    type=str(type)
    saison=str(saison)

    if type=="fruits" and saison=="hiver":
        print("orange, mandarine et kiwi")
    elif type=="fruits" and saison=="été":
        print("Poire, fraise, cassis")
    elif type=="légume" and saison=="hiver":
        print("carrote, topinambour, endive")
    elif type=="légume" and saison=="été":
        print("artichaud, aubergine, navet")

jsp("fruits","hiver")
jsp("fruits","été")
jsp("légume","hiver")
jsp("légume","été")













#Job 9
def moyenne(note1,note2,note3):
    moyenne_etudiant = (note1+note2+note3)/3
    print(moyenne_etudiant)

    if moyenne_etudiant>=15:
        return("Très bon élève")
    elif 11<=moyenne_etudiant<=14:  
        return("Bon élève")
    elif 8<=moyenne_etudiant<=10:
        return("Elève moyen")
    elif 0<=moyenne_etudiant<=7:
        return("Elève devant faire des éfforts")

note1 = float(input("Saissir la 1er note :"))
note2 = float(input("Saissir la 2eme note :"))
note3 = float(input("Saissir la 3eme note :"))

apreciation= moyenne(note1,note2,note3)
print(apreciation)












#Job 10
def pimp(nombre):
    if nombre<0 or not isinstance(nombre, int):
        print("veillez entrez un nombre entier positif")
    elif nombre % 2 == 0 :
        print(f"le nombre {nombre} est pair")
    else :
        print(f"le nombre {nombre} est impair")

pimp(1)
pimp(126)
pimp(0)
pimp(-56)
pimp(1.5)
pimp(2584963215478)
pimp(0.2)












#Job 11
def time_to_text(nombre):
    heure_virgule = nombre / 60
    heure = int(heure_virgule)
    minute = round((heure_virgule - heure)*60)
    return(f"{heure} heures et {minute} minutes")

print(time_to_text(nombre=500))








#Pour aller plus loin
def inverse(nom):
    nom_invers = nom[::-1]
    print(nom_invers)

inverse("chaima")
inverse("bouchra")
inverse("123456789")
