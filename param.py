#Parameter file for create_ic
#This file should be in the same directory as the executable create_ic.py

#target ic file
ic = "<path>"

#particle types (mention which ones in the form of a list)
'''
Currently supported particle types:
PartType0 -> gas
PartType1 -> halo
PartType2 -> disk
PartType5 -> black hole
'''
part_types = ['PartType0', 'PartType1', 'PartType2', 'PartType5']

#Accessing arrays - these should be numpy arrays. Position and velocity arrays should have dimension (3, N_particles).

#For PartType0 (gas) - particle ids, positions, velocities, masses
ic_part0_pids = "<path>"
ic_part0_coord = "<path>"
ic_part0_vel = "<path>"
ic_part0_mass = "<path>"

#For PartType1 (halo) - particle ids, positions, velocities, masses
ic_part1_pids = "<path>"
ic_part1_coord = "<path>"
ic_part1_vel = "<path>"
ic_part1_mass = "<path>"

#For PartType2 (disk) - particle ids, positions, velocities, masses
ic_part2_pids = "<path>"
ic_part2_coord = "<path>"
ic_part2_vel = "<path>"
ic_part2_mass = "<path>"

#For PartType5 (black hole) - particle ids, positions, velocities, masses
ic_part5_pids = "<path>"
ic_part5_coord = "<path>"
ic_part5_vel = "<path>"
ic_part5_mass = "<path>"

#Other IC params (for header)
BoxSize = 0
NumFilesPerSnapshot = 1 
NumPart_ThisFile = "<path>" #Should be a numpy array of the form: [0, N_PartType1, N_PartType2, 0, 0, N_PartType5]
NumPart_Total = "<path>" #Should be same as "NumPart_ThisFile"
Redshift = 0

