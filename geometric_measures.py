directory = "C:/Users/ruth/Documents/objs/"  # Folder where the obj files are - CHANGE REQUIRED

def geometric_measures (file):

    import pymeshlab
    import csv


    ms = pymeshlab.MeshSet()

    ms.load_new_mesh(file)  # Loads a mesh from input folder
    ms.load_filter_script('Filter_script.mlx')  # Loads the filter script (this one cleans mesh and makes convex hull)
    ms.apply_filter_script()  # Applies script

    ms.set_current_mesh(0)  # Makes the current mesh the original
    dict =(ms.compute_geometric_measures())  # Compute measures of original mesh
    mesh_volume = dict['mesh_volume']
    mesh_sa = dict ['surface_area']

    ms.set_current_mesh(1)  # Sets convex hull as current mesh
    dict =(ms.compute_geometric_measures())  # Compute measures of convex hull
    cvh_volume = dict['mesh_volume']  # Assigns mesh volume to variable cvh_volume

    ASR = (cvh_volume - mesh_volume) # Basic calculation for ASR
    PrOcc = (mesh_volume / cvh_volume)
    SSF = (ASR / mesh_sa)

    value_list = [str(file), mesh_volume, cvh_volume, ASR, PrOcc, mesh_sa, SSF]

    with open("Geometric Measures.csv", "a", newline='') as f:
        write = csv.writer(f)
        write.writerow(value_list)





