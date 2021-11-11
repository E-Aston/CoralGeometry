# Geometric measures of corals

Integration of MeshLab with python to compute several geometric measures of individual coral colonies. This is 
split in to two parts - processing of photographs in Metashape to turn these in to 3D reconstructions, as well as 
extracting complexity metrics. These scripts are easy to implement and follow assuming some knowledge of both using
metashape and using a python interpreter / installing modules from the command line. 

Part I: Metashape processing

This script is a downloadable .py file that is run directly from the metashape GUI (graphical user interface).
For every chunk present in the project, it performs end-to-end digitisation of a coral colony according to some
user-input values. Fortunately, these are pop-up boxes that have attached instructions. The only manual step
required of the user is detecting markers and scaling models.

Requirements: Active license for metashape. (optional) Python interpreter (we recommend PyCharm) for inspecting
and editing the python code as required. 

Defaults (and recommended values) for processing are as follows:

Photo quality threshold: <0.35

Alignment quality: High (1)

Dense cloud quality: Medium (2)

Face count for model: High


Part II: Automated metrics extraction

This code automates the extraction of 8 3D complecity metrics from an obj. file.
It loops the below function over every file in a specified folder, saving hours/days/weeks of clicking through
pesky menus. The most efficient way of running this script is to put the .obj file of each coral in to a single
folder, which you refer to in the script. 


Requirements: Meshlab software on PC, and installation of PyMeshlab using pip, installation of os and 
installation of csv

To run the code, you also need the files
"geometric_measures.py", "Clean_Close.mlx" and "Filter_script.mlx" in the current working directory, 
as well as "Geometric measures execute.py", which is 
the executbale script.

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
cm. Note that your models must have been scaled in the software you used to create them for this code to work.

There is only one thing for the user to do to make this code run properly. In "Geometric measures execute.py"
the directory needs to be changed to direct python to the folder where all your .obj files are stored. This folder can
include other file types, it won't break the script - the loop will just ignore all non-.obj files.


NOTE: PyMeshLab is in its infancy and users may run into issues with plugins when trying to call functions. Deleting the plugins
that cause the issue (most likely the Sketchfab one, which is a known issue) enables this script to run.
