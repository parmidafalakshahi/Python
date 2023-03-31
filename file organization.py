import os,glob
folder = input("please enter folder address:")
files = glob.glob(folder + "/*")
format_set = set()
for file in files:
    format = file.split(".").pop()
    format_set.add(format.lower())
#print(format_set)
def make_folder():
    for file_types in format_set:
        try:
            os.makedirs(folder + "/" + file_types)
        except:
            continue

def move_file():
        for file in files:
            try:
                format = file.split(".").pop()
                from_this = file
                to_this = folder + "/" + format + "/" + file.split("\\").pop()
                os.rename(from_this , to_this )
            except:
                continue

make_folder()
move_file()
