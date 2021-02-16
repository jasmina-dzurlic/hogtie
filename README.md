# project
## class project for hackers class (in development)

### Description of project goal: 
This program will detect instances of horizontal gene transfer (HGT) along an evolutionary tree. It will return inferred HGT gene sequences, their gene trees (possibly), and will map the HGT events along the larger input phylogeny.

### Description of the code: 
To identify HGT, this program will use a combination of *k-mer*- and phylogenetic-based methods. This will use packages like"
  * `kmerkit` (in development) for k-mer parsing and comparison
  * `toytree` for visualizing HGT along a tree
  * the program will use a binary state maximum likelihood model for ancestral-state reconstruction
  
### Description of the data:
Inputs will be:
  * Genomic read data of the genome of interest (recipient genome)
  * Some sort of k-mer library that includes k-mers from closely and distantly related species (should include potential donor genomes)
  * Phylogeny

### Description or demonstration of user interaction:
The User would call the tool from CLI, point it to the recipient sequences, the sequences for "k-mer library", and the phylogeny. For example:
```
create_kmer_lib --donor1 --donor2 --donor3 --relatedspecies1 --relatedspecies2 etc.
find_my_hgt --recipient pedicularis.fasta --donor k-mer lib --phylo phylogeny.file
```
