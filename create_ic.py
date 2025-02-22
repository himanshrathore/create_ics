#Code to create a Gadget4 compatible N-body HDF5 initial condition file
#Author: Himansh Rathore, July 2023
#Last updated: Feb 13, 2025 by Himansh Rathore

import numpy as np
import h5py
import os
import param #parameter file param.py should be in the same directory as the script combine_ics.py

print('Starting code...')

#Accessing arrays

#For PartType0 (gas)
if('PartType0' in param.part_types):
    ic_part0_pids = np.load(param.ic_part0_pids)
    ic_part0_coord = np.load(param.ic_part0_coord)
    ic_part0_vel = np.load(param.ic_part0_vel)
    ic_part0_mass = np.load(param.ic_part0_mass)

#For PartType1 (halo)
if('PartType1' in param.part_types):
    ic_part1_pids = np.load(param.ic_part1_pids)
    ic_part1_coord = np.load(param.ic_part1_coord)
    ic_part1_vel = np.load(param.ic_part1_vel)
    ic_part1_mass = np.load(param.ic_part1_mass)

#For PartType2 (disk)
if('PartType2' in param.part_types):
    ic_part2_pids = np.load(param.ic_part2_pids)
    ic_part2_coord = np.load(param.ic_part2_coord)
    ic_part2_vel = np.load(param.ic_part2_vel)
    ic_part2_mass = np.load(param.ic_part2_mass)

#For PartType5 (black hole)
if('PartType5' in param.part_types):
    ic_part5_pids = np.load(param.ic_part5_pids)
    ic_part5_coord = np.load(param.ic_part5_coord)
    ic_part5_vel = np.load(param.ic_part5_vel)
    ic_part5_mass = np.load(param.ic_part5_mass)

#Other IC params (for header)
BoxSize = param.BoxSize
NumFilesPerSnapshot = param.NumFilesPerSnapshot
NumPart_ThisFile = np.load(param.NumPart_ThisFile)
NumPart_Total = np.load(param.NumPart_Total)
Redshift = param.Redshift

#ic file
ic = param.ic

#check if the ic file already exists
if(os.path.exists(ic)):
    #removing file
    os.remove(ic)
    print('IC file already exists. Will remove it and create a new one.')

f = h5py.File(ic, 'w')
print('Starting to create IC: ', ic)

N_part_types = 6 #maximum number of gadget particle types
print('Assuming 6 particle types at maximum')

#header of IC file
head = f.create_group('/Header')

head.attrs['BoxSize'] = BoxSize
head.attrs['MassTable'] = np.zeros(N_part_types) #since particles of a given type can have different masses
head.attrs['NumFilesPerSnapshot'] = NumFilesPerSnapshot
head.attrs['NumPart_ThisFile'] = NumPart_ThisFile
head.attrs['NumPart_Total'] = NumPart_Total
head.attrs['Redshift'] = Redshift
head.attrs['Time'] = 0.0 #since this is the ic

print('Creating header of combined ic...')

if('PartType0' in param.part_types):
    #creating PartType0 (gas)

    #creating ParticleIDs

    dset = f.create_dataset('/PartType0/ParticleIDs', shape = ic_part0_pids.shape, dtype = ic_part0_pids.dtype, data = ic_part0_pids)

    print("Creating particle IDs of PartType0...")

    #creating coordinates

    dset = f.create_dataset('/PartType0/Coordinates', shape = ic_part0_coord.shape, dtype = ic_part0_coord.dtype, data = ic_part0_coord)

    print("Creating coordinates of PartType0...")

    #creating velocities

    dset = f.create_dataset('/PartType0/Velocities', shape = ic_part0_vel.shape, dtype = ic_part0_vel.dtype, data = ic_part0_vel)

    print("Creating velocities of PartType0...")

    #creating masses

    dset = f.create_dataset('/PartType0/Masses', shape = ic_part0_mass.shape, dtype = ic_part0_mass.dtype, data = ic_part0_mass)

    print("Creating masses of PartType0...")
    
if('PartType1' in param.part_types):
    #creating PartType1 (DM halo)

    #creating ParticleIDs

    dset = f.create_dataset('/PartType1/ParticleIDs', shape = ic_part1_pids.shape, dtype = ic_part1_pids.dtype, data = ic_part1_pids)

    print("Creating particle IDs of PartType1...")

    #creating coordinates

    dset = f.create_dataset('/PartType1/Coordinates', shape = ic_part1_coord.shape, dtype = ic_part1_coord.dtype, data = ic_part1_coord)

    print("Creating coordinates of PartType1...")

    #creating velocities

    dset = f.create_dataset('/PartType1/Velocities', shape = ic_part1_vel.shape, dtype = ic_part1_vel.dtype, data = ic_part1_vel)

    print("Creating velocities of PartType1...")

    #creating masses

    dset = f.create_dataset('/PartType1/Masses', shape = ic_part1_mass.shape, dtype = ic_part1_mass.dtype, data = ic_part1_mass)

    print("Creating masses of PartType1...")
    
if('PartType2' in param.part_types):
    #creating PartType2 (stellar disk)

    #creating ParticleIDs

    dset = f.create_dataset('/PartType2/ParticleIDs', shape = ic_part2_pids.shape, dtype = ic_part2_pids.dtype, data = ic_part2_pids)

    print("Creating particle IDs of PartType2...")

    #creating coordinates

    dset = f.create_dataset('/PartType2/Coordinates', shape = ic_part2_coord.shape, dtype = ic_part2_coord.dtype, data = ic_part2_coord)

    print("Creating coordinates of PartType2...")

    #creating velocities

    dset = f.create_dataset('/PartType2/Velocities', shape = ic_part2_vel.shape, dtype = ic_part2_vel.dtype, data = ic_part2_vel)

    print("Creating velocities of PartType2...")

    #creating masses

    dset = f.create_dataset('/PartType2/Masses', shape = ic_part2_mass.shape, dtype = ic_part2_mass.dtype, data = ic_part2_mass)

    print("Creating masses of PartType2...")
    
if('PartType5' in param.part_types):
    #creating PartType5 (central BHs)

    #creating ParticleIDs

    dset = f.create_dataset('/PartType5/ParticleIDs', shape = ic_part5_pids.shape, dtype = ic_part5_pids.dtype, data = ic_part5_pids)

    print("Creating particle IDs of PartType5...")

    #creating coordinates

    dset = f.create_dataset('/PartType5/Coordinates', shape = ic_part5_coord.shape, dtype = ic_part5_coord.dtype, data = ic_part5_coord)

    print("Creating coordinates of PartType5...")

    #creating velocities

    dset = f.create_dataset('/PartType5/Velocities', shape = ic_part5_vel.shape, dtype = ic_part5_vel.dtype, data = ic_part5_vel)

    print("Creating velocities of PartType5...")

    #creating masses

    dset = f.create_dataset('/PartType5/Masses', shape = ic_part5_mass.shape, dtype = ic_part5_mass.dtype, data = ic_part5_mass)

    print("Creating masses of PartType5...")
    
print("Done!")

#end
