# Functions

```python
def extractUMI(qname : str) -> str:
	'''parses QNAME string and returns the UMI'''
	temp = qname.split(':')
	return temp[7]
Input: "NS500451:154:HWKTMBGXX:1:11101:6610:1112:AACGCCAT"
Expected output: "AACGCCAT"

def getUMIs(file : str) -> dict:
	'''Takes in file name and returns a dictionary of UMIs'''
	tempDict = {}
	with open(file, "r"):
		for line in fh:
			line.strip('\n')
			tempDict[line] = True
	return tempDict
Input: "./STL96.txt"
Expected output: UMIs

def getArgs() -> argparse.Namespace:
	'''Processed command-line inputs and returns the arguements in a namespace object'''
	parser = argparse.ArgumentParser(description="Deduper")
	parser.add_arguement() #file
	parser.add_arguement() #outfile 
	parser.add_arguement() #umi file
	parser.add_arguement() #type (single-end/paired-end)
	parser.add_arguement() #assess duplicates
	parser.add_arguement() #randomers
	return parser.parse_args()
Input: NULL
Expected output: argparse.Namespace or Exception
```

## Algorithm
```python
Take in command line arguements

umis = getUMIs(umiFile)

#open output file 
oFh = open(outputFile,"w")

open input file

while line starts with "@":
	line = readline.strip
	write line to output file

#now at the first read, grab that line
read1 = line1.split('\t')

Chr1 = read1[4]
pos1 = read1[3]
strand1 = getStrand(read1[1])
umi1 = extractUMI(read1[0])
cigar1 = read1[5]

#loop to end of input file
while not EOF inputFile:

	line2 = readline.strip()

	if line2 = '':
		break

	read2=line2.split('\t')

	Chr2 = read2[4]
	pos2 = read2[3]
	strand2 = getStrand(read2[1])
	umi2 = extractUMI(read2[0])
	cigar2 = read2[5]

	#Check if UMI is valid/contained within the input UMI file
	if (umi1 in UMIs):
		#check if there is potentially a duplicate in read2
		if chr1 == chr2 && strand1 == strand2 && umi1 == umi2
			#check if Forward strand
			if strand1 == forward 
				#check if 5' start positions are matching 
				if (pos1 - leftS == pos2 || pos1 == pos2):
					#duplicate
					continue loop to grab next line
				else: 
					#non-duplicate
					write read1 to output file
					Chr1 = chr2
					pos1 = pos2
					strand1 = strand2
					umi1 = umi2
					cigar1 = cigar2
			#Reverse strand
			else: 
				#check if 5' start positions are matching 
				if(pos1 + cigar1(sum values of M/S/I/=/X) == pos2 + cigar2(sum values of M/S/I/=/X)):
					#duplicate
					continue loop to grab next line
				else: 
					#non-duplicate
					write read1 to output file
					Chr1 = chr2
					pos1 = pos2
					strand1 = strand2
					umi1 = umi2
					cigar1 = cigar2
		else:
			#values don't match, meaning new read encountered
			write read1 to output file
			Chr1 = chr2
			pos1 = pos2
			strand1 = strand2
			umi1 = umi2
			cigar1 = cigar2
	else:
		#invalid/unknown umi
		#discard 1
		1 values = 2 values 
```


