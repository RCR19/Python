print("introduce dos numeros a comparar: \n")

num_1 = int(input("introduce el primer numero: "))
num_2 = int(input("introdice el segundo numero: "))

print("\n Los numeros a comparar son", num_1, "Y", num_2, "\n")

if num_1 == num_2:
    print("Es igua...")
if num_1 != num_2:
    print("Es diferente...")
if num_1 <= num_2:
    print("Es menor o igual...")
if num_1 >= num_2:
    print("Es mayor o igual...")
if num_1 > num_2:
    print("Es mayor...")
if num_1 < num_2:
    print("Es menor...")
