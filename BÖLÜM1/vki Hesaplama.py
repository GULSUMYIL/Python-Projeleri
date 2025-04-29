# vki hesaplama

print("Vücut kitle indexi hesaplama:)")
print()
kilo=float(input("Kilonuzu giriniz: "))
boy=float(input("Boyunuzu giriniz(cm cinsinden: )"))
vki=kilo/(boy/100)**2
print(f"Vücut kitle endeksi: {vki}")

