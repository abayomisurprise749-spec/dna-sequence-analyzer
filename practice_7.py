dna_sequences = []

count = 1
while count <= 3:
    dna = input("Enter DNA sequences" + str(count) + ": ")
    dna = dna.upper()
    dna = dna.strip()
    dna = dna.replace(" ", "")

    dna_sequences.append(dna)

    count = count + 1

    print("\nMULTI-SEQUENCE DNA ANALYZER")

    for dna in dna_sequences:
        print("\nSequence:", dna)

        valid_bases = "ATGC"
        valid = True

        for base in dna:
            if base not in valid_bases:
                print("Invalid base found:", base)
                valid = False
                break
        if valid and len(dna) > 0:
                print("Length:", len(dna))
                print("A:", dna.count("A"))
                print("T:", dna.count("T"))
                print("G:", dna.count("G"))
                print("C:", dna.count("C"))

                gc = (dna.count("G") + dna.count("C")) / len(dna) * 100
                at = (dna.count("A") + dna.count("T")) / len(dna) * 100

                print("GC content", round(gc, 2), "%")
                print("AT content:", round(at, 2), "%")

                if gc >= 50:
                    print("Classification GC-rich")
                else:
                    print("Classification AT-rich")

        else:
                    print("Please enter a valid, non-empty DNA sequence.")

                    print("-" * 30)





