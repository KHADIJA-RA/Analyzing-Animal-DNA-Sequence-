from rna_translation import codon_table
from dna_transcription import transcribe_dna

def translate_rna(rna):
    protein = ""

    start = rna.find("AUG")

    if start == -1:
        return "No start codon found"

    for i in range(start, len(rna) - 2, 3):
        codon = rna[i:i+3]
        amino_acid = codon_table[codon]

        if amino_acid == "*":
            break

        protein += amino_acid

    return protein
rna = "CCCAUGCGUACGUUAGCUA"

protein = translate_rna(rna)

print("RNA:", rna)
print("Protein:", protein)

rna = "CCCGCGUAC"

protein = translate_rna(rna)

print("RNA:", rna)
print("Protein:", protein)

rna = "AUGCGUUAAACCGG"

protein = translate_rna(rna)

print("RNA:", rna)
print("Protein:", protein)

dna = "ATGCGTACGTTAGCTA"

rna = transcribe_dna(dna)
protein = translate_rna(rna)

print("DNA:", dna)
print("RNA:", rna)
print("Protein:", protein)