# Example Cases

## Case 1 (Non-duplicate)

	Different strand
## Case 2 (Non-duplicate)

	Different UMI
## Case 3 (Non-duplicate)

	Different chromosomes
## Case 4 (Non-duplicate)

	reverse stranded, identical sam position, clipping on left

	3'	     5'
	CTTCTATTATCCTT
	CTTCTATTATCCTT

	CIGAR: 	14M
	Pos: 	111
	ePos: 	125

	3'	     5'
	CTTCTATTATCCTT
        AGTCTATTATCCTT

	CIGAR: 	2S12M
	Pos: 	111
	ePos: 	123

## Case 5 (Duplicate)

	111+14 = 125

	reverse stranded, identical sam position, clipping on right

	3'	     5'
	CTTCTATTATCCTT
	CTTCTATTATCCTT

	CIGAR: 	14M
	Pos: 	111
	ePos: 	125

	3'	     5'
	CTTCTATTATCCTT
	CTTCTATTATCCAG

	CIGAR: 	12M2S
	Pos: 	111
	ePos:	123+2

## Case 6 (Non-duplicate)

	113+14 =/= 125

	reverse stranded, non-identical sam position, clipping on right

	3'	     5'
	CTTCTATTATCCTT
	CTTCTATTATCCTT

	CIGAR: 	14M
	Pos: 	111
	ePos: 	125

	3'	     5'
	CTTCTATTATCCTT--
	--TCTATTATCCTTAG

	CIGAR: 	12M2S
	Pos: 	113
	ePos:	125+2

## Case 7 (Non-duplicate)

	113+12 = 125 

	reverse stranded, non-identical sam position, clipping on left

	3'	     5'
	CTTCTATTATCCTT
	CTTCTATTATCCTT

	CIGAR: 	14M
	Pos: 	111
	ePos: 	125

	3'	     5'
	CTTCTATTATCCTTGG
	   AGTATTATCCTTGG

	CIGAR: 	2S12M
	Pos: 	113
	ePos:	127

## Case 8 (Non-duplicate)

	113+14 =/= 125

	forward stranded, non-identical sam position, clipping on right

	5'	     3'
	CTTCTATTATCCTT
	CTTCTATTATCCTT

	CIGAR: 	14M
	Pos: 	111
	ePos:	125

	5'	    3'
	CTTCTATTATCCTT--
	--TCTATTATCCTTAG

	CIGAR: 	12M2S
	Pos: 	113
	ePos: 	125+2

## Case 9 (Duplicate)	

	113+12 = 125 

	forward stranded, non-identical sam position, clipping on left
	
	5'	    3'
	CTTCTATTATCCTT
	CTTCTATTATCCTT

	CIGAR: 	14M
	Pos: 	111
	ePos:	125

	5'	    3'
	CTTCTATTATCCTT
	AGTCTATTATCCTT

	CIGAR: 	2S12M
	Pos: 	113
	ePos: 	125

## Case 10 (Non-duplicate)

	111+12 =/= 125

	forward stranded, identical sam position, clipping on left

	5'	    3'
	CTTCTATTATCCTT
	CTTCTATTATCCTT

	CIGAR: 	14M
	sPos: 	111
	ePos:	125
	
	5'	    3'
	CTTCTATTATCCTT
        AGCTTCTATTATCC

	CIGAR: 	2S12M
	sPos: 	111
	ePos: 	123

## Case 11 (Duplicate)

	111+14 = 125 

	forward stranded, identical sam position, clipping on right

	5'	    3'
	CTTCTATTATCCTT
	CTTCTATTATCCTT

	CIGAR: 	14M
	sPos: 	111
	ePos:	125
	
	5'	    3'
	CTTCTATTATCCTT
	CTTCTATTATCCAG

	CIGAR: 	12M2S
	sPos: 	111
	ePos: 	123+2
## Case 12 (Non-duplicate)

	Unknown UMI