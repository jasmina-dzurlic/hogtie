# HoGTIE (Horizontal Gene Transfer Identification Engine)

### What task/goal will the project accomplish and why is this useful?
First thought to only occur widely in prokaryotic organisms, recent work has shown the prevalence of horizontal gene transfer (HGT) across the tree of life. HoGTIE uses a combination of k-mer-based and phylogenetic-based comparisons to identify genomic regions and sequences that contain horizontal gene transfer (HGT) in a recipient species. 

  
### What type of data/input will a user provide to the program? Where will the data come from?
HoGTIE is sister to the suite of tools [`k-mer kit`](https://github.com/eaton-lab/kmerkit). To run HoGTIE, the user will provide a phylogeny (branch lengths, topology) that includes the recipient and potential donor species. The user will also provide raw genomic sequencing data for all species along the tips of the provided phylogeny. These sequences will be parsed into k-mer presence/absence matrix by k-mer kit. This matrix and the phylogeny are the basic inputs into HoGTIE.

### How will a user interact with the program?
HoGTIE can be accessed as a CLI or API program. Assuming a matrix has been produced using `kmerkit`, the user need only provide the matrix and phylogeny. *Should I call and run kmerkit inside my program? If so, maybe it makes the most sense for the user to provide a file that contains a list of the sequence data they want to use. This list could be url's to access fasta files on NCBI or a direction to a file on the local device*

```
#running HoGTIE example
hogtie --character_states matrix.file --phylo phylogeny.file
```
### What type of output will the program produce (e.g., text, plots)?
A primary output of this program will be a file containing the reads (or contigs via kassemble) that are likely to contain instances of HGT. If the recipient species has an assembled genome, these reads can be mapped to that genome to identify regions of the genome where HGT took place. Without an assembled genome, these reads/contigs can inputs into BLAST and the potential gene and function can be ascertained. Another output will be a [`toytree`](https://github.com/eaton-lab/toytree) object that visualizes where the HGT took place along the input tree.

### What other tools currently exist to do this task, or something similar?
There are currently a number of methods that focus on identifying horizontal gene transfer in prokaryotic species. These methods are either alignment-based and k-mer-based, where the k-mer-based methods are performed through calculation of a number of distance statistics through comparison of groups of k-mers. There are tools that identify plasmid sequences including [`PlasFlow`](https://github.com/smaegol/PlasFlow) and [`Recyler`](https://github.com/Shamir-Lab/Recycler). Alignment-based methods have been readily applied to eukaryotic species as well: recipient genomes are aligned to putative donor genomes to identify genes within the recipient genome that are more similar to the donor than the recipient. Such approaches can include only a small number of potential donors because they are computationally intensive, and rely on at least partially assembled genomes, which are not available for all species we may be interested in.

HoGTIE draws on both methodologies, decreasing computational intensity through a k-mer identification, yet maintaining a comparative approach through the inclusion of phylogenetic-based comparison. HoGTIE therefore allows for a comparison of the recipient sequences to a wider body of putative donor sequences, mapping of HGT events to the recipient genome itself, and visualization of HGT along an evolutionary tree. 