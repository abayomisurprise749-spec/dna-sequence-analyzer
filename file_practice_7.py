count = 1

while count <= 3:
    print("SAMPLE", count)

    dna = input("Enter a DNA sequence:")

    dna = dna.upper()
    dna = dna.strip()
    dna = dna.replace(" ", "")

    valid_bases = "ATGC"
    dna_status = "Valid"

    for base in dna:
         if base not in valid_bases:
             dna_status = "Invalid"
             print("Invalid base found:", base)
             break
    if dna_status == "Valid":
        print("Your entered:", dna)
        print("A:", dna.count("A"))
        print("T:", dna.count("T"))
        print("G:", dna.count("G"))
        print("C:", dna.count("C"))

        g = dna.count("G")
        c = dna.count("C")
        gc = (g + c) / len(dna) * 100

        print("GC content:", round(gc, 2), "%")

        if gc >= 50:
            print("GC-rich DNA")
    else:
        print("AT-rich DNA")

    count = count + 1
    
