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


obj_file_path = os.environ.get('OBJ_FILE_PATH')
output_file_path = os.environ.get('OUTPUT_FILE_PATH')

xmin = float(os.environ.get('XMIN', 0.0))
xmax = float(os.environ.get('XMAX', 1.0))
ymin = float(os.environ.get('YMIN', 0.0))
ymax = float(os.environ.get('YMAX', 1.0))
zmin = float(os.environ.get('ZMIN', 0.0))
zmax = float(os.environ.get('ZMAX', 1.0))

extract_coordinates_from_obj(obj_file_path, xmin, xmax, ymin, ymax, zmin, zmax, output_file_path)

