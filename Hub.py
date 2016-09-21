'''
    Author: Wouter Dijkstra
'''
import os
path = os.getcwd()

userInput = ""
while True:
    userInput = input('CMD: ').lower()
    if (userInput == "stop" or userInput == "exit" or userInput == "close"):
        print("Exiting hub...")
        break

    commands = userInput.split()

    if(commands[0] == "commands"):
        commandsList = [
            '"commands" - shows all commands available',
            '"run [lesson] [assignment]" - runs assignment X from lesson X (run Les3 3_1)'
        ]
        print("##################################")
        print("#######  C O M M A N D S   #######")
        print("##################################")
        for command in commandsList:
            print(command)
    if(commands[0] == "run"):
        lesson = commands[1]
        assignment = commands[2]

        if("les" in lesson):
            if("" in assignment):


                try:
                    print("##############################################")
                    print("Starting lesson:", lesson,", assignment:", assignment, "for you..")
                    exec(open(path+"/"+lesson+"/"+assignment+".py").read())
                    print("##############################################")
                except ValueError:
                    print("Failed to start this lesson/assignment..")
            else:
                print("Invalid assignment name")
        else:
            print("Invalid lesson name")
