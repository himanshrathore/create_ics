# create_ics
Create a Gadget-4 compatible HDF5 N-body initial conditions file directly from particle arrays.

# Author
Himansh Rathore, July 2023

# Usage:
The parameter file should be in the same directory as the executable "create_ic.py" and should have the name "param.py". Then, directly execute "create_ic.py" using python3.

Example:
<br>
python3 ./create_ic

# Parameter file:
See the supplied "param.py" for instructions.

# Supported particle types:
Currently, the following gadget particles types are supported: <br>
PartType0 -> gas <br>
PartType1 -> dark matter <br>
PartType2 -> stellar disk <br>
PartType5 -> black hole <br> 
