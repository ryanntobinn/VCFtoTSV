# VCFtoTSV
This script processes a VCF (Variant Call Format) files, converting the file to  a TSV (Tab Seperated Values) file using the column headers 'mutation_id', 'ref_counts',  'var_counts', 'normal_cn', 'minor_cn', and 'major_cn'. This can be used to create an  input file for use in the program PyClone.

## Input
Path to VCF (.vcf) and name desired for output (.tsv) file

## Usage 
vcf.py /path/to/file.vcf output_file.tsv
