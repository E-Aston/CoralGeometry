# Geometric measures of corals

Integration of MeshLab with python to compute several geometric measures of individual coral colonies
The contained python script is designed to automate elements of computing geometric measures of coral colonies.
It loops the below function over every file in a specified folder, saving hours/days/weeks of clicking through
pesky menus.


Requirements: Meshlab software on PC, and installation of PyMeshlab using pip 

To run the code, you need the files "Filter_script.mlx"
and "geometric_measures.py" in the current working directory, as well as "Geometric measures output.py", which is 
where you execute the script.

The code runs a series of filters using Meshlab and returns the following as a .csv file called
"Geometric Measures.csv" in the current working directory:

File_Path : File path to the original input mesh. Identifies each coral in the file

Vol: Volume of first mesh

CVH_Vol: Volume of minimum bounding convex hull enclosing original mesh

ASR: Absolute spatial refuge. Volumetric measure of shelter capacity of colony

PrOcc: Proportion Occupied. Proportion of the convex hull occupied by the coral lying inside it. Measures compactness.

Surface_Area: 3D surface area of input colony (not the convex hull)

SSF: Shelter size factor. Ratio of ASR to 3D surface area. Measure of size structure of refuges.

Unit measurements depend on the input mesh. Transformations must be carried out by the user to get to square and cubic
cm.

There is only one thing for the user to do to make this code work. In both "Geometric measures output.py"
the directory needs to be changed to direct python to the folder where all your .obj files are stored. This folder can
include other file types, it won't break the script - the loop will just ignore all non-.obj files.


NOTE: PyMeshLab is in its infancy and users may run into issues with plugins when trying to call functions. Deleting the plugins
that cause the issue (most likely the Sketchfab one, which is a known issue) enables this script to run.
