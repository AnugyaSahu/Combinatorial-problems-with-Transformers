import numpy as np

def load_tsp_file(file_path):
    coordinates = []
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("NODE_COORD_SECTION"):
                break
        for line in file:
            line = line.strip()
            if line == "EOF":
                break
            parts = line.split()
            coordinates.append([float(parts[1]), float(parts[2])])
    return np.array(coordinates)

file_path = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\Datasets\ge1M1r.tsp"
tsp = load_tsp_file(file_path)
print(np.array(tsp).shape)

###### DIMACS TSP

import shutil

def extract_tar_gz(tar_gz_path, extract_path):
    shutil.unpack_archive(tar_gz_path, extract_path, "gztar")
    
data = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\Datasets\TSP_DIMACS.tar.gz"

extract_path = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\TSP dimacs"

extract_tar_gz(data,  extract_path)

def read_single_file(file_path):
    coordinates = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.split()
                if len(line) == 3:
                    try:
                        coordinates.append((int(line[1]), int(line[2])))
                    except(ValueError):
                        continue
        return np.array(coordinates)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

file_path = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\TSP dimacs\C1k.1"
file_content = read_single_file(file_path)
print(file_content.shape)