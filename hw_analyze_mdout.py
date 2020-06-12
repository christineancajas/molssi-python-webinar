import os
import argparse
import glob

if __name__ == "__main__":


    parser = argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy.")
    parser.add_argument("mdout_file",help="The filepath to the file to be analyzed")
    args = parser.parse_args()

    file_location = args.mdout_file
    
    filehandle = open(file_location)
    
    data = filehandle.readlines() 
    filehandle.close() 

    filename = os.path.basename(args.mdout_file).split('.')[0]
   
    #Loop through the lines to obtain the total energies per step         
    #how to get rid of the last 2 values at the end (not associated with the md simulation)

    etot = []
    for line in data:

        if 'Etot' in line:
            energy_line = line
            etot_words = energy_line.split()
            energy = float(etot_words[2])
            etot.append(energy)

        just_etot = etot[:-2] #omit the last 2
        
    outfile_location = F' {filename}_Etot.txt'
    outfile = open(outfile_location, 'w+')
    
    for value in just_etot:
        outfile.write(f'{value}\n')

    outfile.close()

                