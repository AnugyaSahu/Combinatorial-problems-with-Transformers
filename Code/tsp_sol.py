import gzip
import os
import numpy as np

def load_tsp_file(file_path):
    coordinates = []
    with gzip.open(file_path, 'rt') as file:
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

def open_opt_tour_file(file_path):
    tour = []
    with gzip.open(file_path, 'rt') as file:
        for line in file:
            line = line.strip()
            if line.isdigit():
                tour.append(int(line))
    return tour

opt_tours = []
file_names = []

folder_path = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\ALL_tsp.tar\ALL_tsp"

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    if file_name.endswith(".opt.tour.gz"):
        try:
            opt_tour = open_opt_tour_file(file_path)
        except(IndexError):
            continue

        file_names.append(file_name)
        opt_tours.append(opt_tour)

tsp_datas_ = []

folder_path = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\ALL_tsp.tar\ALL_tsp"

for i in file_names:
    s = str(i.split(".")[0])
    s = s + ".tsp.gz"
    file_path = os.path.join(folder_path, s)
    tsp_datas_.append(load_tsp_file(file_path))

if len(file_names) == len(tsp_datas_):
    print(len(file_names))
    print(True)

for i in tsp_datas_:
    print(i.shape)
    
for i in opt_tours:
    print(i)