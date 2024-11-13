#!/usr/bin/python

import argparse
import textwrap

def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='python ./Wells_deduper.py',
		description="Remove PCR duplicates from a sorted sam file",
		formatter_class=argparse.RawDescriptionHelpFormatter,
		epilog=textwrap.dedent('''\
A software tool to remove all PCR duplicates from a sorted sam file containing 
uniquely mapped reads, such that only a single copy of each read is maintained 
in an output sam file. The software tool created should minimize usage of memory 
during execution and accurately identify all potential instances of 
PCR duplicfication.\n
         '''))
    parser.add_argument("-f", "--file",help="Input sorted sam file", type=str, required=True)
    parser.add_argument("-u", "--umi", help="valid UMI file", type=str, required=True)
    parser.add_argument("-o", "--outfile", help="output file", type=str, required=True)
	
    return parser.parse_args()

def getUMI(qname : str) -> str:
	'''parses QNAME string and returns the UMI'''
	temp = qname.split(':')
	return temp[7]

def readInputUMIs(file : str) -> dict:
	'''Takes in file name and returns a dictionary of UMIs'''
	tempDict = {}
	with open(file, "r") as fh:
		for line in fh:
			line = line.strip('\n')
			tempDict[line] = 1
	return tempDict

def getStrand(flag : int) -> bool:
	'''Takes in flag and returns true if read is on forward strand'''
	if ((flag & 16) == 16):
		return False
	else:
		return True

def getFivePrimePosition(cigar : str, pos : int, strand : bool) -> int:
	'''Calculates 5' position in read'''
	#Minus front S value (or 0) from start position
	tempPos = pos - getFrontClip(cigar)
	#if forward strand, return updated position 
	if strand:
		return tempPos
	#if reverse strand
	else:
		#return position + length
		return (tempPos + getCigarLength(cigar))

def getFrontClip(cigar : str) -> int:
	'''Checks for front clipping, returns amount of front clipped bases'''
	#if an S exists before the last character of the string
	if cigar.find('S',0,len(cigar)-1) > 0:
		#return 0 to the position of S in the cigar string as an int
		return int(cigar[0:cigar.find('S',0,len(cigar)-1)])
	else:
		#no front clipping, return 0
		return 0

def getCigarLength(cigar : str) -> int:
	'''Converts number characters to integers and returns a sum'''
	#Acceptable characters to be included in sum
	included = ['S', 'M', 'X', 'D', '=', 'N']
	sum = 0
	temp = ''
	#Loop over every position in the cigar string 
	for value in cigar:
		#If a number is encountered, append it to string
		if value.isdigit():
			temp += value 
		#If a character is encountered 
		else:
			#if that character is valid 
			if value in included:
				#typecast string to an integer and add to sum
				sum += int(temp)
			#Reset string 
			temp = ''
	return sum

def deduplicate(inputFile : str, outputFile : str, UMIs : dict) -> None:
	'''Removes PCR duplicates from input file'''
	reads = {}
	chrs = {}
	headerLines = 0
	uniqueReads = 0
	invalidUMIs = 0
	duplicatesRemoved = 0

	with open(inputFile,"r") as iFh, open(outputFile, "w") as oFh:
		while True:
			read = iFh.readline().strip()

			#EOF
			if read == '':
				break
			#Header lines 
			elif read[0] == '@':
				headerLines += 1
				oFh.write(read + "\n")
				continue
			#Read lines
			else:
				readList = read.split('\t')
				
				# clear read dictionary (memory) on new chromosome
				if readList[2] not in chrs.keys(): 
					del reads
					reads = {}
					chrs[readList[2]] = 0

				#Get UMI from read 
				umi = getUMI(readList[0])

				#if UMI is found in input UMI file
				if umi in UMIs.keys():
					
					#Gets read strand 
					strand = getStrand(int(readList[1]))

					#Calculates read 5' position from cigar, position and strand 
					fivePrimePosition = getFivePrimePosition(str(readList[5]), int(readList[3]), strand)

					#If read parameter pairing is novel 
					if (strand,umi,fivePrimePosition) not in reads.keys():			
						#store read pairing (composite key)
						reads[(strand,umi,fivePrimePosition)] = 1				
						oFh.write(read + "\n")
						#increment read and chromosome read counts 
						uniqueReads += 1
						chrs[readList[2]] += 1
					#Duplicate
					else:
						duplicatesRemoved += 1	
				#Invalid/Unknown UMI
				else:
					invalidUMIs += 1

	for chr in chrs:
		print(chr + "\t" + str(chrs[chr]))
	print("Number of header lines: " + str(headerLines))
	print("Number of Unknown UMIs: " + str(invalidUMIs))
	print("Number of unique reads: " + str(uniqueReads))
	print("Number of duplicates removed: " + str(duplicatesRemoved))
	return

def main() -> None:
    args = getArgs()

	#Read in UMI file 
    UMIs = readInputUMIs(args.umi)
	
	#Deduplicate reads in sam file 
    deduplicate(args.file, args.outfile, UMIs)

if __name__ == "__main__":
    main()