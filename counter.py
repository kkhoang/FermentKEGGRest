# This program takes .sif files and counts a modified
# edge density

filepaths = ['bacteria_enzyme_map00010.sif', 'bacteria_enzyme_map00020.sif', 'bacteria_enzyme_map00051.sif', 'bacteria_enzyme_map00620.sif', 'bacteria_enzyme_map00720.sif', 'bacteria_enzyme_map00910.sif']

# Read each bacteria to enzyme .sif file and calculate
for filepath in filepaths:
  bacteria = {}
  enzyme = {}
  # Count the number of bacteria-enzyme edge
  with open(filepath) as fp:
    line = fp.readline()
    while line:
      bac, be, enz = line.rstrip('\n').split(' ')
      # Count number of edges bacteria has
      if bac in bacteria:
        bacteria[bac] += 1
      else:
        bacteria[bac] = 1
      # Count number of edges enzyme has
      if enz in enzyme:
        enzyme[enz] += 1
      else:
        enzyme[enz] = 1
      line = fp.readline()
  # Store value (# of enzymes a bacteria has/# of enzymes in pathway)
  # also store the number of connections an enzyme has
  f = open('a' + filepath[:-4] + '.txt', 'w')
  for bac in bacteria:
    print(str(bacteria[bac]/(len(enzyme))))
    f.write(str(bacteria[bac]/len(enzyme)) + '\n')
  for enz in enzyme:
    f.write(enz + '\t' + str(enzyme[enz]) + '\n')
  print(len(enzyme))
  f.close()