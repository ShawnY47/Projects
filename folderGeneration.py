import os, shutil

for i in range (10):
    os.makedirs('LTH0000'+str(i))
    i += 1

for folder in (os.listdir(os.getcwd())):
    if os.path.isfile(folder):
        continue
    elif os.path.isdir(folder):
        shutil.copy('/Users/shawn/Desktop/PythonLearning/Textbook/ex1.py',os.path.join(os.getcwd(),folder))
