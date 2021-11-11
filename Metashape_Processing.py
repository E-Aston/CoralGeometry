'''

This code is intended to be run from the Metashape GUI. As of July 2021, it works with python 3.5 - 3.8. Python 3.9 is
not supported, although this is unlikely to matter for scripts run directly from the GUI.

This script executes over all chunks of data, and expects that there are already multiple chunks in the open project,
each already populated with photographs.

There are several values within the script that are expected to be chosen by the user, which are referred to in
dialogue boxes

In the arguments box, before running the script, be sure to choose a quality threshold below which to disable photos.
The metashape manual recommends 0.5 as a value. In several instances, underwater photographs will be of a lower quality
according to this algorithm due to barrel distortion associated with underwater camera apperatus, as  well as bad
visibility. Thus, we often use 0.35.

'''

import Metashape, sys


doc = Metashape.app.document
chunk = doc.chunk

Metashape.app.messageBox("The script that is about to execute will serially process every chunk in the current project using the same settings. The next 3 dialogue boxes present you with choices based on your computing power, available time and required model quality. Ensure all chunks are populated with the correct photographs.\n\n"
                         "We recommend aligning on high quality and processing dense clouds on medium quality. The face count in final meshes is set to high. Each chunk will be processed using the same settings. Sparse cloud cleaning is automatic, removing your need to be at "
                         "the desk whilst processing is occurring. \n\nPhotographs in each chunk will be disabled automatically based on their quality value. This is set to 0.35 by default. You can change this in the arguments box when running the script if you wish."
                         "\n\n*Please note that because different users have different methods for scaling models (marker types are varied), this script does not provide for marker detection and scale bar placement. This should be done manually at the end of processing.")

Alignquality = Metashape.app.getInt(label ="Pick an alignment quality for your chunks.\nHigh = 1\nMedium = 2\nLow = 4", value=1)
dcquality = Metashape.app.getInt(label ="Pick an dense cloud quality for your chunks.\nHigh = 2\nMedium = 4\nLow = 8", value=4)

scClean = Metashape.app.getFloat(label ="The sparse cloud will be cleaned using 3 iterations of point removal based on reprojection error, projection accuracy and reconstruction "
                                        "uncertainty.\n Each removal will remove the worst x percent of points. Please choose this percentage. We recommend 90-95.", value=95)

for chunk in Metashape.app.document.chunks:
    chunk.analyzePhotos()

    camera = chunk.cameras

    ### Leave the below and above threshold values at 0, they are just a counter ###

    below_threshold = 0
    above_threshold = 0

    # Set threshold value for quality.

    threshold = float(sys.argv[1])

    # Function that returns number of photographs that will be rejected based on user-define threshold

    for camera in chunk.cameras:
        if float(camera.meta["Image/Quality"]) < threshold:
            below_threshold += 1
        else:
            above_threshold += 1

    for camera in chunk.cameras:
        if float(camera.meta["Image/Quality"]) < threshold:
            camera.enabled = False

    '''
    
    For quality of photo matching, the following parameters correspond to metashape's GUI settings:
    
    Low quality = 4
    Medium quality = 2
    High quality = 1
    
    '''

    chunk.matchPhotos(downscale=Alignquality, generic_preselection=True, reference_preselection=True)
    chunk.alignCameras()

    print (" --- Cameras are aligned. Sparse point cloud generated ---")

    points_original = len(chunk.point_cloud.points)

    pre_clean_points = len([p for p in chunk.point_cloud.points if p.valid])

    TARGET_PERCENT = scClean  # percentage of left points

    points = chunk.point_cloud.points
    f = Metashape.PointCloud.Filter()
    f.init(chunk, criterion=Metashape.PointCloud.Filter.ReprojectionError)  # Reprojection Error
    list_values = f.values
    list_values_valid = list()

    for i in range(len(list_values)):

        if points[i].valid:
            list_values_valid.append(list_values[i])

    list_values_valid.sort()
    target = int(len(list_values_valid) * TARGET_PERCENT / 100)
    threshold = list_values_valid[target]
    f.selectPoints(threshold)
    f.removePoints(threshold)

    points = chunk.point_cloud.points

    f = Metashape.PointCloud.Filter()
    f.init(chunk, criterion=Metashape.PointCloud.Filter.ReconstructionUncertainty)
    list_values = f.values
    list_values_valid = list()

    for i in range(len(list_values)):

        if points[i].valid:
            list_values_valid.append(list_values[i])

    list_values_valid.sort()
    target = int(len(list_values_valid) * TARGET_PERCENT / 100)
    threshold = list_values_valid[target]
    f.selectPoints(threshold)
    f.removePoints(threshold)

    points = chunk.point_cloud.points

    f = Metashape.PointCloud.Filter()
    f.init(chunk, criterion=Metashape.PointCloud.Filter.ProjectionAccuracy)
    list_values = f.values
    list_values_valid = list()

    for i in range(len(list_values)):

        if points[i].valid:
            list_values_valid.append(list_values[i])

    list_values_valid.sort()
    target = int(len(list_values_valid) * TARGET_PERCENT / 100)
    threshold = list_values_valid[target]
    f.selectPoints(threshold)
    f.removePoints(threshold)

    chunk.optimizeCameras(fit_f=True, fit_cx=True, fit_cy=True, fit_b1=False, fit_b2=False, fit_k1=True,
                          fit_k2=True, fit_k3=True, fit_k4=False, fit_p1=True, fit_p2=True,
                          fit_corrections=False, adaptive_fitting=False, tiepoint_covariance=False)

    firstit_points = len([p for p in chunk.point_cloud.points if p.valid])

    points = chunk.point_cloud.points
    f = Metashape.PointCloud.Filter()
    f.init(chunk, criterion=Metashape.PointCloud.Filter.ReprojectionError)  # Reprojection Error
    list_values = f.values
    list_values_valid = list()

    for i in range(len(list_values)):

        if points[i].valid:
            list_values_valid.append(list_values[i])

    list_values_valid.sort()
    target = int(len(list_values_valid) * TARGET_PERCENT / 100)
    threshold = list_values_valid[target]
    f.selectPoints(threshold)
    f.removePoints(threshold)

    points = chunk.point_cloud.points

    f = Metashape.PointCloud.Filter()
    f.init(chunk, criterion=Metashape.PointCloud.Filter.ReconstructionUncertainty)
    list_values = f.values
    list_values_valid = list()

    for i in range(len(list_values)):

        if points[i].valid:
            list_values_valid.append(list_values[i])

    list_values_valid.sort()
    target = int(len(list_values_valid) * TARGET_PERCENT / 100)
    threshold = list_values_valid[target]
    f.selectPoints(threshold)
    f.removePoints(threshold)

    points = chunk.point_cloud.points

    f = Metashape.PointCloud.Filter()
    f.init(chunk, criterion=Metashape.PointCloud.Filter.ProjectionAccuracy)
    list_values = f.values
    list_values_valid = list()

    for i in range(len(list_values)):

        if points[i].valid:
            list_values_valid.append(list_values[i])

    list_values_valid.sort()
    target = int(len(list_values_valid) * TARGET_PERCENT / 100)
    threshold = list_values_valid[target]
    f.selectPoints(threshold)
    f.removePoints(threshold)

    secondit_points = len([p for p in chunk.point_cloud.points if p.valid])

    chunk.optimizeCameras(fit_f=True, fit_cx=True, fit_cy=True, fit_b1=False, fit_b2=False, fit_k1=True,
                          fit_k2=True, fit_k3=True, fit_k4=False, fit_p1=True, fit_p2=True,
                          fit_corrections=False, adaptive_fitting=False, tiepoint_covariance=False)

    points = chunk.point_cloud.points
    f = Metashape.PointCloud.Filter()
    f.init(chunk, criterion=Metashape.PointCloud.Filter.ReprojectionError)  # Reprojection Error
    list_values = f.values
    list_values_valid = list()

    for i in range(len(list_values)):

        if points[i].valid:
            list_values_valid.append(list_values[i])

    list_values_valid.sort()
    target = int(len(list_values_valid) * TARGET_PERCENT / 100)
    threshold = list_values_valid[target]
    f.selectPoints(threshold)
    f.removePoints(threshold)

    points = chunk.point_cloud.points

    f = Metashape.PointCloud.Filter()
    f.init(chunk, criterion=Metashape.PointCloud.Filter.ReconstructionUncertainty)
    list_values = f.values
    list_values_valid = list()

    for i in range(len(list_values)):

        if points[i].valid:
            list_values_valid.append(list_values[i])

    list_values_valid.sort()
    target = int(len(list_values_valid) * TARGET_PERCENT / 100)
    threshold = list_values_valid[target]
    f.selectPoints(threshold)
    f.removePoints(threshold)

    points = chunk.point_cloud.points

    f = Metashape.PointCloud.Filter()
    f.init(chunk, criterion=Metashape.PointCloud.Filter.ProjectionAccuracy)
    list_values = f.values
    list_values_valid = list()

    for i in range(len(list_values)):

        if points[i].valid:
            list_values_valid.append(list_values[i])

    list_values_valid.sort()
    target = int(len(list_values_valid) * TARGET_PERCENT / 100)
    threshold = list_values_valid[target]
    f.selectPoints(threshold)
    f.removePoints(threshold)

    thirdit_points = len([p for p in chunk.point_cloud.points if p.valid])
    chunk.optimizeCameras(fit_f=True, fit_cx=True, fit_cy=True, fit_b1=True, fit_b2=True, fit_k1=True,
                          fit_k2=True, fit_k3=True, fit_k4=True, fit_p1=True, fit_p2=True,
                          fit_corrections=False, adaptive_fitting=False, tiepoint_covariance=False)


    '''
    
    For quality of dense cloud, the downscale factor is the factor by which the image quality is reduced:
    Low quality = 8
    Medium quality = 4
    High quality = 2
    
    '''

    chunk.buildDepthMaps(downscale=dcquality, filter_mode=Metashape.MildFiltering)
    chunk.buildDenseCloud()

    print("--- Dense cloud built. Moving on to 3D model generation ---")

    chunk.buildModel(surface_type=Metashape.Arbitrary, interpolation=Metashape.EnabledInterpolation,
                     face_count=Metashape.HighFaceCount)
    chunk.buildUV(mapping_mode=Metashape.GenericMapping)
    chunk.buildTexture(blending_mode=Metashape.MosaicBlending, texture_size=4096)


    print("--- Processing finished ---")

    chunk.buildOrthomosaic(fill_holes=True)

print("Script finished")

Metashape.app.messageBox("Processing finished. \n The next step is to manually trim models to isolate your focal object. Following this you can export the .obj file to extract complexity metrics.")
