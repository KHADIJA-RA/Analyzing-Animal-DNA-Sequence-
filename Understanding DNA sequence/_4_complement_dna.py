dna = "ATGCGTACGTTAGCTA"
def complement_dna(dna):
    complement=''
    for base in dna:
        if base== 'A':
            complement+='T'
        elif base=='T':
            complement+='A'
        elif base== "G":
            complement+='C'
        elif base=='C':
            complement+='G'
    return complement
    return complement[::-1]
 
result = complement_dna(dna)


print("DNA:", dna)
print("Complement:", result)

