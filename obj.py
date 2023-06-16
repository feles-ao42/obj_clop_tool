import os

def extract_coordinates_from_obj(obj_file, xmin, xmax, ymin, ymax, zmin, zmax, output_file):
    coordinates = []

    with open(obj_file, 'r') as f:
        for line in f:
            if line.startswith('v '):
                parts = line.split()
                x = float(parts[1])
                y = float(parts[2])
                z = float(parts[3])

                if xmin <= x <= xmax and ymin <= y <= ymax and zmin <= z <= zmax:
                    coordinates.append((x, y, z))

    with open(output_file, 'w') as f:
        for coord in coordinates:
            f.write(f"v {coord[0]} {coord[1]} {coord[2]}\n")

    print(f"Extracted coordinates saved to {output_file}.")

obj_file_path = "./data/obj/after.obj"
output_file_path = "./data/obj/out_after.obj"

xmin = 0.0
xmax = 100.0
ymin = 0.0
ymax = 50.0
zmin = 0.0
zmax = 100.0

extract_coordinates_from_obj(obj_file_path, xmin, xmax, ymin, ymax, zmin, zmax, output_file_path)

