# This script transforms the data collection .txt
# file to a .sif one

pathway_list = ['map00010', 'map00020', 'map00051', 'map00620', 'map00720', 'map00910']

# Splits all the data based on pathway
bac_enz_files = {} # Bacteria-Enzyme networks
all_inf_files = {} # Tripartite networks 
for pathway in pathway_list:
    bac_enz_files[pathway] = open("bacteria_enzyme_%s.sif" % pathway, "w")
    all_inf_files[pathway] = open("all_nodes_%s.sif" % pathway, "w")
# Enzyme-pathway networks
enz_path = open("enzyme_pathway.sif", "w")
all_inf = open("all_nodes.sif", "w")

# Write to here
filepath = "rest.txt"
with open(filepath) as fp:
    line = fp.readline()
    while line:
        bac, path, enz, boo = line.split('\t')
        print(bac + ' ' + path + ' ' + enz + ' ' + boo)
        if int(boo) == 1:
            bac_enz_files[path].write(bac + ' be ' + enz + '\n')
            all_inf_files[path].write(bac + ' be ' + enz + '\n')
        if bac == 'lla':
            enz_path.write(enz + ' ep ' + path + '\n')
            all_inf.write(enz + ' ep ' + path + '\n')
        all_inf_files[path].write(enz + 'ep' + path + '\n')
	line = fp.readline()

for pathway in pathway_list:
    bac_enz_files[pathway].close()
    all_inf_files[pathway].close()
enz_path.close()
all_inf.close()            
