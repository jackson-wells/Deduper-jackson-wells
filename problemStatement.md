# Problem Statement
		During library preparation, amplification is often necessitated to ensure adequate 
	sequencing yeilds and sample coverage. PCR is used to complete the amplication step but can 
	introduce duplicated read sequences and bias. Because of this, it then becomes a requirement 
	to deduplicate sequencing data so that errors are not encountered in downstream analysis. 
	
		We have been tasked with the development of a software tool to remove all PCR duplicates 
	from a sorted sam file containing uniquely mapped reads, such that only a single copy of each 
	read is maintained in an output sam file. The software tool created should minimize usage of 
	memory during execution and accurately identify all potential instances of PCR duplicfication. 
	
		Given that this can be accomplished in a timely manner, the software tool should also be 
	able to complete this process for single-end and paired-end data inputs, differentiate 
	between known and random UMIs and perform error correction on UMIs. 
# Definitions

### PCR-duplicate 
	Duplicated read sequences that occur when two (or more) copies of the same molecule get 
	onto different beads in a flow cell 

### Soft-Clipping
	Removal of bases from either end of read sequences that do do not align with the reference

### CIGAR String
	Number of bases precede an identifier character
	
#### Example 1 
	CIGAR String: 14M
		14 base matches or mismatches

#### Example 2
	CIGAR String: 2S12M
		2 bases soft clipped 
		12 bases matched/mismatched 

#### Example 3
	CIGAR String: 5M1024N5M
		5 bases matched/mismatched
		1024 bases skipped
		5 bases matched/mismatched

### UMI/Randomer
	short random sequence of bases added to each molecule during sequencing. 
# Key Points 
- Single-end data
- 96 known UMIs (Unique Molecular Index)
- Strand must be computed from bit flag
- Discard UMIs with errors
- Retain only single copy of each read
- Do not load everything into memory
	- open output file and input file simultaneously 
- Adjust for soft clipping
	- Sam file positions will be offset if soft-clipping has occurred 
- Duplicates have 
	- Same Alignment position
		- Chromosome 
		- 5' start of read
		- Strand 
	- Same UMI
- left side clipping does not contribute to end position, right side it does 

| Read Identifier | Sam File Column | Sam Name  |
| --------------- | --------------- | --------- |
| Chromosome      | 3               | RNAME     |
| Position        | 4               | POS       |
| Strand          | 2               | FLAG      |
| 5' Start        | 4+6             | POS+CIGAR |
| UMI             | 1               | QNAME[7]  |
