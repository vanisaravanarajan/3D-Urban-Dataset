# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:08:13 2022

@author: vanis
"""

import numpy as np
import os
import glob
import open3d


#A2D2 + Sydney Urban Object 
DATA_DIR  = './Urban_Objects_Dataset/'
LABELS = ['4wd ','building', 'bus', 'car', 'pedestrian', 'pillar', 'pole',  \
          'traffic_lights', 'traffic_sign', 'truck','ute','van','curbstone', \
          'Nature object','RD normal street','Sidewalk']


folders = glob.glob(os.path.join(DATA_DIR, "[!README]*")) 

print(LABELS)

for i, folder in enumerate(folders):

        print("processing class: {}".format(os.path.basename(folder)))
        folder1 = os.path.basename(folder)
        train_files = glob.glob(os.path.join(folder, "train/*"))
        #print(train_files)
        test_files = glob.glob(os.path.join(folder, "test/*"))
        
        for f in train_files:
            points = np.load(f,allow_pickle = 'True')
            pc_xyz = points[:, 0:3]
            num_points = len(pc_xyz)
            pcd = open3d.geometry.PointCloud()
            #pcd.colors = o3d.utility.Vector3dVector([1, 0, 0])
            l = [[0,0,0] for j in range(pc_xyz.shape[0])];
            pcd.colors = open3d.utility.Vector3dVector(np.array(l))
            # assign point coordinatesr
            pcd.points = open3d.utility.Vector3dVector(pc_xyz)
            open3d.visualization.draw_geometries([pcd])
            
            
        
        for f in test_files:
            points = np.load(f,allow_pickle = 'True')
            pc_xyz = points[:, 0:3]
            num_points = len(pc_xyz)
            pcd = open3d.geometry.PointCloud()
            #pcd.colors = o3d.utility.Vector3dVector([1, 0, 0])
            l = [[0,0,0] for j in range(pc_xyz.shape[0])];
            pcd.colors = open3d.utility.Vector3dVector(np.array(l))
            # assign point coordinatesr
            pcd.points = open3d.utility.Vector3dVector(pc_xyz)
            open3d.visualization.draw_geometries([pcd])

