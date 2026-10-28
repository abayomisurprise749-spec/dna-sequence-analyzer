dna = input("Enter a DNA sequence: ").upper()
motif = input("Enter a motif to find: ").upper()

valid_bases = "ATGC"

if not dna or any(base not in valid_bases for base in dna):
    print("Invalid DNA sequence!")
elif not motif or any(base not in valid_bases for base in motif):
    print("Inalid motif!")
else:
    count = 0
    position = dna.find(motif)
    while position != -1:
        print("Motif found at position:", position)
        count = count + 1
        position = dna.find(motif, position + 1)

        print("Total overlapping occurences:", count)

        

