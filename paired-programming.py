# Git Collab Assignment

 ## Goal of the project: Is it clear to you from the proposal.md how the goal can be accomplished using Python and the specified packages?

 It is clear from the proposal.md that Horizontal Gene Transfer Identification Engine (HoGTIE) will use a blend of modules from kmerkit, ipcoal, and toytree to idenitify genomic regions and sequences that contain HGT in recent sequences. 


 ## The Data: Is it clear to you from the proposal.md what the data for this project is, or will look like?

It is evident that hoGTIE will require a phylogeny and genetic data as inputs. The user will provide raw sequence data for all species along the tips of the provided phylogeny. I have a couple of questions about the sequence data. What kind of sequence data is allowed as input? RAD-seq? WGS? Illumina? Nanopore? Is there a preferred type of sequence data for this analysis? Is there a preferred type of genetic file type for this input (i.e fasta, fastq, BED, BAM, SAM)? What type of file is the phylogeny presented in? How are branch lenths and tips represented in this file? What does the k-mer presence/absence matrix file look like? Is it a simple binary of 0 and 1's? An example in the proposal may help visiualize how this data input may appear. 

Rachel and I discussed output data in our meeting during class. A visualization of where signatures of horizontal gene transfer is present in the genome will be a very useful asset to this tool. Potenitally a line graph across chromosomes of a scatter plot using matplotlib or toytree will aid in visualizing the output data. 


 ## Does the current code include a proper skeleton (pseudocode) for starting this project?

The current code is in development towards a pseudcode for the project. The code for the phylogeny is quite clear and developed. The code for the genetic input from kmerkits needs more input once input modules are complete. 


 ## What can this code do so far?

The pagel.py code uses toytree and numpy to assign liklihood values to tree tips and calculates the conditional likelihood of character states at each node then runs Felsenstein's pruning algorithm on an input tree, given instantaneous transition rates alpha and beta. After running the pruning algorithm, a likelihood score is assigned to the characters states at each node to create the phylogeny. 


 ## Given the project description, what are some individual functions that could be written to accomplish parts of this goal?

Given the project descript, the module I am developing, Kassemble, can help assemble regions of horizonatal gene transfer. My current understanding of the project and what is needed that I can help contribute to is the visualization of the signatures of horizontal gene transfer and contig assembly. This can be done with a function such as def_see_genome_ that will call kassemble and use toyplot to visiual outputs of horizontal gene transfer.  

 ## Code contributions/ideas:
So far I added information to the __init__.py file. Then I added a z-score_plot.py file that uses a random numpy array as test data and calls the data in a def def_see_genome_ that uses toyplot to visiualize data. This test dataset and plot can be used later with real data to visualize regions on the genome of detected horizontal gene transfer. 

Ideas for moving forward would be as mentioned before, focusing on user-interation via visualization and types of input data that this program will require, paticularly that of raw sequence data. 
