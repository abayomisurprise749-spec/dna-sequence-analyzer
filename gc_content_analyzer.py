dna = input("Enter a DNA sequence: ").upper().strip()

valid_bases = "ATGC"

if dna == "":
    print("Error: DNA sequence cannot be empty.")
elif any(base not in valid_bases for base in dna):
    print("Error: Invalid DNA sequence.")
else:
    print("DNA sequence:", dna)
    print("Sequence length:", len(dna))

    g_count = dna.count("G")
    c_count = dna.count("C")

    gc_content = (g_count + c_count) / len(dna) * 100

    print("G count:", g_count)
    print("C count:", c_count)
    print("GC content:", gc_content, "%")

    if gc_content >= 50:
        print("Classification: GC-rich")
    else:
        print("Classification: AT-rich")

    print("A count:", dna.count("A"))
    print("T count:", dna.count("T"))
    print("G count:", dna.count("G"))
    print("C count:", dna.count("C"))

        
    
