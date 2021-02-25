'''from guizero import App, Text
app = App(title="Hi there")

firstmessage = Text(app, text="This is big text")
secondmessage = Text(app, text="This is green")

firstmessage.text_size = 40
secondmessage.bg = "green"

app.display()

#event gui
# Import the GUI widgets that you'll be using, and create the 'app' for your program.
from guizero import App, TextBox, PushButton, Text, info
app = App()

# Function definitions for your events go here.
def btn_go_clicked():
    info("Greetings","Hello, " + txt_name.value + " - I hope you're having a nice day")

# Your GUI widgets go here
lbl_name = Text(app, text="Hello. What's your name?")
txt_name = TextBox(app)
btn_go = PushButton(app, command=btn_go_clicked, text="Done")

# Show the GUI on the screen
app.display()
'''
# guizero - Hero name generator
'''
from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox


def make_hero_name():
    adjective = bgp_adjective.value
    colour = txt_colour.value
    animal = cmb_animal.value
    hero = adjective + " " + colour + " " + animal
    lbl_output.value = "You are... The " + hero + "."


    
app = App(title="Hero-o-matic")

# Function definitions for your events go here.

# Your GUI widgets go here
message1 = Text(app, text="Choose an adjective")
bgp_adjective = ButtonGroup(app, options=["Amazing", "Bonny", "Charming", "Delightful"], selected="Amazing")

message2 = Text(app, text="Enter a colour?")
txt_colour = TextBox(app)

message3 = Text(app, text="Pick an animal")
cmb_animal = Combo(app, options=["Aardvark", "Cat", "Dolphin", "Tiger", "Velociraptor", "Walrus"], selected="Aardvark", width=20)


btn_make_name = PushButton(app, text='Make me a hero', command=make_hero_name)
lbl_output = Text(app, text="A hero name will appear here")

# Set up event triggers here

# Show the GUI on the screen, start listening to events.
app.display()
'''

#using a box
from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox, Box
app = App(title="Hero-o-matic", width=300, bg="white")
def make_hero_name():
    adjective = bgp_adjective.value
    colour = txt_colour.value
    animal = cmb_animal.value
    hero = adjective + " " + colour + " " + animal
    lbl_output.value = "You are... The " + hero + "."
    print(lbl_output)


# create a box
box = Box(app)

# modify each widget so it is now housed in the box

# now change the properties of the box
box.bg = "white"
box.text_size = 12

message1 = Text(app, text="Choose an adjective")
bgp_adjective = ButtonGroup(app, options=["Amazing", "Bonny", "Charming", "Delightful"], selected="Amazing")

message2 = Text(app, text="Choose a colour")
message2.text_color = "blue"
txt_colour = TextBox(app)

message3 = Text(app, text="Pick an animal")
cmb_animal = Combo(app, options=["Aardvark", "Badger", "Cat", "Dolphin", "Velociraptor"], selected="Aardvark", width=20)

btn_make_name = PushButton(app, text='Make me a hero', command=make_hero_name)
lbl_output = Text(box, text="Your hero name will appear here")
app.display()
# This is then shown on the screen by setting the .value property of lbl_output to a string including the new name.

'''Challenges
Add some more adjectives and animals to the program
Change the program by replacing one type of widget in the code for another (e.g. swap the adjective ButtonGroup for a ComboBox)
Add another part to the superhero name, perhaps using checkboxes'''