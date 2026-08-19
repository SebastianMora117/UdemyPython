from datetime import *

mi_hora = datetime.time(14, 30, 0) #hora, minuto, segundo
print(type(mi_hora))
print(mi_hora.minute) #obtener el minuto
print(mi_hora.hour) #obtener la hora

mi_dia = datetime.date(2024, 6, 1) #año, mes, día
print(mi_dia.year) #obtener el año
print(mi_dia.month) #obtener el mes
print(mi_dia.day) #obtener el día

dia_pc = datetime.date.today() #obtener la fecha actual del sistema
print(dia_pc)

mi_fecha_hora = datetime(2024, 6, 1, 14, 30, 0) #año, mes, día, hora, minuto, segundo
mi_fecha = mi_fecha.replace(month = 1) #reemplazar el mes por otro
print(mi_fecha)

nacimiento = date(1990, 1, 1)
defuncion = date(2070, 8, 30)
vida = defuncion - nacimiento #calcular la diferencia entre dos fechas
print(vida.days) #obtener la cantidad de días entre las dos fechas