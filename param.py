#Parameter file for create_ic
#This file should be in the same directory as the executable create_ic.py

#ic file
ic = "./ics_lmc_smc_infall.hdf5"

#Accessing arrays

#For PartType1 (halo)
ic_part1_pids = "./ic_arrays/ic_part1_pids.npy"
ic_part1_coord = "./ic_arrays/ic_part1_coord.npy"
ic_part1_vel = "./ic_arrays/ic_part1_vel.npy"
ic_part1_mass = "./ic_arrays/ic_part1_mass.npy"

#For PartType2 (disk)
ic_part2_pids = "./ic_arrays/ic_part2_pids.npy"
ic_part2_coord = "./ic_arrays/ic_part2_coord.npy"
ic_part2_vel = "./ic_arrays/ic_part2_vel.npy"
ic_part2_mass = "./ic_arrays/ic_part2_mass.npy"

#For PartType5 (black hole)
ic_part5_pids = "./ic_arrays/ic_part5_pids.npy"
ic_part5_coord = "./ic_arrays/ic_part5_coord.npy"
ic_part5_vel = "./ic_arrays/ic_part5_vel.npy"
ic_part5_mass = "./ic_arrays/ic_part5_mass.npy"

#Other IC params (for header)
BoxSize = 0
NumFilesPerSnapshot = 1 
NumPart_ThisFile = "./ic_arrays/NumPart.npy" 
NumPart_Total = "./ic_arrays/NumPart.npy"
Redshift = 0



