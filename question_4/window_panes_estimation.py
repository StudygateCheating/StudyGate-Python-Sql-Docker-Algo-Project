"""
Inorder determine the number of panes. The process below is used:

1. Given a hometown one can estimate the number of blocks based on the size of the town.

2. Given the number of blocks, one can estimate the number of buildings per block.

3. One can get(or make an assumption) the average height of the buildings and the number of windows. (Some buildings are tall and others are average)

4. Each windows with have the number of panes that it has based on the size of the window and the size of the pane.

5.  One should also factor in the number of free areas where there are no buildings and remove that value from the land size of the hometown.

6. Since we cannot have a have a fraction of a pane the final value will be rounded off to the nearest whole number

"""
import math


def get_size_of_window_panes():
    land_size = 1000000  # square Meters
    block_size = 1000 # square meters
    number_of_buildings_per_block = 20
    average_building_height = 50 # Meters
    free_area =  100 # square neters
    windows_size = 2 # square meters
    pane_size = 0.20 # square meters

    total_number_of_buildings = (land_size - free_area ) / block_size  * number_of_buildings_per_block
    total_bumber_of_windows_per_building = average_building_height  / windows_size
    total_no_of_windows_home_town = total_number_of_buildings * total_bumber_of_windows_per_building
    total_number_of_panes_per_window = windows_size / pane_size
    total_no_of_panes_home_town = total_number_of_panes_per_window * total_no_of_windows_home_town
    return math.ceil(total_no_of_panes_home_town)


if __name__ == '__main__':
    result =  get_size_of_window_panes()
    print(result)
