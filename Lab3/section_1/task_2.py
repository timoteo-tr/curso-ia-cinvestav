diccionario = {
    "ferret": "ferret",
    "boar": "boar",
    "jaguar" : "jaguar",
    "giraffe": "giraffe",    
    "lizard" : "lizard",
    "locust": "locust",
    "lion": "lion",
    "wolf": "wolf",
    "parrot": "parrot",
    "raccoon": "raccoon",
    "butterfly": "butterfly",
    "fly": "fly",
    "gnat": "gnat",
    "bat": "bat",
    "otter": "otter",
    "bear": "bear",
    "polar bear": "polar bear",
    "oyster": "oyster",
    "sheep": "sheep",
    "bee": "bee",
    "eagle": "eagle",
    "antelope": "antelope",
    "spider": "spider",
    "tuna": "tuna",
    "ostrich": "ostrich",
    "wasp": "wasp",
    "whale": "whale",
    "bison": "bison",
    "buffalo": "buffalo",
    "owl": "owl",
    "donkey": "donkey",
    "horse": "horse",
    "goat": "goat",
    "squid": "squid",
    "chameleon": "chameleon",
    "camel": "camel",
    "crab": "crab",
    "kangaroo": "kangaroo",
    "cat": "cat",
    "dog": "dog"
}
diccionario_a = {}
diccionario_b = {}
diccionario_y = {}

for palabra in sorted(diccionario.keys()):
    if "a" in palabra:
        diccionario_a[palabra] = palabra

print("Diccionario con palabras que contienen la letra 'a':\n")
for clave, valor in diccionario_a.items():
    print(f"{clave} : {valor}")

print()
input("Presiona Enter para continuar...")
print()

for palabra in sorted(diccionario.keys()):
    if "b" in palabra:
        diccionario_b[palabra] = palabra

print("Diccionario con palabras que contienen la letra 'b':\n")
for clave, valor in diccionario_b.items():
    print(f"{clave} : {valor}")

print()
input("Presiona Enter para continuar...")
print()

for palabra in sorted(diccionario.keys()):
    if "y" in palabra:
        diccionario_y[palabra] = palabra

print("Diccionario con palabras que contienen la letra 'y':\n")
for clave, valor in diccionario_y.items():
    print(f"{clave} : {valor}")

