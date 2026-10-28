import site
import sys

sys.path.append(site.getusersitepackages())

from Bio.Seq import Seq

sequence = input("Enter a DNA sequence: ").upper().strip()

if sequence == "":
    print("Error: DNA sequence cannot be empty.")
elif all(base in "ATGC" for base in sequence):
    dna = Seq(sequence)

    print("DNA sequence:", dna)
    print("Length:", len(dna))
    print("RNA sequence:", dna.transcribe())
    print("Complement:", dna.complement())
    print("Reverse complement:", dna.reverse_complement())

else:
    print("Error: Invalid DNA sequence!")



    

