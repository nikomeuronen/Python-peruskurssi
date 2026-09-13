sukupuoli = input ("Kerro biologinen sukupuolesi (n/m): ")
hemoglobiini = int(input("Anna hemoglobiiniarvosi: "))
if sukupuoli == "n":
    if hemoglobiini < 117:
        print ("Hemoglobiinisi on alhainen")
    if 117 <= hemoglobiini <= 175:
        print ("Hemoglobiinisi on normaali")
    else: 
        print("Hemoglobiinisi on korkea")
elif sukupuoli == "m":
    if hemoglobiini < 134:
        print ("Hemoglobiinisi on alhainen")
    if 134 <= hemoglobiini <= 195:
        print ("Hemoglobiinisi on normaali")
    else:
        print ("Hemoglobiinisi on korkea")
else:
    print("Virheellisesti syötetty sukupuoli")
