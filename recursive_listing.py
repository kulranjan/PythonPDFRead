
from os import chdir, listdir
from os.path import isfile, join, exists, isdir
import camelot

# print("\\".join((r"C:\kdata\myPYTHON\Python_Courses\Python_March2022_Tutorials\Day9\Generators", "entry.py")))
# print(os.getcwd())
# new_file_name = join(r"C:\kdata\myPYTHON\Python_Courses\Python_March2022_Tutorials\Day9\Generators", "entry.py")
# print(new_file_name)


def get_files(path):
    for file in listdir(path):
        full_path = join(path, file)
        if isfile(full_path):
            if exists(full_path):
                yield full_path


def get_directories(path):
    for directory in listdir(path):
        full_path = join(path, directory)
        if isdir(full_path):
            if exists(full_path):
                yield full_path


# def get_files_recursively(directory):
#     for file in get_files(directory):
#         yield file
#     for subdirectory in get_directories(directory):
#         for file in get_files_recursively(subdirectory):
#             yield file

# simplified version of above function


def get_files_recursively(directory):
    yield from get_files(directory)
    for subdirectory in get_directories(directory):
        yield from get_files_recursively(subdirectory)


files = get_files_recursively(r"C:\Users\kulra\OneDrive\Desktop\SplittedPDF")

#for file_names in files:
#   print(file_names)

file=list(files)

#print(type(files))
print(len(file))

def convert(lit): 
    res_dct={lit[i]:"" for i in range(len(lit))}

    #res_dct={lit[i]:i for i in range(len(lit))}
    return res_dct
def convert2(lit): 
    #res_dct={lit[i]:"" for i in range(len(lit))}

    res_dct={lit[i]:i for i in range(len(lit))}
    return res_dct

#cdict={file:range(len(file))}

#filesInDictionaryString=convert(file)
filesInDictionaryNumber=convert2(file)

#for c in cdict:
#    print (c)

#print(filesInDictionaryString)
#print(filesInDictionaryNumber)

chdir(r"C:\Users\kulra\OneDrive\Desktop\SplittedPDF")

print(dir)
for key in filesInDictionaryNumber:
    print(key)

    #tables = camelot.read_pdf("04 2022 120 Day OS Checks 09 10 21 to 12 08 21   179  2pg-1.pdf", flavor = 'stream')

    #tables[0].df[4][tables[0].df[4].str.strip().astype(bool)]