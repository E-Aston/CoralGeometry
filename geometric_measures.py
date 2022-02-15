def geometric_measures (file):

    import pymeshlab
    import csv


    ms = pymeshlab.MeshSet()

    ms.load_new_mesh(file)  # Loads a mesh from input folder


    ms.set_current_mesh(0)  # Makes the current mesh the original
    dict =(ms.compute_geometric_measures())  # Compute measures of original mesh
    mesh_sa = dict['surface_area'] # Assigns variable name

    ms.load_filter_script('Clean_Close.mlx')  # Loads the filter script (this one cleans mesh and closes holes)
    ms.apply_filter_script()  # Applies script

    dict =(ms.compute_geometric_measures())  # Compute measures of closed mesh
    mesh_volume = dict['mesh_volume']  # Assigns mesh volume to variable mesh_volume
    
    boundingbox = ms.current_mesh().bounding_box()
    width = boundingbox.dim_x()


    height = boundingbox.dim_z()

    ms.load_filter_script('Filter_script.mlx')  # Loads the filter script (this one makes a convex hull)
    ms.apply_filter_script()  # Applies script

    ms.set_current_mesh(1)  # Sets convex hull as current mesh
    dict = (ms.compute_geometric_measures())  # Compute measures of convex hull
    cvh_volume = dict ['mesh_volume'] # Assigns variable name

    ASR = (cvh_volume - mesh_volume) # Basic calculation for ASR
    PrOcc = (mesh_volume / cvh_volume) # Proportion of cvh occupied by mesh (compactness)
    SSF = (ASR / mesh_sa) # Shelter size factor (fragmentation of habitat)

    value_list = [str(file), mesh_sa, mesh_volume, cvh_volume, ASR, PrOcc, SSF, width, height]

    with open("Geometric Measures.csv", "a", newline='') as f:
        write = csv.writer(f)
        write.writerow(value_list)



