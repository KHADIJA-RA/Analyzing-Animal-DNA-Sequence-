dna='ATGCGTACGTTAGCTA'
#find length of dna 
length= len(dna)
print("DNA lenght =", length)
#give access to indiviual characters
for base in dna:
    print(base)


print("A:", dna.count("A"))
print("T:", dna.count("T"))
print("G:", dna.count("G"))
print("C:", dna.count("C"))
# count the G+C content 

def gc_content(dna):
    g = dna.count("G")
    c = dna.count("C")

    return (g + c) / len(dna) * 100
result = gc_content(dna)
print ('GC content:' ,result,'%')