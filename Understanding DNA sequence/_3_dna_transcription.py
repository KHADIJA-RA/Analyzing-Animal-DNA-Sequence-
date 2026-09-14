dna = "ATGCGTACGTTAGCTA"
def transcribe_dna(dna):
    return dna.replace("T", "U")
    

rna = transcribe_dna(dna)

print("DNA:", dna)
print("RNA:", rna)