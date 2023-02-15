def DNA_strand(dna):
    # code here
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    # return "".join([complement[base] for base in dna])
    result = ""
    for base in dna:
        result += complement[base]
    
    return result

print(DNA_strand("GTAT"))