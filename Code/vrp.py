
import pandas as pd

def load_data_from_file(file_path):
    data = {}
    current_section = None

    with open(file_path, "r") as file:
        for line in file:
            
            line = line.strip()

            if line.startswith("TIME"):
                current_section = "TIME"
                data[current_section] = []
            elif line.startswith("DEPOTS_NODES"):
                current_section = "DEPOTS_NODES"
                data[current_section] = []
            elif line.startswith("CUSTOMERS_NODES"):
                current_section = "CUSTOMERS_NODES"
                data[current_section] = []
            elif line.startswith("VEHICLES"):
                current_section = "VEHICLES"
                data[current_section] = []
            elif line.startswith("COSTS"):
                current_section = "COSTS"
                data[current_section] = []
            else:
                if current_section:
                    data[current_section].append(line.strip().split())

    return data

file_path = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\Datasets\VRP_01.txt"
loaded_data = load_data_from_file(file_path)
time = pd.DataFrame(loaded_data["TIME"])
time.columns = time.iloc[0]
time = time[1:-1]
print(time)

distance_matrix = []
costs = loaded_data["COSTS"]
for i in costs:
    for j in i:
        distance_matrix.extend