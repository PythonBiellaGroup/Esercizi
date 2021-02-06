import platform

def sys_info():
    print("Il Sistema attualmente in uso è: " + platform.system())
    print("Info Release: " + platform.release())