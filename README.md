# FindMirTar
Compute the correlation between microRNA and target.

A tool to collate microRNA with transcriptome data. The output files are concurrent with MirTarSite obligatory input format. Conflate the sequencing data and deep-learning method to predict microRNA target.

## Introduction
MicroRNAs are a non-coding RNA in Eukaryota. Manifestly function as regulate transcriptional and translational programs by base pairing. They modulate biological processes, such as development, proliferation, and defense mechanism. Hence, apprehend the target of microRNAs could elevate gene expression research. 

Previous studies showed that one microRNA confine different genes. Experiment, however, could not freely express determinate target results without sequencing data. In addition, it is important for researchers to analyze these data with an accurate and effectual method.

What follows is a outline of FindMirTar scoring method to predict target gene. If there is a mismatch, A pairing to G or C pairing to T, for example, the penalty score will increase 1 point. Other mismatch, such as G:U wobble, will increase 0.5 point.

### Predict microRNA Target
#### Requirements
* Python 3.7+
* argparse
* pandas
* ruby
* Bowtie (http://bowtie-bio.sourceforge.net/)

#### Input 
* microRNA fasta file
```
>hsa-miR-183-5p
UAUGGCACUGGUAGAAUUCACU
>hsa-miR-33a-5p
GUGCAUUGUAGUUGCAUUGCA
>hsa-miR-129-5p
CUUUUUGCGGUCUGGGCUUGC
```
* transcriptome fasta file (Homo_sapiens.GRCh38.cdna.abinitio)
```
>GENSCAN00000000001 cdna chromosome:GRCh38:5:122151991:122153085:1 transcript_biotype:protein_coding
ATGGAAAGAGGAAAGAAGAAAAGAATTTCCAATAAGTTACAACAAACTTTTCACCATTCT
AAAGAACCCACTTTCCTTATCAACCAAGCTGGGCTTCTCTCTAGTGACTCCTATTCTAGC
CTTTCCCCAGAAACAGAGAGTGTTAATCCTGGTGAAAATATAAAGACAGACACTCAGAAA
AAGAGACCTGGGACTGTGATACTATCAAAACTGTCAAGTAGAAGAATTATATCGGAAAGC
CAGCTTAGCCCCCCTGTGATCCCGGCCCGCAGGCCTGGATTCCGGGTATGCTATATCTGT
GGCCGAGAATTTGGGTCCCAGTCAATTGCCATTCATGAACCCCAGTGCTTGCAGAAGTGG
CATATTGAAAACAGCAAGTTGCCCAAGCATTTGAGGAGGCCAGAACCCTCCAAACCACAG
TCTCTCAGCAGCAGTGGGTCCTACAGTCTTCAGGCAACTAACGAGGCTGCATTTCAGAGT
GCCCAGGCTCAGCTGCTGCCCTGTGAATCCTGTGGCCGCACATTCTTGCCAGATCATCTT
CTTGTTCATCACAGAAGCTGCAAGCCAAAGGGTGAGGGTCCCAGAGCACCACACTCAAAC
AGTTCTGATCATCTTACTGGCCTCAAGAAAGCTTGTAGTGGAACCCCAGCCCGACCAAGG
ACTGTTATCTGCTACATATGTGGTAAGGAATTTGGCACCCTGTCCCTTCCTATTCATGAG
CCCAAATGCCTGGAAAAGTGGAAAATGGAAAATGACCGGCTCCCTGTGGAGCTCCACCAG
CCACTCCCACAGAAGCCTCAGCCCCTTCCGAATGCACAGTCCAGCCAAGCGGGACCAAAT
CAAGCTCAGCTTGTGTTCTGCCCACATTGTAGCCGAATCTTTACCTCAGACCGCCTCCTG
GTACACCAGAGAAGTTGTAAAACTCATCCTTATGGGCCAAAATATCAGAATTTGAATTTA
GGGAGTAAAGGAGGCCTAAAAGAGTACACTAATTCCAAGCAGCAAAGGAACAGGGCAGCA
CCCAGTGTAACTGATAAGGTAATTCATGCCACACAAGACGCATTAGGTGAACCTGGTGGT
GCCCTCTGCCTGTAG
```

#### Usage
Please make sure BOWTIE is added in your 'PATH' and MirTarSite folder is under the premirtar
```
python premirtar.py [-h] FULL-PATH-TO-microRNA-FASTA-FILE FULL-PATH-TO-TRANSCRIPTOME-FASTA-FILE

miRTarget
Tools to combine psRNAtarget and MirTarSite
Please type in the full path of miRNA and transcriptome data for analyzing!

positional arguments:
miRNA                 microRNA fasta file 5'->3' sequence
transcritome          transcriptome fasta file 5'->3' sequence

optional arguments:
  -h, --help  show this help message and exit
```
