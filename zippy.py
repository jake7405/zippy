#!python3
import sys
_MAX_ARGS = 7
def interactive():
    menu = {}
    menu['1'] = "Create Archive (Zip)" 
    menu['2'] = "Decompress Archive (Unzip)"
    menu['3'] = "Generate Hash"
    menu['4'] = "Manpages/Help"
    menu['5'] = "Settings"
    menu['6'] = "Exit"
    
    print("\nZippy: A simple text-based file compression suite")
    print("-------------------------------------------------")
    print("Main Menu:\n")
    
    while True:
        for i in menu:
            print(i +')', menu[i])
        option = input("\nWhat would you like to do?    SELECT: ")
        print()
    
    def parse(option):
        arg_size = len(sys.argv)
        if arg_size < 2:
            pass # basic help
            exit()
        if arg_size == 2:
            arg2(sys.argv[1])
            
    def arg2(arg):
        pass

    def arg3(arg):
        pass

    def arg4_plus(arg):
        pass
