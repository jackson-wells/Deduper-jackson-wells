#!/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=4
#SBATCH --job-name=deduper
#SBATCH --nodes=1
#SBATCH --time=1-00:00:00
#SBATCH --error=logs/deduper_%j.txt
#SBATCH --output=logs/deduper_%j.txt 

/usr/bin/time -v python /projects/bgmp/jwel/bioinfo/Deduper-jackson-wells/Wells_deduper.py \
    -f /projects/bgmp/jwel/bioinfo/Deduper-jackson-wells/input.sorted.sam \
    -u /projects/bgmp/jwel/bioinfo/Deduper-jackson-wells/STL96.txt \
    -o /projects/bgmp/jwel/bioinfo/Deduper-jackson-wells/output.sam
