dna= "ATGCATF"
def validate_dna(dna):
    for base in dna:
        if base not in "ATGC":
            print("Inavalid base", base)
            return False
    return True

print("Valid DNA:", validate_dna(dna))
dna2= "ATTGCA"
def validate_dna2(dna2):
    for base in dna2:
        if base not in "ATGC":
            print("Invalid base", base)
            return False 
    return True
print("Valid DNA2",validate_dna2(dna2))