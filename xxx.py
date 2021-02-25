from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox, CheckBox, Picture, ListBox

app = App(title="Hero - o - Matic", width=800, layout="grid", bg="yellow")
app.height = 800

# The lists
pics = ["TheHulk.jpg", "Spiderman.jpg"]
piclist = ["TheHulk", "Spiderman", "Batman", "WonderWoman"]
animallist = ["AARDVARK", "BADGER", "CAT", "DOLPHIN", "FROG", "POODLE"]
adjectives = ["AMAZING", "BONNY", "FUNNY", "CHARMING", "DELIGHTFUL"]


# Collecting inputs and showing the choice of hero
def makeheroname():
    global piccheckyes
    global piccheckno
    global labeloutput
    adjective = bgpadjective.value
    colour = textcolour.value
    animal = cmbanimal.value
    hero = adjective + " " + colour + " " + animal
    labeloutput.value = "You are ... The " + hero + "."
    labeloutput.text_size = 14

    piccheckyes = CheckBox(app, text="I want to see a  SUPERHERO", command=pictureadd, grid=[1, 13])
    piccheckyes.text_size = 16
    piccheckno = CheckBox(app, text="I don't want to see a picture thanks", command=end, grid=[1, 14])
    piccheckno.text_size = 16


# Hiding widgets
def hide():
    bgpadjective.hide()
    message1.hide()
    message2.hide()
    message3.hide()
    cmbanimal.hide()
    buttonclick.hide()
    labeloutput.hide()
    piccheckyes.hide()
    piccheckno.hide()
    textcolour.hide()


# Finish
def end():
    hide()
    message4 = Text(app, text="GOODBYE", grid=[2, 5])
    message4.text_size = 18


# Choose a SuperHero
def pictureadd():
    global combobox
    global buttonfavourite
    hide()
    combobox = Combo(app, options=piclist, grid=[2, 2])
    combobox.text_size = 18

    buttonfavourite = PushButton(app, text=" Choose your favourite SUPERHERO from above then click HERE",
                                 command=picture, grid=[2, 4])
    buttonfavourite.text_size = 18


# Show Superhero choice picture
def picture():
    labeloutput.hide()
    combobox.hide()
    buttonfavourite.hide()
    picchoice = combobox.value + ".jpg"
    picture = Picture(app, image=picchoice, grid=[0, 2])


# Setting up the initial widgets
message1 = Text(app, text="Choose an adjective", grid=[1, 1])
message1.text_size = 18
bgpadjective = ButtonGroup(app, options=adjectives, grid=[0, 2],
                           selected="AMAZING")
bgpadjective.text_size = 14
message2 = Text(app, text="Enter a colour", grid=[2, 3])
message2.text_size = 18
textcolour = TextBox(app, grid=[2, 4])
textcolour.width = 15
textcolour.text_size = 18
message3 = Text(app, text="Pick an animal ", grid=[1, 5])
message3.text_size = 18

cmbanimal = Combo(app, options=animallist, grid=[0, 7])
cmbanimal.text_size = 14

buttonclick = PushButton(app, text="Make me a hero", command=makeheroname, grid=[2, 9], width=15, height=2)
buttonclick.bg = "red"
buttonclick.text_size = 18
buttonclick.font = "bold"

labeloutput = Text(app, text=" Hero name will appear here", grid=[1, 10])
app.display()
