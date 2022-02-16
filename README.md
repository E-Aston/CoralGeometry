NOTE: Version control has been updated and checked for Python 3.10 and pymeshlab 2021.01 (As of Feb 2022 the most 
up-to-date version of both packages). Installation instructions are reflective of this. 

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

All you need to do is download the script "Metashape_Processing.py", and run it from inside Metashape. The process
is guided at the beginning then applies the chosen settings to all chunks in the project. To set it up correctly, 
just populate the document with photos of colonies, each one of these added as a separate chunk. 

Defaults (and recommended values) for processing are as follows:

Photo quality threshold: <0.35

Alignment quality: High (1)

Dense cloud quality: Medium (4)

Face count for model: High


Part II: Automated metrics extraction

This code automates the extraction of 10 3D complexity metrics from an obj. file.
It loops the function over every file in a specified folder, saving hours/days/weeks of clicking through
pesky menus. The most efficient way of running this script is to put the .obj file of each coral in to a single
folder, which you refer to in the script. (instructions are embedded)


Requirements: Python interpreter (we recommend PyCharm), installation of PyMeshlab using pip.

To run the code, you also need the files
"Clean_Close.mlx" and "Filter_script.mlx" in the current working directory, 
as well as "Geometric measures execute.py", which is the executbale script.

INSTRUCTIONS:

Install python (ver 3.6 or above will work but we assume a fresh installation). Do so directly from the Python website. 
https://www.python.org/downloads/

When installing, ensure to check the box entitled "Add Python 3.XX to PATH" or nothing will work without manual intervention. 
pip (the package responsible for installing other packages) comes installed by default. We will use this to install
the dependencies for the script. Open the command prompt terminal (press windows key, then type cmd to find it). 

paste the following to install pymeshlab

pip install pymeshlab

with this installed, the package will run. The other dependencies, os and csv, are pre-installed with python. 

To run the code, a python interpreter is needed. We recommend the use of PyCharm, a freely available integrated development engine (IDE)
capable of running the code. This software comes with installation and setup instructions for first time users which may vary between 
systems so we do not provide instructions on how to install here. Note that any interpreter can be used by those familiar with python. 

The code runs a series of filters using Meshlab and returns the following as a .csv file called
"Geometric Measures.csv" in the current working directory:

File_Path : File path to the original input mesh. Identifies each coral in the file

Vol: Volume of first mesh (the coral)

CVH_Vol: Volume of minimum bounding convex hull enclosing original mesh

ASR: Absolute spatial refuge. Volumetric measure of shelter capacity (interstitial space) of the object. Calculation : CVH_Vol - Vol = ASR

PrOcc: Proportion Occupied. Proportion of the convex hull occupied by the coral lying inside it. Measures compactness. Calculation: Vol / CVH_Vol = PrOcc

Surface_Area: 3D surface area of input colony (not the convex hull)

SSF: Shelter size factor. Ratio of ASR to 3D surface area. Measure of size structure of refuges. Calculation: ASR / Surface_area = SSF

Unit measurements depend on the input mesh. Transformations must be carried out by the user to get to square and cubic
cm. Note that your models must have been scaled in the software you used to create them for this code to work.

There is only one thing for the user to do to make this code run properly. In "Geometric measures execute.py"
the directory needs to be changed to direct python to the folder where all your .obj files are stored. This folder can
include other file types, it won't break the script - the loop will just ignore all non-.obj files.

