dias = ["lunes","martes","miercoles"]
print(dias)
print(dias[1])
dias.append("miercoles")
print(dias)
dias.pop()
del dias[0]
print(dias)
dias[0] =  "domingo"
print(dias)

for dia in dias:
    print(dia,end=" ")

alumnos = []
totalAlumnos = int(input("ingrese el total de alumnos a registrar:"))
for contador in range(totalAlumnos):
    nuevoAlumno = input("Nombre del alumno " + str(contador) + " : ")
    alumnos.append(nuevoAlumno)
print("relación de alumnos : ")
for alumno in alumnos:
    print(alumno,end= " | ")