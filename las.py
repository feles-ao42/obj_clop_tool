import laspy
import numpy as np
import os


def extract_points_by_coordinates(input_file, output_file, min_x, max_x, min_y, max_y, min_z, max_z):
    # LASファイルを読み込みます
    inFile = laspy.file.File(input_file, mode='r')

    # 座標範囲に基づいてポイントをフィルタリングします
    x_range = np.logical_and(inFile.x >= min_x, inFile.x <= max_x)
    y_range = np.logical_and(inFile.y >= min_y, inFile.y <= max_y)
    z_range = np.logical_and(inFile.z >= min_z, inFile.z <= max_z)
    selected_points = np.logical_and(np.logical_and(x_range, y_range), z_range)
    print("X ~~~~~~~~")
    print(inFile.x.min())
    print(inFile.x.max())
    print((inFile.x.max() - inFile.x.min()) / 2)
    print("Y ~~~~~~~~")
    print(inFile.y.min())
    print(inFile.y.max())
    print((inFile.y.max() - inFile.y.min()) / 2)
    # print("Z ~~~~~~~~")
    # print(inFile.z.min())
    # print(inFile.z.max())
    # print(inFile.z.max() - inFile.z.min())

    if np.any(selected_points):
        # 選択されたポイントを新しいLASファイルに書き込みます
        outFile = laspy.file.File(output_file, mode='w', header=inFile.header)
        outFile.points = inFile.points[selected_points]
        outFile.close()
        print("切り出し処理が完了しました。")
    else:
        print("指定された座標範囲内にデータが見つかりませんでした。")


# 使用例
input_file = "./data/las/input.las"  # 入力ファイルのパス
output_file = "./data/las/output.las"  # 出力ファイルのパス

min_x = 357103
max_x = 357201
min_y = 3917373
max_y = 3917517
min_z = 0
max_z = 300

extract_points_by_coordinates(input_file, output_file, min_x, max_x, min_y, max_y, min_z, max_z)
