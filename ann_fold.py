import pandas as pd
import os as os
import numpy as np

data_dir = 'O:/daaaCEMTREX/openImgCSv/v6/open_data/val_present'
annot_dir = 'O:/daaaCEMTREX/openImgCSv/v6/labels/validation-annotations-bbox.csv'
df = pd.read_csv(annot_dir)
df.head
data_folders = os.listdir(data_dir)
for folder in data_folders:
    # import pdb; pdb.set_trace()
    if folder.endswith('.csv') or folder.endswith('.ipynb'):
        continue
    image_folder_dir = data_dir + '/' + folder
    images = os.listdir(image_folder_dir)
    image_list = [i[:-4] for i in images]
    new_df = df[df['ImageID'].isin(image_list)]
    class_df = pd.read_csv("O:/downloads/required_classes.csv")
    class_list = class_df.ClassID.tolist()
    # print(class_list)
    n1 = new_df[(new_df["LabelName"].isin(class_list))]
    n1.to_csv(image_folder_dir+'/'+folder+".csv")
    ########## rename classes