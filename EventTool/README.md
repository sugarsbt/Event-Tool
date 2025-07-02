# WHAT IS SUGAR'S EVENT TOOL?

Event tool is a simple Python tool to make scripting SDV Mod events easier and faster! 

It's not a full-on program, so it won't do much of the work for you, since event scripting takes a lot of creativity.
However, it will (hopefully!) make event scripting more easier to read and more user-friendly.

Also - emphasis on *simple*. This tool was initially made for personal use, so it's more catered to which commands I use most often.
It does not include the entire command list, but it does let you add custom commands that isn't specifically supported by this tool, such as `advancedMove` and the like.


# HOW DO I USE SUGAR'S EVENT TOOL?

It's pretty simple! First, you need to install **Python** if you haven't already. 
You can install the latest version at https://www.python.org/downloads/.

Then, you need to install the Python VS Code extension, assuming you're on VS Code. https://marketplace.visualstudio.com/items?itemName=ms-python.python
If not, search around to see how to use and run Python files for your coding program.

Open main.py in this folder. First, to test that it works, run the program. 
It should say in the terminal:

```Hello! Here's your event script. The key is not included. ```
```This tool is not 100 percent accurate and you should not rely on it. ```
```Please make sure to look over the code to ensure there aren't any errors! :)```

```/speak Abigail \"Hello! I'm saying something awesome.\"/pause 500/speak {{ModId}}_Iris \"Hello! I'm a custom NPC.\"/move farmer 0 4 up/faceDirection farmer down/action addMoney 500/emote Abigail 32/jump farmer/jump {{ModId}}_Iris 10/message \"Hi\"/question fork1 \"question?#Yes#No/fork {{ModId}}_OtherEvent/quickQuestion Hi?#Yup#Nope(break)Yup script(break)Nope script/end```

The first line is just a lil reminder to look over your code. 
The second like is the event script that you would copy and paste into your events section of your mod.

When you return to the main.py file, you will see three comment lines. Read them carefully and find where you should be typing.

Delete the example code in the input section.

Now comes the fun part, where you get to make the event itself! There's various commands that take a slightly different format.
However, I'll start with the most basic function: `c()`.

# c(cc)

`c` is short for command. It's the function you can use to write everything. From `advancedMove`s, to `end`.
You do not need to write the slash you use to divide all event commands. 

For example, if I wanted to end the event, I would simply write `c("end")`.

# action(action)

For `action()`, you do not need to type out `action` before your choice of action. 
You simply need to write the action as the argument, like `action(addMoney 500)`.

# emote(actor, emote)

For `emote()`, the first argument takes the actor's name, and the second argument takes either the emote numeral id or one of this tool's ids.

For example, this would be valid: `emote("Abigail", "$happy")`

These are the valid emotes taken by the tool, which are later converted to the actual emote ids automatically.
    
    "$empty": "4",
    "$question": "8",
    "$angry": "12",
    "$exclamation": "16",
    "$heart": "20",
    "$sleep": "24",
    "$sad": "28",
    "$happy": "32",
    "$x": "36",
    "$pause": "40",
    "$videogame": "52",
    "$musicnote": "56",
    "$blush": "60"

# faceDirection(actor, direction)

For `faceDirection()`, the first argument takes the actor's name, and the second argument takes either the direction numeral id or one of this tool's accepted direction ids.

For example, this would be valid: `faceDirection("Abigail", "$up")`

These are the valid directions taken by the tool, which are later converted to the actual direction ids automatically.

    "$up": "0",
    "$right": "1",
    "$down": "2",
    "$left": "3"

# jump(actor, intensity)

For `jump()`, the first argument takes the actor's name, and the second argument takes the intensity of the jump. The default is 8.
*The second argument is OPTIONAL.*

For example, this would be valid: `jump("Abigail")`, as well as `jump("Abigail", "6")`.

# message(msg)

For `message()`, the argument takes the message itself. You do not need to put escaped quotation marks around the input, the tool automatically does it for you.

For example, this would be valid: `message("This is a message. Hooray!")`

# move(actor, x, y, faceDirection)

The first argument is the name of the actor. The second and third arguments are the x y coords (enclosed in quotation marks). 
The fourth takes either the direction numeral id or one of this tool's accepted direction ids.

For example, this would be valid: `move("Abigail", "0", "6", "$up")`

These are the valid directions taken by the tool, which are later converted to the actual direction ids automatically.

    "$up": "0",
    "$right": "1",
    "$down": "2",
    "$left": "3"

Unfortunately, as of now, the command does not support multiple NPC movements at once. You will have to use the custom command `c()` for this.

# qq(question, answers)

`qq()` is the quickQuestion command in abbreviated. The first argument is the question string. The second is an array.
If you don't have a question for this, you still need to put "".

For the array, you will have to format it like this: ["Answer #1", "Answer1 script here", "Answer #2", "Answer2 script here"]

For example, this would be valid: `qq("Yes or no?", ["Yes", "script following yes here", "No", "script following no here"])`

You cannot use functions in the answer scripts. You will have to manually format it correctly.

# question(fork, question, answers)

`question()` takes three arguments. The fork argument is slightly complex. It should be formatted like this: 