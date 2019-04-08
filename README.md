# FermentKEGGRest
Pulls pathway information from KEGG

## pull.py 
    # collects data from KEGG
    # Uses KEGG API via Biopython
    # Formats as follows:
    # [ORGANISM]  [PATHWAY] [ENZYME #]  [1 | 0]
    # 0 means that bacteria has no KEGG ortholog for that enzyme
    # 1 means that bacteria has KEGG ortholog for that enzyme
To run this program, simply download this; then either
    
 * Run in a Python IDE
 * or if in an SSH client, use the command

    # python pull.py

## toSIF.py 
    # transform data .txt file to .sif networks per metabolic pathways
    # Simple file parser that formats into .sif
    # [NODE 1] [EDGE TYPE] [NODE 2]
    # Three types of networks were made
      # Bacteria to Enzyme
      # Enzyme to Pathway
      # Bacteria to Enzyme to Pathway
To run this program, simply download this; then either
    
  * Run in a Python IDE
  * or if in an SSH client, use the command
    
        python pull.py

Must have the .txt file formatted as:
[ORGANISM]  [PATHWAY] [ENZYME #]  [1 | 0]
  
## counter.py 
    # counts the numbers of edges per bacteria per pathway divided by total enzymes in the pathway
To run this program, simply download this; then either
    
 * Run in a Python IDE
 * or if in an SSH client, use the command
        
        python pull.py

Must have .sif file
