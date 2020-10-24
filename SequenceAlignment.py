class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Reading the sequence from the text file and set the value for alignment
f1 = open("ReferenceSequence.txt", "r")
if f1.mode == "r":
    Reference_Sequence = f1.read()
f1.close()

f2 = open("SampleSequence.txt", "r")
if f2.mode == "r":
    Target_Sequence = f2.read()
f2.close()
# Display of the sequence that are going to align
print("Your Sample Sequence: " + Target_Sequence)
print("The Reference Sequence: " + Reference_Sequence)
#
print("Alignment is in progress........")
print("...")
print("...")
print("Here is the result:")
print("")

# Variables was set for the while loop and output

output = ""
ua = ""
i=0

# Running the alignment. If the nucleotide is matched, it will added to the alligned result. Otherwise, it will be unmatched
while i < len(Reference_Sequence):
    if Reference_Sequence[i] == Target_Sequence[i]:
        output += Reference_Sequence[i]
        ua += " "
    if Reference_Sequence[i] != Target_Sequence[i]:
        output += " "
        ua += Target_Sequence[i]
    i=i+1
# Print out the result
print("Reference sequence: " + Reference_Sequence)
print("Alligned sequence:  " + color.BOLD + color.YELLOW + output + color.END)
print("Unmatched sequence: " + color.RED + ua + color.END)
