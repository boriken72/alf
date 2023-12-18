import pyjokes
from ai import AI
from todo import Todo, Item

alf = AI()
todo = Todo()

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    alf.say(funny)

def add_todos()->bool:
    item = Item()
    alf.say("Tell me what to add to the list")
    try:
        item.title = alf.list()
        todo.new_item(item)
        message = "Added" + item.title
        alf.say(message)
        return True
    except:
        print("Oops there was an error")
        return False

def list_todos()->bool:
    alf.say("Here are your to do's")
    for item in todo:
        alf.say(item.title)
    else:
        alf.say("This list is empty")
        
def remove_todo()->bool:
    alf.say("Tell me which item to remove")
    try:
        item_title = alf.listen()
        todo.remove_item(title=item_title)
        message = "Removed" + item_title
        alf.say(message)
        return True
    except:
        print("oops there was an error")
        return False
           
command = ""

while True and "goodbye" not in command:
    try:
        command = alf.listen()
    except:
        print("oops there was an error")
        command = ""
    print(f"command was: {command}")
    print(type(command))
    
    if command == "tell me a joke":
        joke()
    
    if command in ['add item', 'add to do', 'add to-do']:
        add_todos()
        command = ""
    if command in ["list todos", "list todo", "list to-do", "list to do"]:
        list_todos()
        command = ""
    if command in ["remove todo", "remove item", "remove todos", "remove to-do"]:
        remove_todo()
        command = ""
            
alf.say("Goodbye, look forward to our next encounter ")
