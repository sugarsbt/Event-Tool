
eventString = ""

def inputData():
    ####### Begin writing functions below for your input. After you're done, go to main.py and run it. ########

    speak("Abigail", "Hello! I'm saying something awesome.")
    c("pause 500")
    speak("`Iris", "Hello! I'm a custom NPC.")
    move("farmer", "0", "4", "up")
    faceDirection("farmer", "down")
    action("addMoney 500")
    emote("Abigail", "$happy")
    jump("farmer")
    jump("`Iris", "10")
    message("Hi")
    question("1`OtherEvent", "question?", ["Yes", "No"])
    qq("Hi?", ["Yup", "Yup script", "Nope", "Nope script"])
    c("end")

    ####### The example code is above. You may delete everything in between the first comment and this one. #######



####### WARNING! Do not touch any of the code below. #######
def speak(actor, text):
    global eventString
    eventString += "/speak "+actor+" \\\""+text+"\\\""
def move(actor, x, y, faceDirection):
    global eventString
    eventString += "/move "+actor+" "+x+" "+y+" "+faceDirection
def faceDirection(actor, direction):
    global eventString
    eventString += "/faceDirection "+actor+" "+direction
def action(action):
    global eventString
    eventString += "/action "+action
def c(cc):
    global eventString
    eventString += "/"+cc
def emote(actor, emote):
    global eventString
    eventString += "/emote "+actor+" "+emote
def jump(actor, intensity=8):
    global eventString
    if intensity==8:
        eventString += "/jump "+actor
    else:
        eventString += "/jump "+actor+" "+intensity
def message(msg):
    global eventString
    eventString += "/message \\\""+msg+"\\\""
def question(fork, question, answers):
    global eventString
    if fork != "false":
        eventString += "/question fork"+fork[0]+" \\\""+question
        for i in answers:
            eventString += "#"+i
        else:
            eventString += "/fork "
            for i in fork:
                if i == fork[0]:
                    continue
                eventString += i
    else:
        eventString += "/question null \\\""+question
        for i in answers:
            eventString += "#"+i
def qq(question, answers):
    global eventString
    eventString += "/quickQuestion "+question
    index = 0
    for i in range(0, len(answers), 2):
        eventString += "#" + answers[i]
    for i in range(1, len(answers), 2):
        eventString += "(break)" + answers[i]


inputData()

eventString = eventString.replace("`", "{{ModId}}_")
emoteDict = {
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
}
directionDict = {
    "$up": "0",
    "$right": "1",
    "$down": "2",
    "$left": "3"
}
advancedMoveDirectionDict = {
    "$aup": "4",
    "$aright": "1",
    "$adown": "2",
    "$aleft": "3"
}
for key in emoteDict:
    eventString = eventString.replace(key, emoteDict[key])
for key in directionDict:
    eventString = eventString.replace(key, directionDict[key])
for key in advancedMoveDirectionDict:
    eventString = eventString.replace(key, advancedMoveDirectionDict[key])

print("\n\nHello! Here's your event script. \nThe key is not included. This tool is not 100 percent accurate and you should not rely on it. \nPlease make sure to look over the code to ensure there aren't any errors! :)\n\n"+eventString)