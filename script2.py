

def main():
    lijst1, lijst2= getsequentie()
    seq= is_dna()
    knipt(lijst1, lijst2, seq)


def getsequentie():
    lijst1=[]
    lijst2=[]
    for regel in open ("enzymen.txt"):
        regel.replace("^","")
        regel.split()
        lijst1.append(regel[0])
        lijst2.append(regel[1])
    return lijst1,lijst2

def is_dna():
    seq=""
    file="sequence.txt"
    for c in open (file):
        if c.startswith('>')==False:
            seq+=c.rstrip()
    validDNA="ATCG"
    is_dna=all(c in validDNA for c in seq.upper())
    print(is_dna)
    return seq

def knipt (lijst1, lijst2, seq):
    for i in range(len(lijst2)):
        if lijst2[i] in seq:
            print("match met", lijst1[i] ,"in positie",seq.index(lijst2[i]))
            print (seq)
            

main()
