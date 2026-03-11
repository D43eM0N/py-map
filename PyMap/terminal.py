import cmd
import subprocess

import sys, os
sys.path.append(os.path.join(os.getcwd(), "PingSweep"))

class myTool(cmd.Cmd):
    intro = "Welcome to PyMap!\nType help or -h to list commands. Type exit to quit.\n"
    prompt = "PyMap > "

    def  do_use(self, arg):
        "for use modules, use 1, use 2 etc."

        ping_path = os.path.join("PingSweep", "pingsweep.py")
        port_path = os.path.join("PortWise", "portscanner.py")

        if arg == "1":
            self.prompt = "PyMap/PingSweep > "

            while True:
                command = input(self.prompt)

                if command == "back":
                    self.prompt = "PyMap > "
                    break

                if command == "exit":
                    self.do_exit(self) 

                split_command = command.split()

                subprocess.run(["python", ping_path] + split_command[1:])


        elif arg == "2":
            self.prompt = "Pymap/PortScanner > "

            while True:
                command = input(self.prompt)

                if command == "back":
                    self.prompt = "PyMap > "
                    break

                if command == "exit":
                    self.do_exit(self) 

                split_command = command.split()

                subprocess.run(["python", port_path] + split_command[1:])
    

    def do_exit(self, arg):

        print("Quiting PyMap...")

        raise SystemExit
        
if __name__ == '__main__':
    myTool().cmdloop()