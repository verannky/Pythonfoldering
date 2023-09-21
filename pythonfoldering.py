import os
import shutil

# Main folder and subfolders
main_folder_loc = '/Users/nunky/Downloads/RAWDATA/'  # Input main folder location
main_folder_name = 'Tower ID - 001'  # Input main folder name

def main_folder(main_folder_name):
    destination_path = os.path.join(main_folder_loc, main_folder_name)
    os.makedirs(destination_path, exist_ok=True)

main_folder(main_folder_name)

subfolders = ["1.Ortho", "2.Major Side", "3.Minor Side"]
# Function to create subfolders inside the main folder
def makingsubfolder(subfolders, main_folder_loc, main_folder_name):
    for subfolder_name in subfolders:
        destination_path = os.path.join(main_folder_loc, main_folder_name, subfolder_name)
        os.makedirs(destination_path, exist_ok=True)

makingsubfolder(subfolders, main_folder_loc, main_folder_name)
subfolder_loc = os.path.join(main_folder_loc, main_folder_name)

subsubfolders = ["1.General Tower",
                 "2.Conductor and Hardware",
                 "3.Aviation Warning Light and Spheres",
                 "1.Structure Pads",
                 "2.Steel Structure and Foundations",
                 "3.Different line components",
                 "4.OPGW and Hardware",
                 "5.Vibration Dampers and Spacer Dampers",
                 ]

subsubfolders2 = ["1.Structure Pads",
                 "2.Steel Structure and Foundations",
                 "3.Different line components",
                 "4.OPGW and Hardware",
                 "5.Vibration Dampers and Spacer Dampers",
                 ]

# Function to create subsubfolders inside the subfolders
def makingsubsubfolder(subsubfolders, subfolder_loc):
    for subsubfolder_name in subsubfolders:
        destination_path = os.path.join(subfolder_loc, subsubfolder_name)
        os.makedirs(destination_path, exist_ok=True)

makingsubsubfolder(subsubfolders, subfolder_loc)

def move_subsubfolder(subsubfolder_name, subfolder_loc, destination_folder):
    source_folder = os.path.join(subfolder_loc, subsubfolder_name)
    if os.path.exists(source_folder):
        destination_path = os.path.join(subfolder_loc, destination_folder, subsubfolder_name)
        shutil.move(source_folder, destination_path)
    else:
        print(f"Subsubfolder '{subsubfolder_name}' not found in '{subfolder_loc}'")

#movesubsubfolder to subfolder Ortho
ortho_folder = "1.Ortho" 
generaltower = "1.General Tower"
move_subsubfolder(generaltower, subfolder_loc, ortho_folder)
ConductorHardware = "2.Conductor and Hardware"
move_subsubfolder(ConductorHardware, subfolder_loc, ortho_folder)
Aviation = "3.Aviation Warning Light and Spheres"
move_subsubfolder(Aviation, subfolder_loc, ortho_folder)

#movesubsubfolder to subfolder Major Side
major_folder = "2.Major Side"
StructurePads = "1.Structure Pads"
move_subsubfolder(StructurePads, subfolder_loc, major_folder)
SteelStructure = "2.Steel Structure and Foundations"
move_subsubfolder(SteelStructure, subfolder_loc, major_folder)
Differentline = "3.Different line components"
move_subsubfolder(Differentline, subfolder_loc, major_folder)
OPGW_file = "4.OPGW and Hardware"
move_subsubfolder(OPGW_file, subfolder_loc, major_folder)
Vibration = "5.Vibration Dampers and Spacer Dampers"
move_subsubfolder(Vibration, subfolder_loc, major_folder)

makingsubsubfolder(subsubfolders2, subfolder_loc)
#movesubsubfolder to subfolder Major Side
minor_folder = "3.Minor Side"
StructurePads = "1.Structure Pads"
move_subsubfolder(StructurePads, subfolder_loc, minor_folder)
SteelStructure = "2.Steel Structure and Foundations"
move_subsubfolder(SteelStructure, subfolder_loc, minor_folder)
Differentline = "3.Different line components"
move_subsubfolder(Differentline, subfolder_loc, minor_folder)
OPGW_file = "4.OPGW and Hardware"
move_subsubfolder(OPGW_file, subfolder_loc, minor_folder)
Vibration = "5.Vibration Dampers and Spacer Dampers"
move_subsubfolder(Vibration, subfolder_loc, minor_folder)

image_path = '/Users/nunky/Downloads/RAWDATA/T.01/'  # Input image location
subsubsubfolders_name = ["1. General Tower", 
              "2. Orthomosaic of Tower", 
              "1. Conductor & Spacer Dampers", 
              "1. Aviation Warning Spheres",
              "1. Major_OPGW_GSW in Line 1", 
              "1. Major_Steel Structure Area 1", 
              "2. Major_OPGW_GSW in Line 2", 
              "1. Major_Insulator in Line 1 on Phase 1", 
              "2. Major_Steel Structure Area 2", 
              "2. Major_Insulator in Line 2 on Phase 1", 
              "3. Major_Insulator in Line 1 on Phase 2", 
              "3. Major_Steel Structure Area 3", 
              "4. Major_Insulator in Line 2 on Phase 2", 
              "5. Major_Insulator in Line 1 on Phase 3", 
              "4. Major_Steel Structure Area 4", 
              "6. Major_Insulator in Line 2 on Phase 3", 
              "5. Major_Steel Structure Area 5", 
              "1. Major_Structure Pads and Foundation",

              "2. Minor_OPGW_GSW in Line 2", 
              "1. Minor_Steel Structure Area 1", 
              "1. Minor_OPGW_GSW in Line 1", 
              "2. Minor_Insulator in Line 2 on Phase 1", 
              "2. Minor_Steel Structure Area 2", 
              "1. Minor_Insulator in Line 1 on Phase 1", 
              "4. Minor_Insulator in Line 2 on Phase 2", 
              "3. Minor_Steel Structure Area 3", 
              "3. Minor_Insulator in Line 1 on Phase 2", 
              "6. Minor_Insulator in Line 2 on Phase 3", 
              "4. Minor_Steel Structure Area 4", 
              "5. Minor_Insulator in Line 1 on Phase 3", 
              "5. Minor_Steel Structure Area 5", 
              "1. Minor_Structure Pads and Foundation"]

def organize_images(image_path, subsubsubfolder_loc):
    images = [f for f in os.listdir(image_path) if f.lower().endswith('.jpg')]
    images.sort(key=lambda x: os.path.getmtime(os.path.join(image_path, x)))
    
    if len(images) != 96:  # Check if the total number of images is 96
        other_folder = os.path.join(image_path, 'Other')
        os.makedirs(other_folder, exist_ok=True)
        
        # Move the remaining images to the "Other" folder
        for i in range(96, len(images)):
            image = images[i]
            source_path = os.path.join(image_path, image)
            destination_path = os.path.join(other_folder, image)
            shutil.move(source_path, destination_path)
    
    for i in range(len(images)):
        subsubsubfolder_index = i // 3
        if subsubsubfolder_index < len(subsubsubfolders_name):
            subsubsubfolder_name = subsubsubfolders_name[subsubsubfolder_index]
            subsubsubfolder_loc = os.path.join(image_path, subsubsubfolder_name)
            os.makedirs(subsubsubfolder_loc, exist_ok=True)
            image = images[i]
            source_path = os.path.join(image_path, image)
            destination_path = os.path.join(subsubsubfolder_loc, image)
            shutil.move(source_path, destination_path)
        else:
            print(f"Move {images[i]} to 'Other' folder")
# Call the function
organize_images(image_path, subsubsubfolders_name)

def move_subsubsubfolder(subsubsubfolder_name, subsubsubfolder_location, destination_folder):
    source_folder = os.path.join(subsubsubfolder_location, subsubsubfolder_name)
    if os.path.exists(source_folder):
        destination_folder = os.path.join(destination_folder, subsubsubfolder_name)
        shutil.move(source_folder, destination_folder)
    else:
        print(f"Subsubsubfolder '{subsubsubfolder_name}' not found in '{subsubsubfolder_location}'")

#move subsubsubfolder to subfolder Ortho > subsubfolder General Tower
move_gentower = "1. General Tower"
move_ortho = "2. Orthomosaic of Tower"
subsubsubfolder_loc = image_path
destination_folder = os.path.join(subfolder_loc, "1.Ortho", "1.General Tower")  # Specify the destination folder path
move_subsubsubfolder(move_gentower, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_ortho, subsubsubfolder_loc, destination_folder)

#move subsubsubfolder to subfolder Ortho > subsubfolder Conductor and Hardware
move_conductor = "1. Conductor & Spacer Dampers"
subsubsubfolder_loc = image_path
destination_folder = os.path.join(subfolder_loc, "1.Ortho", "2.Conductor and Hardware")  # Specify the destination folder path
move_subsubsubfolder(move_conductor, subsubsubfolder_loc, destination_folder)

#move subsubsubfolder to subfolder Ortho > subsubfolder Aviation Warning Light and Spheres
move_aviation = "1. Aviation Warning Spheres"
subsubsubfolder_loc = image_path
destination_folder = os.path.join(subfolder_loc, "1.Ortho", "3.Aviation Warning Light and Spheres")  # Specify the destination folder path
move_subsubsubfolder(move_aviation, subsubsubfolder_loc, destination_folder)

#move subsubsubfolder to subfolder Major Side > subsubfolder Structure Pads
move_structure = "1. Major_Structure Pads and Foundation"
subsubsubfolder_loc = image_path
destination_folder = os.path.join(subfolder_loc, "2.Major Side", "1.Structure Pads")  # Specify the destination folder path
move_subsubsubfolder(move_structure, subsubsubfolder_loc, destination_folder)

#move subsubsubfolder to subfolder Major Side > subsubfolder Steel Structure & Foundations
move_steelstruc1 = "1. Major_Steel Structure Area 1"
move_steelstruc2 = "2. Major_Steel Structure Area 2"
move_steelstruc3 = "3. Major_Steel Structure Area 3"
move_steelstruc4 = "4. Major_Steel Structure Area 4"
move_steelstruc5 = "5. Major_Steel Structure Area 5"
subsubsubfolder_loc = image_path
destination_folder = os.path.join(subfolder_loc, "2.Major Side", "2.Steel Structure and Foundations")  # Specify the destination folder path
move_subsubsubfolder(move_steelstruc1, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_steelstruc2, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_steelstruc3, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_steelstruc4, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_steelstruc5, subsubsubfolder_loc, destination_folder)

#move subsubsubfolder to subfolder Major Side > subsubfolder Steel Structure & Foundations
move_difflinecomp1 = "1. Major_Insulator in Line 1 on Phase 1"
move_difflinecomp2 = "2. Major_Insulator in Line 2 on Phase 1"
move_difflinecomp3 = "3. Major_Insulator in Line 1 on Phase 2"
move_difflinecomp4 = "4. Major_Insulator in Line 2 on Phase 2"
move_difflinecomp5 = "5. Major_Insulator in Line 1 on Phase 3"
move_difflinecomp6 = "6. Major_Insulator in Line 2 on Phase 3"
subsubsubfolder_loc = image_path
destination_folder = os.path.join(subfolder_loc, "2.Major Side", "3.Different line components")  # Specify the destination folder path
move_subsubsubfolder(move_difflinecomp1, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_difflinecomp2, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_difflinecomp3, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_difflinecomp4, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_difflinecomp5, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_difflinecomp6, subsubsubfolder_loc, destination_folder)

#move subsubsubfolder to subfolder Major Side > subsubfolder Steel Structure & Foundations
move_opgw1 = "1. Major_OPGW_GSW in Line 1"
move_opgw2 = "2. Major_OPGW_GSW in Line 2"
subsubsubfolder_loc = image_path
destination_folder = os.path.join(subfolder_loc, "2.Major Side", "4.OPGW and Hardware")  # Specify the destination folder path
move_subsubsubfolder(move_opgw1, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_opgw2, subsubsubfolder_loc, destination_folder)

copy_source = os.path.join(subfolder_loc, "2.Major Side", "3.Different line components")
copy_to = os.path.join(subfolder_loc, "2.Major Side", "5.Vibration Dampers and Spacer Dampers")

try:
    for item in os.listdir(copy_source):
        source_item = os.path.join(copy_source, item)
        destination_item = os.path.join(copy_to, item)

        if os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item)
        else:
            shutil.copy2(source_item, destination_item)

    print(f"Contents of '{copy_source}' copied to '{copy_to}' successfully.")
except shutil.Error as e:
    print(f"Error copying contents: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#move subsubsubfolder to subfolder Minor Side > subsubfolder Structure Pads
move_minstructure = "1. Minor_Structure Pads and Foundation"
subsubsubfolder_loc = image_path
destination_folder = os.path.join(subfolder_loc, "3.Minor Side", "1.Structure Pads")  # Specify the destination folder path
move_subsubsubfolder(move_minstructure, subsubsubfolder_loc, destination_folder)

#move subsubsubfolder to subfolder Minor Side > subsubfolder Steel Structure & Foundations
move_minsteelstruc1 = "1. Minor_Steel Structure Area 1"
move_minsteelstruc2 = "2. Minor_Steel Structure Area 2"
move_minsteelstruc3 = "3. Minor_Steel Structure Area 3"
move_minsteelstruc4 = "4. Minor_Steel Structure Area 4"
move_minsteelstruc5 = "5. Minor_Steel Structure Area 5"
subsubsubfolder_loc = image_path
destination_folder = os.path.join(subfolder_loc, "3.Minor Side", "2.Steel Structure and Foundations")  # Specify the destination folder path
move_subsubsubfolder(move_minsteelstruc1, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_minsteelstruc2, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_minsteelstruc3, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_minsteelstruc4, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_minsteelstruc5, subsubsubfolder_loc, destination_folder)

#move subsubsubfolder to subfolder Major Side > subsubfolder Steel Structure & Foundations
move_mindifflinecomp1 = "1. Minor_Insulator in Line 1 on Phase 1"
move_mindifflinecomp2 = "2. Minor_Insulator in Line 2 on Phase 1"
move_mindifflinecomp3 = "3. Minor_Insulator in Line 1 on Phase 2"
move_mindifflinecomp4 = "4. Minor_Insulator in Line 2 on Phase 2"
move_mindifflinecomp5 = "5. Minor_Insulator in Line 1 on Phase 3"
move_mindifflinecomp6 = "6. Minor_Insulator in Line 2 on Phase 3"
subsubsubfolder_loc = image_path
destination_folder = os.path.join(subfolder_loc, "3.Minor Side", "3.Different line components")  # Specify the destination folder path
move_subsubsubfolder(move_mindifflinecomp1, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_mindifflinecomp2, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_mindifflinecomp3, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_mindifflinecomp4, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_mindifflinecomp5, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_mindifflinecomp6, subsubsubfolder_loc, destination_folder)

#move subsubsubfolder to subfolder Major Side > subsubfolder Steel Structure & Foundations
move_minopgw1 = "1. Minor_OPGW_GSW in Line 1"
move_minopgw2 = "2. Minor_OPGW_GSW in Line 2"
subsubsubfolder_loc = image_path
destination_folder = os.path.join(subfolder_loc, "3.Minor Side", "4.OPGW and Hardware")  # Specify the destination folder path
move_subsubsubfolder(move_minopgw1, subsubsubfolder_loc, destination_folder)
move_subsubsubfolder(move_minopgw2, subsubsubfolder_loc, destination_folder)

copy_source_minor = os.path.join(subfolder_loc, "3.Minor Side", "3.Different line components")
copy_to_minor = os.path.join(subfolder_loc, "3.Minor Side", "5.Vibration Dampers and Spacer Dampers")

try:
    for item in os.listdir(copy_source_minor):
        source_item = os.path.join(copy_source_minor, item)
        destination_item = os.path.join(copy_to_minor, item)

        if os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item)
        else:
            shutil.copy2(source_item, destination_item)

    print(f"Contents of '{copy_source_minor}' copied to '{copy_to_minor}' successfully.")
except shutil.Error as e:
    print(f"Error copying contents: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
