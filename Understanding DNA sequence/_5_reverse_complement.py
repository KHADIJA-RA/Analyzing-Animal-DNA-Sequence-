from 04_complement_dna import complement_dna

dna = "ATGCGTACGTTAGCTA"
def reverse_complement(dna):
    complement = complement_dna(dna)

    return complement[::-1]


result = reverse_complement(dna)

print("DNA:", dna)
print("Reverse Complement:", result)