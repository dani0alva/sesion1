dias = ("lunes","martes","miercoles")

print(dias)
dias = list(dias)
dias.append("jueves")
dias = tuple(dias)
print(dias)

print(dias[0:2])
for dia in dias:
    print(dia,end= ' - ')