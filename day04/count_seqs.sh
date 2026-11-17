#!/bin/zsh
# UPSKILLER · DAY 4 · Shell lesson · your first shell script
#
# GOAL: running   ./count_seqs.sh neuro_genes.fasta
# should print:
#     File: neuro_genes.fasta
#     Sequences: 6
#     Microglia genes: 2
#
# $1 means "the first thing typed after the script name" (here: neuro_genes.fasta).
# Fill in the three TODO lines. Then, in the terminal:
#     chmod +x count_seqs.sh        (make it runnable, once)
#     ./count_seqs.sh neuro_genes.fasta

file=$1
if [ -z "$file" ]; then
    echo "Usage: ./count_seqs.sh FILE"
    exit 1
fi
echo "File: $file"
# TODO 1: print "Sequences: " followed by the number of header lines (lines starting with >)
echo "Sequences: $(grep -c "^>" "$file")"

# TODO 2: print "Microglia genes: " followed by how many header lines contain the word microglia
      echo "Microglia genes: $(grep "^>" "$file" | grep -c "microglia")"

# TODO 3 (bonus): if no file name was given, print "Usage: ./count_seqs.sh FILE" and stop.
#         hint: this goes ABOVE echo "File...":
#         if [ -z "$file" ]; then echo "Usage: ./count_seqs.sh FILE"; exit 1; fi
