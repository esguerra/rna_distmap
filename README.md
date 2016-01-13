
README
================================================================================

rna_distmap is just the simplest possible script to plot a distance matrix.
It uses scipy's spatial.distance function to compute the distance matrix
of all atom-to-atom distances.

## Version

This is version 0.2 created on October 30, 2012 while postducking at Kar. Inst.
in tze Zveeden.

## Setup

1. Clone the repository

```git
git clone https://github.com/esguerra/rna_distmap.git
```

## Usage

To run the program just call it from the prompt:

```bash
./rna_distmap.py 1ehz
```

It will make a picture just like the one in Yathindra and Malathi's
1982 paper [1] for the crystal structure of phenylalanine tRNA at 1.93
Angstrom resolution.  

[1] R. Malathi and N. Yathindra, Secondary and tertiary structural
foldings in tRNA, Biochemistry Journal, **1982**, *205*, 457-460  


