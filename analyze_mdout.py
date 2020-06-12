import os
import argparse

# Tell argparse to handle arguments
parser = argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy")

# Tell argparse what arguments to expect ie. the user is going to give us a path for the file and description of this argument
parser.add_argument("path", help="The filepath to the file to be analyzed.")

#Get arguments from the user (ie. args will contain the arguments)
args = parser.parse_args()

filename = args.path #to get value of the argument "path" ie. the path for the file
f = open(filename, 'r')

# Read the data in the file.
data = f.readlines()
f.close()

# Open a file for writing
base_filename = filename.split('.')  
base_filename = base_filename[0]
output_filename = F'{base_filename}_Etot.txt'

f_write = open(output_filename, 'w+')

print(F'Writing output to {output_filename}') #this new file most like be saved in the same folder as the input file bc filename is the whole path ie. data/03_prod.mdout so newfile will also be data/newfile path

f_write.write('Total Energy\n')

#creat empty list
etot = []

# Loop through lines in the file.
for line in data:
    split_line = line.split()
    
    # Get information from the line
    if 'Etot' in line:
        etot.append(split_line[2]) #append all the energies into etot

etot = etot[:-2] #overwrite and slice that includes everything but not including the last 2 values

for energy in etot:
    f_write.write(F'{energy}\n')
        
f_write.close()