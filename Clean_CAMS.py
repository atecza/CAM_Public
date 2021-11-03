"""
This routine will cremove any duplicate lines by disccarding any lines that are older than other lines
The routine takes all the files in the provided directory, cleans them, and places them in a new "clean" directory.
"""
# ----------------------------------- IMPORTS --------------------------------------#
import os
import datetime
import pandas as pd
# ----------------------------------------------------------------------------------#
home_dir = '/home/carterrhea/Documents/CAM-proj'  # Directory containing CAM infomation
clean_dir = '/home/carterrhea/Documents/CAM-proj/Clean/'  # Directory to be made containing clean CAMS
# ----------------------------------------------------------------------------------#



CAMS_block = {}  # User ID : blocks
CAMS_link = {}  # User ID: links
os.chdir(home_dir)
names = []
cam_names = []

for filename in os.listdir(os.getcwd()):  # Step through files
    # Clean link files
    if filename.endswith('_links.csv'):
        indices_keep = []  # Indices to keep
        df = pd.read_csv(filename)  # Read in data
        cam_name = filename.split("_")[0]+'_'+filename.split("_")[1]
        df_blocks = pd.read_csv(cam_name+'_blocks.csv')
        connecting_blocks = [(start,end) for start,end in zip(df['starting_block'],df['ending_block'])]
        connecting_blocks_inv = [(end,start) for start,end in zip(df['starting_block'],df['ending_block'])]
        duplicate_lines = {}  # {(start,end): [indices]}
        # Collect dictionary of duplicate links and indices in dataframe
        for index,connection in enumerate(connecting_blocks):
            if connecting_blocks.count(connection) + connecting_blocks_inv.count(connection) > 1:
                if duplicate_lines.get(connection):
                    duplicate_lines[connection].append(index)
                else:
                    duplicate_lines[connection] = [index]
            else:
                indices_keep.append(index)  # Keep single line
        # Step through each duplicate and delete the entries with a early time
        for blocks,indices in duplicate_lines.items():
            best_index = indices[0]  # Set first as best
            best_time = [int(val) for val in df.iloc[[best_index]]['timestamp'].values[0].split(':')]
            best_time = datetime.time(hour=best_time[0], minute=best_time[1], second=best_time[2])
            # Step through all other lines
            for line_index in indices[1:]:
                possible_time = [int(val) for val in df.iloc[[line_index]]['timestamp'].values[0].split(':')]
                possible_time = datetime.time(hour=possible_time[0], minute=possible_time[1], second=possible_time[2])
                if possible_time > best_time:
                    best_time = possible_time
                    best_index = line_index
            indices_keep.append(best_index)
        # Update dataframe
        df = df.iloc[indices_keep]
        # Save as clean dataframe
        df.to_csv(clean_dir+filename, index = False, header=True)

    # Clean blocks
    if filename.endswith('_blocks.csv'):
        df = pd.read_csv(filename)
        df = df[df['title'] != '']  # Drop empty blocks
        df.to_csv(clean_dir+filename, index = False, header=True)
