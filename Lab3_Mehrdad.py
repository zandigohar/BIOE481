# Script 1
# BIOE481_HW3
# Mehrdad Zandigohar

# Q1
print("Q1.________________Python Version________________")
import sys
print(sys.version,'\n')
# Python 3.8.5 is the version of current Python on my OS


# Q2
print("Q2.________________Tuple vs. List________________")
print("Mehrdad\t09/22/2020\nBIOE481\n2020",'\n')


# Q3
print("Q3.________________Tuple vs. List________________")
a=0.825
b=0.125
c=a/b
d=a+b
e=a*b

print("c=%.3f" % c)
print("d=%.3f" % d)
print("e=%.3f" % e,'\n')


l = ['alfa', 'beta', 'gamma']
t = ('alfa', 'beta', 'gamma')


# Q4
print("Q4.________________Tuple vs. List________________")
print("1. Creation: Use brackets for lists and paranthesis for tuples to creat it:")
print("List:", l)
print("Tuple:", t,'\n')

print("2. Data Type: They are different data structures:")
print("List:", type(l))
print("Tuple", type(t),'\n')

print("3. Mutability: You can modify a list but not a tuple:")
print("Lets try to replace the 3rd element by 'omega'.")
l[2] = 'omega'
print("List:",l)
try:
    t[2] = 'omega'
except Exception as err:
    print("Tuple:",err)
print("Note: Lists can be modified unlike tuples as seen above. \n")

print("4. Storage: Lists take more memory comparing to tuples:")
print('List:',l.__sizeof__())
print('Tuple:',t.__sizeof__(),'\n')

print("5. Reading Data: Tuples are easy to read and used as key in dictionaries:")
key_val= {t:2020}
print("tuple:",key_val)
try:
    key_val = {l:2020}
except Exception as err:
    print("list:",err,'\n')


# Q5
print("Q5.________________DNA and RNA nitrogenous bases________________")

dna_base=["Cytosine", "Guanine", "Adenine", "Thymine"]
rna_base=("Cytosine", "Guanine", "Adenine", "Uracil")
print("dna_base=",dna_base)
print("rna_base=",rna_base,'\n')


# Q6
print("Q6.________________Dictionary of Some Amino Acids________________")
amino_dict={"ALA":0.17,"ARG":0.81,"ASN":1.23,"CYS":-0.24,"VAL":0.07}
print("Dictionary: {Residue : Hydrophobicity}")
print("amino_dict",amino_dict,'\n')
print("For VAL the hydrophobicity is:",amino_dict["VAL"],'\n')
print("_____________________________The End_____________________________")
# End
