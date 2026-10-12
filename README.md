# DNA Sequence Analyzer
A beginner Python bioinformatics project that analyzes DNA sequences by calculating nucleotide counts and GC/AT contents.

## Project Overview
This project was created as part of my journey as a Biochemistry student learning Python and Bioinformatics.
The program accepts up to three DNA sequences, checks whether they contain valid DNA bases, and analyzes valid sequences.

## Feactures
- Accepts up to three DNA sequences.
- Converts lowercase letters to uppercase.
- Removes leading, trailing, and internal spaces.
- Validates DNA sequences using A, T, G, C.
- Counts individual nucleotides (A, T, G, C).
- Calculates GC content and AT content.
- Classifies sequences as GC-rich or AT-rich.
- Rejects invalid or empty DNA sequences.

## Technologies Used
- Python 3
- GitHub

## How to Run
1. Install Python 3
2. Download `practice_7.py` from this respository.
3. Open the file in Python IDLE or another Python editor.
4. Run the program
5. Enter up to three DNA sequences when prompted

## Example
input:
ATGC

Expected analysis:
- Length: 4
- A: 1
- T: 1
- G: 1
- C: 1
- GC content: 50.0%
- AT content: 50.0%
- Classificaton GC-rich
