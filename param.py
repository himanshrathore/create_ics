#Parameter file for create_ic
#This file should be in the same directory as the executable create_ic.py

#target ic file
ic = "./ics_lmc_smc_infall.hdf5"

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
ic_part0_pids = "./ic_arrays/ic_part0_pids.npy"
ic_part0_coord = "./ic_arrays/ic_part0_coord.npy"
ic_part0_vel = "./ic_arrays/ic_part0_vel.npy"
ic_part0_mass = "./ic_arrays/ic_part0_mass.npy"

#For PartType1 (halo) - particle ids, positions, velocities, masses
ic_part1_pids = "./ic_arrays/ic_part1_pids.npy"
ic_part1_coord = "./ic_arrays/ic_part1_coord.npy"
ic_part1_vel = "./ic_arrays/ic_part1_vel.npy"
ic_part1_mass = "./ic_arrays/ic_part1_mass.npy"

#For PartType2 (disk) - particle ids, positions, velocities, masses
ic_part2_pids = "./ic_arrays/ic_part2_pids.npy"
ic_part2_coord = "./ic_arrays/ic_part2_coord.npy"
ic_part2_vel = "./ic_arrays/ic_part2_vel.npy"
ic_part2_mass = "./ic_arrays/ic_part2_mass.npy"

#For PartType5 (black hole) - particle ids, positions, velocities, masses
ic_part5_pids = "./ic_arrays/ic_part5_pids.npy"
ic_part5_coord = "./ic_arrays/ic_part5_coord.npy"
ic_part5_vel = "./ic_arrays/ic_part5_vel.npy"
ic_part5_mass = "./ic_arrays/ic_part5_mass.npy"

#Other IC params (for header)
BoxSize = 0
NumFilesPerSnapshot = 1 
NumPart_ThisFile = "./ic_arrays/NumPart.npy" #Should be a numpy array of the form: [0, N_PartType1, N_PartType2, 0, 0, N_PartType5]
NumPart_Total = "./ic_arrays/NumPart.npy" #Should be same as "NumPart_ThisFile"
Redshift = 0



