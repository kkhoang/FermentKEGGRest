# This is a script that collects information from KEGG

from Bio.KEGG import REST

# Lists of KEGG pathways and bacteria 
pathway_list = ['map00010', 'map00020', 'map00051', 'map00620', 'map00720', 'map00910']
organism_list = ['lla', 'lpl', 'lbr', 'lec', 'lki', 'llf', 'lmm', 'ctyk', 'thl', 'wcb', 'bli', 'ece', 'sab', 'lsa', 'hsl']

# Dictionary of lists for each pathways' enzymes' ec number

pathway_ec = {}
# Dictionary of lists of enzymes a bacteria has in KEGG pathway
organism_enzymes = {}

# Populate dictionary with the organism list
for organism in organism_list:
    organism_enzymes[organism] = {}

# Populate dictionary with lists of enzymes in that
# pathway
for pathway in pathway_list:
    ec_read = REST.kegg_link('ec', pathway).read()
    pathway_ec[pathway] = []
    for line in ec_read.rstrip().split('\n'):
        path, ec = line.split('\t')
        pathway_ec[pathway].append(ec[3:])

count = 0 
# Go through each pathway and collect all the orthologs
for pathway in pathway_list:
    print(pathway)
    orthology_read = REST.kegg_link('ko', pathway).read()
    # For each ortholog, find the ec number and if 
    # an organism has the gene for it
    for line in orthology_read.rstrip().split('\n'):
        pathway, ortholog = line.split('\t')
        to_ec = REST.kegg_link('ec', ortholog[3:]).read()
        print(ortholog)
        if len(to_ec) > 6:
	    for entry in to_ec.rstrip().split('\n'):
	        ta, ec = entry.split('\t')
                ec = ec[3:]
                print(ec)
	        # Link the ortholog to genes
                to_genes = REST.kegg_link('genes', ortholog[3:]).read()
                # Read through entire REST result and see if organism is there - most time consuming step
	        if ec not in organism_enzymes[organism]:
		    organism_enzymes[organism][ec] = 0
                for mine in to_genes.rstrip().split('\n'):
                    ko, gene = mine.split('\t')
            	    # Loop through each organism and check
        	    for organism in organism_list:
        	        if organism in gene[:len(organism)]:
        	            organism_enzymes[organism][ec] = 1
                            count += 1

# Save information as .txt file, formatted as:
# [ORGANISM]    [PATHWAY] [EC]  [1 | 0]
f = open("rest.txt", "w")
for organism in organism_list:
    for pathway in pathway_ec:
        for ec in pathway_ec[pathway]:    
            if ec in organism_enzymes[organism]:
	        f.write(organism + '\t' + pathway + '\t' + ec + '\t' + str(organism_enzymes[organism][ec]) + '\n')
            else:
                f.write(organism + '\t' + pathway + '\t' + ec + '\t' + '0\n')
