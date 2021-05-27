'''

The following python script is designed to automate elements of computing geometric measures of coral colonies.
Its use requires the installation of PyMeshlab using pip. To run the code, you need the files "Filter_script.mlx"
and "geometric_measures.py" in the current working directory.

The code runs a series of filters using Meshlab and returns the following as a .csv file called
"Geometric Measures.csv" in the current folder:

File_Path : File path to the original input mesh. Identifies each coral in the file
Vol: Volume of first mesh
CVH_Vol: Volume of minimum bounding convex hull enclosing original mesh
ASR: Absolute spatial refuge. Volumetric measure of shelter capacity of colony
PrOcc: Proportion Occupied. Proportion of the convex hull occupied by the coral lying inside it. Measures compactness.
Surface_Area: 3D surface area of input colony (not the convex hull)
SSF: Shelter size factor. Ratio of ASR to 3D surface area. Measure of size structure of refuges.

Unit measurements depend on the input mesh. Transformations must be carried out by the user to get to square and cubic
cm.

There is only one thing for the user to do to make this code work. In "Geometric measures execute.py" the directory needs
to be changed to direct python to the folder where all your .obj files are stored. This folder can include other file types, 
it won't break the script - the loop will just ignore all non-.obj files.


'''

import os
from geometric_measures import geometric_measures
import csv

Variable_names = ['File_Path', "Vol", "CVH_Vol", "ASR", "PrOcc", "Surface_Area", "SSF", "SAVR"]  # Sets up a CSV with variable
# names in current dir.
with open("Geometric Measures.csv", "w", newline='') as f:
    write = csv.writer(f)
    write.writerow(Variable_names)

directory = "Your_file_path"  # Sets WD where obj files are stored - INPUT NEEDED
for filename in os.listdir(directory):
    if filename.endswith(".obj"):
        geometric_measures(os.path.join(directory, filename))
    else:
        continue

