dna='ATGCGTACGTTAGCTA'
#find length of dna 
length= len(dna)
print("DNA lenght =", length)
#give access to indiviual characters
for base in 'ATGC':
    print(base, ':', dna.count(base))

def gc_content(dna):
    g = dna.count("G")
    c = dna.count("C")

    return (g + c) / len(dna) * 100
print("GC content",gc_content(dna),'%')
result = gc_content(dna)
def at_content(dna):
    a = dna.count("A")
    t = dna.count("T")

    return (a + t) / len(dna) * 100
print("A + T Content:", at_content(dna), "%")

#Validate the DNA sequence 
def validate_dna(dna):
    for base in dna:
        if base in "ATGC":
            return True

    return False
print("valid DNA:",validate_dna(dna))
