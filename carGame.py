command = ""

# Prompt the user to enter the command
while command.lower() !="quit":
    command = input("Enter a command: ").lower()
    
    # Check the command and perform the required action
    if command() == "list":
        print("List of available commands:")
        print("list - List all available commands")
        print("create <name> - Create a new item")
        print("read <id> - Read an item by its ID")
        print("update <id> - Update an item by its ID")
        print("delete <id> - Delete an item by its ID")
        print("quit - Exit the program")
    
    elif command().startswith("create "):
        name = command.split(" ")[1]
        print(f"Creating new item: {name}")
    
    elif command().startswith("read "):
        id = int(command.split(" ")[1])
        print(f"Reading item with ID {id}")
    
    elif command().startswith("update "):

started = False

while True:
    command = input ('>').lower() 
    
    if command == 'start':
        print('The car has started.')
        if started:
            print('The car is already started.')
    elif command == 'stop':
        print('The car has stopped.')
        if not started:
            print('The car is already stopped.')
    
    elif command == 'accelerate':
        print('The car is accelerating.')
    
    elif command == 'brake':
        print('The car is braking.')
    
    elif command == 'help':
        print("""
start -to start a car
stop - to stop a car
accelerate - to accelerate the car
brake - to apply brakes to the car
help - to get help on available commands
quit - to exit the program
        """)
    
    elif command == 'quit':
        print('Goodbye!')
        break
    else:
        print('Invalid command. Please try again.')