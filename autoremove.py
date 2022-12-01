import os
import glob # for glob.glob
import sys # for sys.argv
from sys import platform # for platform

# if not win32, then exit
if os.name != 'nt':
    print ("This script is for Windows only.")
    sys.exit(1)

# get the path to the current directory

username = os.getlogin()
print(f"Username: {username}")

print("Note : script ini hanya berjalan di Windows dan menghapus files exe pada windows, jika ingin menambahkan untuk menghapus yang lain, bisa ditambahkan di script ini pull request ke github saya atau tunggu updatenya :D".upper())

print('''\n

    Github Pages : https://Xnuvers007.github.io
    blog : https://mykingbee.blogspot.com
    Github : Xnuvers007
    Donate : https://saweria.co/Xnuvers007

\n''')

print("======"*5)
# get the list of all files in Downloads folder exe
# for file in glob.glob(f"C:\\Users\\{username}\\Downloads\\testautoremoveexe\\*.exe"):
def normal():
    for file in glob.glob(f"C:\\Users\\{username}\\Downloads\\*.exe"):

        # get the file name
        filename = os.path.basename(file)

        # get the file size
        filesize = os.path.getsize(file)

        # print the file name and size
        print(f"File: {filename} Size: {filesize}\n")

    print("======"*5)
    print("\n")

    print("Apakah anda yakin ingin menghapus file exe pada Downloads? (y/n)")
    answer = input()
    if answer == "y" or answer == "Y":
        print("Deleting...")
        path = f"C:\\Users\\{username}\\Downloads\\*.exe"
        for filename in glob.glob(path):
            os.remove(filename)
        print("Done!")
    else:
        print("Aborted!")

    os.system("pause")

def internetdownloadmanager():
    for file in glob.glob(f"C:\\Users\\{username}\\Downloads\\Programs\\*.exe"):

        # get the file name
        filename = os.path.basename(file)

        # get the file size
        filesize = os.path.getsize(file)

        # print the file name and size
        print(f"File: {filename} Size: {filesize}\n")

    print("======"*5)
    print("\n")

    print("Apakah anda yakin ingin menghapus file exe pada Downloads? (y/n)")
    answer = input()
    print("\n")
    if answer == "y" or answer == "Y":
        print("Deleting...")
        path = f"C:\\Users\\{username}\\Downloads\\Programs\\*.exe"
        for filename in glob.glob(path):
            os.remove(filename)
        print("Done!")
    else:
        print("Aborted!")

    os.system("pause")

def main():
    print("======"*5)
    print("1. Normal")
    print("2. Internet Download Manager")
    print("3. Update (Khusus yang menggunakan Git clone")
    print("======"*5)
    print("Pilih Mode : ")
    mode = input()
    if mode == "1":
        normal()
    elif mode == "2":
        internetdownloadmanager()
    elif mode == "3":
        os.system("git pull origin master")
    else:
        print("Mode tidak ditemukan")
        os.system("pause")
        main()
    
if __name__ == "__main__":
    main()