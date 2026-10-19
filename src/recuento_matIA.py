instrumentos = ["pinza", "tijera", "pinza"]
pinzas_esperadas=2
contador=0
for n in instrumentos:
    if n =="pinza":
        contador=contador+1
print(f"Pinzas contadas {contador}")
print(f"Pinzas esperadas {pinzas_esperadas}")
if contador < pinzas_esperadas:
    print("Resultado: faltan pinzas")
elif contador > pinzas_esperadas:
    print("Resultado: sobran pinzas")
else:
    print("Resultado: coincide")

