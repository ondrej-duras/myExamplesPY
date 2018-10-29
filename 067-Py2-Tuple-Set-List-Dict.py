#!/usr/bin/env python2

# Tuple -alebo N-tica - konstantne pole, jeho prvky menit nemozno
# ... teda :-) ak je prvkom pole, 
# tak pole vymenit za ine nemozno, ovsem obsah pola modifikovat mozno
# i co do poctu prvkov
print "-------- Tuple - N-tica -----------"
my_Tuple = ("Jano","Fero",10,[1,2,3],{"a":10,"b":20})
print my_Tuple
my_Tuple[3][0]=4
print my_Tuple
try:
  my_Typle[2]=20
except:
  print "Ved som vravel, ze Tuple nezmenis ! :-)"


# Set -alebo Mnozina - pole prvkov, ktore sa nemozu opakovat
# ... teda inymi slovami sa kazda hodnota moze v mnozine
# vyskytnut najviac jeden krat.
# Pozor! Mnozina je pole NETRIEDENE.
# Preto prehladavanie prvkov moze prebiehat v nepredvidatelnom poradi
# ...asi B-stromy :-)

print "-------- Set - Mnozina ------------"
# stary zapis mnoziny
my_Set=set([1,1,2,3,4,4,4,4])
print my_Set
# novy zapis mnoziny
my_Set = {1,1,2,3,4,4}
print my_Set
my_Set.add(5)
print my_Set
my_Set.remove(3)
print my_Set


# List -alebo zoznam, alebo tiez pole - pole prvkov, ktore je mozne lubovolne menit
# prvkami pola moze byt vsetko mozne
print "-------- List - Pole/Zoznam -------"
my_List = [1,2,3,"Jano","Fero",[4,5,6],{"a":"Adam","b":"Bozena"},lambda x: str(x)+" "+str(raw_input("Meno:"))]
print my_List
print my_List[7]("ahoj")
my_List.append("cau")
print my_List
my_List.pop(8)
print my_List
my_List.remove("Jano")
print my_List
my_List[4] = "Palo"  # index musi byt v existujucom rozsahu !
my_List.insert(3,"Peter")
print my_List


# Dictionary -alebo slovnik, alebo tiez associativne pole, teda perlovsky hash
# je pole usporiadanych dvojic kluc:hodnota, pricom zoznam klucov je mnozina,
# teda kazdy kluc sa v slovniku moze vyskytovat najviac raz
print "-- Dictionary - Slovnik/Hash ------"
my_Dict = {"a":"Adam","b":1,2:3,"c":lambda x: x+5,"z":[1,2,3,4]}
print my_Dict
print my_Dict["a"]
my_Dict["a"]="Fero"
print my_Dict
print my_Dict["c"](10) # volanie funkcie
my_Dict["nove"]='Nieco nove'
print my_Dict
my_Dict.pop("nove")
print my_Dict


print "-----------------------------------"
# List ako argument 
# - premenlivy pocet argumentov
# - argumenty volane odkazom
def fcia1(*x):
  print x[0]

# Dictionary ako argument
# - pomenovane a volitelne parametre
def fcia2(**x):
  a=x["jano"]
  print a

fcia1(10)
fcia2(jano="Ahoj")

# --- end ---

