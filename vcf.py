#!/usr/bin/env python

# vcf.py
# Ryan Tobin, 2023
# Version 1.0.0

# This script has been tested in Python 3.9 

'''
This script processes a VCF (Variant Call Format) files, converting the file to 
a TSV (Tab Seperated Values) file using the column headers 'mutation_id', 'ref_counts', 
'var_counts', 'normal_cn', 'minor_cn', and 'major_cn'. This can be used to create an 
input file for use in the program PyClone
'''

import sys

if len(sys.argv) < 3:
    print('\nvcf.py')
    print('This script processes a VCF (Variant Call Format) file, converting the file to')
    print('a TSV (Tab Seperated Values) file using the column headers "mutation_id", "ref_counts",')
    print("'var_counts', 'normal_cn', 'minor_cn', and 'major_cn'. This can be used to create an ")
    print("input file for use in the program PyClone")
    print('\nInput: Path to VCF (.vcf) file and name desired for output (.tsv) file')
    print('\nUsage: vcf.py /path/to/file.vcf output_file.tsv')
    sys.exit(0)

# Open the input VCF file
with open(sys.argv[1], "r") as vcf_file:
    # Open the output TSV file
    with open(sys.argv[2], "w") as tsv_file:
        # Write the column headers to the output TSV file
        tsv_file.write("mutation_id\tref_counts\tvar_counts\tnormal_cn\tminor_cn\tmajor_cn\n")

        # Loop through each line in the input VCF file
        for line in vcf_file:

            # Skip any lines that start with '#' 
            if line.startswith("#"):
                continue

            # Split the line by tab characters
            parts = line.strip().split("\t")

            # Combine CHROM, REF, and ALT with "_"
            mutation_id = "_".join([parts[0], parts[3], parts[4]])
            
            # Replace original '0/1:' with blank space in TUMOR data
            tumor_string = parts[10].replace('0/1:','')

            # Split at the character ":" and only keep characters BEFORE ":"
            new_tumor_string = tumor_string.split(':')[0]

            # Split at the character "," and seperate into two new columns
            ref_counts, var_counts = new_tumor_string.split(',')
            
            # Write the mutation ID and the constant values for the other columns to the output TSV file
            tsv_file.write(f"{mutation_id}\t{ref_counts}\t{var_counts}\t2\t0\t2\n")
