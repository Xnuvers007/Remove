import winreg as reg
import os

def AddToRegistry():
    # path3 = os.path.dirname(os.path.realpath(__file__))
    # print(path3)
    # find the path files autoremove.py
    path = os.path.dirname(os.path.abspath(__file__))
    s_name = ".\\autoremove.exe"
    address = os.path.join(path, s_name)

    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"

    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open, "autoremove", 0, reg.REG_SZ, address)
    reg.CloseKey(open)

def RemoveFromRegistry():
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"

    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.DeleteValue(open, "autoremove")
    reg.CloseKey(open)

if __name__ == '__main__':
    print("Apakah Kamu ingin Membuatnya Menjadi Startup? (y/n)")
    print(" y = Menambahkannya ke Registry")
    print(" n = Menghapusnya dari Registry")
    print(" p = Keluar dari Program")
    answer = input("Jawaban: ")
    if answer == 'y' or answer == 'Y':
        AddToRegistry()
        print("Berhasil Menambahkan ke Registry")
    elif answer == 'n' or answer == 'N':
        RemoveFromRegistry()
        print("Berhasil Menghapus dari Registry")
    elif answer == 'p' or answer == 'P':
        exit()
    else:
        print("Pilihan tidak ada")
        exit(code=None)
