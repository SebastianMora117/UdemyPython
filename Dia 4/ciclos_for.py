lista = ['Sebastian', 'Juan', 'David']

for persona in lista:
    numero_persona = lista.index(persona) + 1
    print(f"Hola {persona} eres el {numero_persona} de la lista")

palabra = "Hola mundo"

for l in palabra:
    print(l)

dic = {'clave 1': 'a', 'clave 2': 'b'}

for a, b in dic.items():
    print(f"{a} : {b}")