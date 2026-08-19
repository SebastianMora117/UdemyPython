# /d digigito numerico 
# /w caracter alfanumerico
# /s espacio en blanco
# /D digito no numerico
# /W caracter no alfanumerico
# /S espacio no en blanco

# + 1 o mas ocurrencias
# {n} n ocurrencias
# {n,m} entre n y m ocurrencias
# {n,} n o mas ocurrencias
# * 0 o mas ocurrencias
# ? 0 o 1 ocurrencia

import re

texto = "Hola, mi nombre es Juan y mi número de teléfono es 123-456-7890. También puedes contactarme en mi correo electrónico juan@email.com"

patron = "juan"

busqueda = re.search(patron, texto)
print(busqueda.start()) #imprime la posición donde inicia la coincidencia
print(busqueda.end()) #imprime la posición donde termina la coincidencia
print(busqueda.findall()) #imprime todas las coincidencias encontradas

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span()) #imprime la posición donde inicia y termina la coincidencia

texto_dos = "El número de teléfono es 123-456-7890 y el correo electrónico es juan@email.com"

patron = r"\d\d\d-\d\d\d-\d\d\d\d" #expresión regular para buscar un número de teléfono en formato xxx-xxx-xxxx

resultado = re.search(patron, texto_dos)
print(resultado)

#VERIFICACION DE CORREO ELECTRONICO
import re

email = "usuario@host.com"

def verificar_email(email):
    if re.search("@", email) and re.search(r"\.com$", email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

#VERIFICAR PRIMERA PALABRA DE UN TEXTO
import re

frase = "Hola CHAMO"

def verificar_saludo(frase):
    if re.match(r"Hola" ,frase):
        print("Ok")
    else:
        print("No has saludado")

#VALIDAR PATRONES
import re

cp = "AB123"

def verificar_cp(cp):

    if re.search(r"^[A-Za-z]{2}\d{4}$", cp):
        print("Ok")
    else:    
        print("El código postal ingresado no es correcto")