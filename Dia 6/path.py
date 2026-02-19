from pathlib import *

base = Path.home()
guia = Path("madrid", "Santiago Bernabeu")
guia2 = guia.with_name("nose.txt")

print(base)
print(guia)
print(guia2)