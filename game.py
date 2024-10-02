


# Importing necessary modules+
import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout



class screen1(Screen):
    pass
class screen2(Screen):
    pass
class MyBoxLayout(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.current_hint_index = 0
        self.ii= random.randrange(1,6)
        self.ii=2
        if self.ii==1:
            a=['Enter an adjective','Enter a name:','Enter a verb:','Enter a noun:','Enter an adjective2:']
            self.hints = a
        if self.ii==2:
            b=["enter an adjective [thing which is very strong and powerful] ","enter a name ","enter a verb ","enter an adjective ","enter a verb "]
            self.hints=b
        if self.ii==3:
            c=['enter an adjective describing a human ',"enter a name ","enter a verb ","enter an adjective ","enter an adjective (describing a monstor) ","enter a verb "]
        if self.ii==4:
            d=["an adjective describing an a explorer ","enter a name ","enter a verb in v3 form (ending with ed) ","enter an adjective describing the path ","enter an adjective describing the jewellery "]
            self.hints=d
        if self.ii==5:
            e=["enter an adjective ","enter a name  ","enter a verb ","enter an adjective ",'enter a noun ','enter a verb   ']
            self.hints=e

        self.input = []

        # Create TextInput with first hint
        self.text_input = TextInput(hint_text=self.hints[self.current_hint_index])
        self.add_widget(self.text_input)

        # Create 'Next' button
        self.next_button = Button(text='Next')
        self.next_button.bind(on_press=self.next_input)
        self.add_widget(self.next_button)

        self.next_label = Label(text='story')
        self.add_widget(self.next_label)

        self.next_button1 = Button(text='Display content')
        self.next_button1.bind(on_press=self.adven)
        self.add_widget(self.next_button1)

    def next_input(self, instance):
        # Get current text from TextInput
        current_text = self.text_input.text

        # Store current text in inputs dictionary with current hint as key
        self.input.append(current_text)

        # Move to next hint
        self.current_hint_index += 1

        # If there are more hints, update the TextInput hint and clear the text
        if self.current_hint_index < len(self.hints):
            self.text_input.hint_text = self.hints[self.current_hint_index]
            self.text_input.text = ''
        else:
            # If there are no more hints, disable the TextInput and Next button
            self.text_input.hint_text = 'All inputs completed'
            self.text_input.disabled = True
            self.next_button.disabled = True
            # Print inputs to console
            print(self.input)
            print(len(self.input))
            s=self.input


    def adven(self,inputs):

        i=self.ii
        if i == 1:
            self.next_label.text=f" Once upon a time, there was a {self.input[0]} adventurer named {self.input[1]}. {self.input[1]} had always dreamed of {self.input[2]}ing to the top of the tallest {self.input[3]} in the world. After months of training and preparation, {self.input[1]} set out on their journey. As they climbed higher and higher, they faced countless {self.input[4]} challenges and nearly gave up many times. But in the end, they persevered and finally reached the summit, where they were greeted by a {self.input[4]} view that took their breath away."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i==2:
            self.next_label.text =f"In a distant galaxy, a {self.input[0]} spaceship captain named {self.input[1]} and their trusty crew embarked on a mission to {self.input[2]} a new planet for colonization. But when they arrived, they found that the planet was already inhabited by {self.input[3]} creatures who were not too happy about the visitors. {self.input[1]} and their crew had to use all their skills and quick thinking to {self.input[4]} their way out of danger and make it back to their spaceship in one piece."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i==3:
            self.next_label.text =f"In a post-apocalyptic world, a {self.input[0]} survivor named {self.input[1]} set out on a mission to {self.input[2]} the last remaining oasis on earth. {self.input[1]} had to brave dangerous {self.input[3]} terrain and fight off hordes of {self.input[4]} creatures along the way. But as they finally reached the oasis, they realized that they were not alone. Other survivors had also made it there, and together they formed a new community and vowed to {self.input[5]} to rebuild what was left of their world."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i==4:
            self.next_label.text =f"Deep in the Amazon rainforest, a {self.input[0]} explorer named {self.input[1]} set out on a mission to find a lost city of gold. As they {self.input[2]}ed through the dense jungle, they faced all sorts of {self.input[3]} obstacles, from treacherous rivers to venomous snakes. But finally, they stumbled upon the city, where they discovered not just gold, but also a {self.input[4]} artifact that held the key to unlocking the secrets of the ancient civilization."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i==5:
            self.next_label.text =print(f"In a world of magic, a {self.input[0]} wizard named {self.input[1]} set out on a quest to {self.input[2]} a powerful artifact that was said to grant unlimited power to whoever possessed it. Along the way, they faced many {self.input[3]} challenges and battled fierce monsters with their trusty {self.input[4]}. But in the end, they found the artifact and realized that it came with a great responsibility. {self.input[1]} used their newfound powers to {self.input[5]} the world and ensure that it was a better place for all.")

            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]

# fantasyy
class screen3(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super(screen3, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.current_hint_index = 0
        self.ii = random.randrange(1, 6)

        if self.ii == 1:
            a = ['Enter an adjective', 'Enter a noun:', 'Enter a name:', 'Enter a adjective (describing things):',"enter a noun ","Enter a place: " ,'Enter a adjective (describing powers):','Enter an verb with ing form:','enter a noun (with ing form):','enter a verb:','enter an adjective:','enter an adjective describing a wild creature: ',"A noun: "]
            self.hints = a
        if self.ii == 2:
            b = ["enter an adjective  ", "enter a noun ", "enter a name ",
                 "enter an verb with ing form ", "enter an adjective describing an animal ",'enter an adjective ','enter an adjective describing a human ','enter an adjective describing an animal','enter an verb in ing form ','enter an adjective ']
            self.hints = b
        if self.ii == 3:
            c = ['enter a noun  ', "enter a name ", "enter an adjective describing the name ", "enter an adjective describing a living thing ",
                 "enter a noun ", "enter a verb ",'enter a noun','enter your fav place','name a body part','enter an adjective ']
        if self.ii == 4:
            d = ["enter an adjective  ", "enter a noun ", "enter a name ",
                 "enter a verb (ending with -ing) ", "enter an adjective ",'enter a noun ','enter a verb','enter an adjective ']
            self.hints = d
        if self.ii == 5:
            e = ["enter an adjective ", "enter an adjective  ", "enter a an adjective ", "enter a noun ", 'enter a name ',
                 'enter an adjective','enter an adjective','enter a noun','enter a noun','enter an adjective','enter a noun','enter an adjective ','enter a place','enter a noun ','enter an adjective']
            self.hints = e

        self.input = []

        # Create TextInput with first hint
        self.text_input = TextInput(hint_text=self.hints[self.current_hint_index])
        self.text_input.pos_hint ={'center_x':.5,'center_y':.9}
        self.add_widget(self.text_input)

        # Create 'Next' button
        self.next_button = Button(text='Next')
        self.next_button.bind(on_press=self.next_input)
        self.add_widget(self.next_button)

        self.next_label = Label(text='story')
        self.add_widget(self.next_label)

        self.next_button1 = Button(text='Display content')
        self.next_button1.bind(on_press=self.fantasy)
        self.add_widget(self.next_button1)

    def next_input(self, instance):
        # Get current text from TextInput
        current_text = self.text_input.text

        # Store current text in inputs dictionary with current hint as key
        self.input.append(current_text)

        # Move to next hint
        self.current_hint_index += 1

        # If there are more hints, update the TextInput hint and clear the text
        if self.current_hint_index < len(self.hints):
            self.text_input.hint_text = self.hints[self.current_hint_index]
            self.text_input.text = ''
        else:
            # If there are no more hints, disable the TextInput and Next button
            self.text_input.hint_text = 'All inputs completed'
            self.text_input.disabled = True
            self.next_button.disabled = True
            # Print inputs to console
            print(self.input)
            print(len(self.input))
            s = self.input


    def fantasy(self,inputs):
        i = self.ii
        if i == 1:
            self.next_label.text=f"In a far-off land, a {self.input[0]} {self.input[1]} named {self.input[2]} set out on a quest to find the {self.input[3]} {self.input[4]} of {self.input[5]}. {self.input[2]} had heard that whoever possessed the {self.input[4]} would be granted {self.input[6]} powers beyond their wildest dreams. After many days of {self.input[7]}ing through treacherous mountains and {self.input[8]}ing across vast plains, {self.input[2]} finally reached the {self.input[5]} where the {self.input[4]} was said to be kept. But {self.input[2]} soon realized that the journey was far from over, as they would have to {self.input[9]} their way through countless {self.input[10]} obstacles and defeat the {self.input[11]} {self.input[12]} guarding the {self.input[4]}."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i==2:
            self.next_label.text =f"Once upon a time, in a magical kingdom far, far away, there was a {self.input[0]} {self.input[1]} named {self.input[2]}. {self.input[2]} had always dreamed of {self.input[3]}ing with dragons, and one day, their wish came true. As {self.input[2]} was {self.input[3]}ing through the forest, they stumbled upon a {self.input[4]} dragon with {self.input[5]} scales and fiery eyes. At first, {self.input[2]} was {self.input[6]}, but soon they realized that the dragon was actually quite {self.input[8]}. They spent the day {self.input[3]}ing through the skies and exploring the kingdom, and when it was time to say goodbye, {self.input[2]} felt a little bit {self.input[9]}, but also grateful for the experience."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i==3:
            self.next_label.text =f"It was a dark and stormy {self.input[0]}. {self.input[1]} was {self.input[2]} because they had heard that a {self.input[3]} {self.input[4]} lived nearby. But {self.input[1]} was determined to {self.input[5]} it, so they grabbed a {self.input[6]} and set out into the stormy night. As they approached the {self.input[4]}'s {self.input[7]}, they could feel their {self.input[8]} beating faster and faster. But when they finally came face to face with the {self.input[3]} creature, {self.input[1]} realized that it was actually quite {self.input[9]}."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i==4:
            self.next_label.text =f"Once upon a time, there was a {self.input[0]} {self.input[1]} named {self.input[2]} who had always been fascinated by the mysterious and {self.input[3]} creatures that lurked in the forest. One day, while {self.input[4]} through the woods, {self.input[2]} stumbled upon a {self.input[3]} {self.input[5]} that promised to take them on a journey to explore the magical world of the forest. As they {self.input[6]} deeper and deeper into the woods, they encountered {self.input[7]} fairies, {self.input[7]} unicorns, and even a {self.input[7]} dragon. When it was time to go back to the human world, {self.input[2]} felt a little bit {self.input[3]}, but also grateful for the experience."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i==5:
            self.next_label.text =f"In a land of {self.input[0]} castles and {self.input[1]} forests, there lived a {self.input[2]} {self.input[3]} named {self.input[4]}. {self.input[4]} had always been fascinated by the tales of brave knights and beautiful princesses, and one day, they decided to set out on a quest to rescue a {self.input[5]} princess from a {self.input[6]} dragon. With nothing but their {self.input[7]} and their courage, {self.input[4]} set out on their journey. Along the way, they encountered {self.input[8]} bandits and had to cross a treacherous {self.input[9]} river. But when they finally arrived at the {self.input[10]} where the dragon was holding the princess captive, they realized that they would have to use their wit and {self.input[11]} to outsmart the {self.input[12]} beast. The {self.input[13]} that {self.input[4]} came up with worked like a charm, and the {self.input[14]} princess was finally free. And {self.input[4]} returned home, hailed as a hero, and with a great story to tell."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]

# mystery
class screen4(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super(screen4, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.current_hint_index = 0
        self.ii = random.randrange(1, 6)
        self.ii = 2
        if self.ii == 1:
            a = ['Enter an adjective', 'Enter a noun:', 'Enter a name:', 'Enter a verb ending with ing:', 'Enter an adjective:','enter a noun','enter a verb ending in ed',"Enter an adjective: "]
            self.hints = a
        if self.ii == 2:
            b = ["Enter an adjective: ","Enter a noun: ","Enter a name: ","Enter a verb ending in 'ing': ","Enter an adjective: ","Enter a noun: ","Enter a verb ending in 'ed': ","Enter an adjective: ","Enter a noun: ","Enter an adjective: ","Enter a noun: ","Enter an adjective: ","Enter a place: ","Enter a noun: ","Enter an adjective: ","Enter a place: ","Enter a noun: ","Enter an adjective: ","Enter a place: ","Enter a noun: ","Enter a verb ending in 'ing': ","Enter an adjective: ","Enter a noun: ","Enter a verb ending in 'ing': ","Enter an adjective: ","Enter a noun: ","Enter a name: ","Enter a verb ending in 'ing': ","Enter an adjective: ","Enter a noun: ","Enter a verb ending in 'ed': ","Enter an adjective: ","Enter a noun: ","Enter an adjective: ","Enter a place: ","Enter a noun: ","Enter a verb ending in 'ing': ","Enter an adjective: ","Enter a noun: ","Enter a verb ending in 'ing': ","Enter an adjective: ","Enter a noun: "]
            self.hints = b
        if self.ii == 3:
            c = ["Enter a name: ","Enter an adjective: ","Enter another adjective: ","Enter a verb ending in 'ing': ","Enter another verb ending in 'ing': ","Enter an adjective: ","Enter another adjective: ","Enter a noun: "]
        if self.ii == 4:
            d = ["Enter an adjective: ","Enter a name: ","Enter an adjective: ","Enter a noun: ","Enter a verb ending in -ing: ","Enter a noun: ","Enter a verb ending in -ing: ","Enter an adjective: ","Enter an adjective: ","Enter a noun: ","Enter an adjective: "]
            self.hints = d
        if self.ii == 5:
            e = ["Enter a name of a detective: ","Enter an adjective: ","Enter an adjective: ","Enter an adjective: ","Enter a verb ending in -ing: ","Enter a verb ending in -ing: ","Enter an adjective: ","Enter a verb ending in -ing: " ]
            self.hints = e

        self.input = []

        # Create TextInput with first hint
        self.text_input = TextInput(hint_text=self.hints[self.current_hint_index])
        self.add_widget(self.text_input)

        # Create 'Next' button
        self.next_button = Button(text='Next')
        self.next_button.bind(on_press=self.next_input)
        self.add_widget(self.next_button)

        self.next_label = Label(text='story')
        self.add_widget(self.next_label)

        self.next_button1 = Button(text='Display content')
        self.next_button1.bind(on_press=self.mystery)
        self.add_widget(self.next_button1)

    def next_input(self, instance):
        # Get current text from TextInput
        current_text = self.text_input.text

        # Store current text in inputs dictionary with current hint as key
        self.input.append(current_text)

        # Move to next hint
        self.current_hint_index += 1

        # If there are more hints, update the TextInput hint and clear the text
        if self.current_hint_index < len(self.hints):
            self.text_input.hint_text = self.hints[self.current_hint_index]
            self.text_input.text = ''
        else:
            # If there are no more hints, disable the TextInput and Next button
            self.text_input.hint_text = 'All inputs completed'
            self.text_input.disabled = True
            self.next_button.disabled = True
            # Print inputs to console
            print(self.input)
            print(len(self.input))
            s = self.input


    def mystery(self,inputs):
        i = self.ii
        if i == 1:
            self.next_label.text=f"Once upon a time, there was a {self.input[0]} {self.input[1]} named {self.input[2]} who had always been fascinated by the mysterious and {self.input[3]} creatures that lurked in the forest. One day, while {self.input[4]} through the woods, {self.input[2]} stumbled upon a {self.input[3]} {self.input[5]} that promised to take them on a journey to explore the magical world of the forest. As they {self.input[6]} deeper and deeper into the woods, they encountered {self.input[7]} fairies, {self.input[7]} unicorns, and even a {self.input[7]} dragon. When it was time to go back to the human world, {self.input[2]} felt a little bit {self.input[7]}, but also grateful for the experience."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        # these two stories are different
        if i == 2:
            self.next_label.text=f"Once upon a time, there was a {self.input[0]} {self.input[1]} named {self.input[2]} who had always been fascinated by the mysterious and {self.input[3]} creatures that lurked in the forest. One day, while {self.input[4]} through the woods, {self.input[2]} stumbled upon a {self.input[5]} {self.input[6]} that promised to take them on a journey to explore the magical world of the forest. As they {self.input[7]} deeper and deeper into the woods, they encountered {self.input[8]} fairies, {self.input[9]} unicorns, and even a {self.input[10]} dragon. When it was time to go back to the human world, {self.input[2]} felt a little bit {self.input[11]}, but also grateful for the experience. They knew they would always cherish their memories of the {self.input[8]} forest and the {self.input[12]} where they had met the {self.input[13]}, {self.input[14]}ing fairies, and the {self.input[9]} unicorns {self.input[15]}ing in the moonlight. And who knows? Maybe one day they would even come face to face with the {self.input[10]} dragon again."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i == 3:
            self.next_label.text=f"Detective {self.input[0]} had always prided themselves on being one step ahead of the game, but this case was different. They had been hired to investigate a {self.input[1]} kidnapping, and all of the clues seemed to lead to a {self.input[2]} dead end. But Detective {self.input[0]} wasn't one to give up easily. They spent countless hours {self.input[3]}ing the crime scene and {self.input[4]}ing the suspects until finally, they cracked the case. The kidnapper was actually the victim's {self.input[5]} twin sibling, who had been {self.input[4]}ing the whole thing in order to collect the ransom money."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i == 4:
            self.next_label.text=f"It was a {self.input[0]} day when Private Eye {self.input[1]} received a mysterious letter in the mail. The letter was written in a {self.input[2]} handwriting and contained only one sentence: 'The {self.input[3]} will be stolen tonight.' Private Eye {self.input[1]} knew they had to act fast. They spent the day {self.input[4]}ing around the city, trying to find the {self.input[3]} in question and {self.input[5]}ing anyone who seemed suspicious. Finally, they stumbled upon a {self.input[6]} thief attempting to steal the {self.input[7]} from a {self.input[8]} museum. Private Eye {self.input[1]} managed to catch the thief just in time, saving the priceless artifact from being lost forever."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i == 5:
            self.next_label.text=f"Detective {self.input[0]} had seen some {self.input[1]} crimes in their time, but this one took the cake. They had been called to investigate a {self.input[2]} murder at a {self.input[3]} mansion, and all of the suspects seemed to be hiding something. But Detective {self.input[0]} wasn't one to back down from a challenge. They spent countless hours {self.input[4]}ing through the evidence and {self.input[5]}ing the suspects until finally, they uncovered the truth. The killer was actually the {self.input[6]} butler, who had been {self.input[7]}ing behind the scenes all along."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]


# crime
class screen5(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super(screen5, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.current_hint_index = 0
        self.ii = random.randrange(1, 6)
        self.ii = 2
        if self.ii == 1:
            a = ["A name: ","An adjective: ","An adjective: ","A noun: ","An adjective: ","A noun: ","An adjective: "]
            self.hints = a
        if self.ii == 2:
            b = ["Enter a name: ","Enter an adjective: ","Enter an adjective: ","Enter a noun: ","Enter an adjective: ","Enter a noun: ","Enter an adjective: ","Enter an adjective: ","Enter an adjective: "]
            self.hints = b
        if self.ii == 3:
            c = ["Enter a name: ","Enter an adjective: ","Enter a noun: ","Enter a verb ending in 'ing': ","Enter an adjective: ","Enter an adjective: ","A noun: ","Enter a verb ending in 'ing': ","Enter an adjective: "]
        if self.ii == 4:
            d = ["Enter an adjective: ","Enter a name: ","Enter an adjective: ","A noun: ","Enter a name: ","Enter an adjective: ","Enter a name: "]
            self.hints = d
        if self.ii == 5:
            e = ["Enter a name: ","Enter an adjective: ","Enter an adjective: ","Enter a name: ","Enter an adjective: ","Enter a noun: ","Enter an adjective: ","A noun: "]
            self.hints = e

        self.input = []

        # Create TextInput with first hint
        self.text_input = TextInput(hint_text=self.hints[self.current_hint_index])
        self.add_widget(self.text_input)

        # Create 'Next' button
        self.next_button = Button(text='Next')
        self.next_button.bind(on_press=self.next_input)
        self.add_widget(self.next_button)

        self.next_label = Label(text='store')
        self.add_widget(self.next_label)

        self.next_button1 = Button(text='Display content')
        self.next_button1.bind(on_press=self.crime)
        self.add_widget(self.next_button1)

    def next_input(self, instance):
        # Get current text from TextInput
        current_text = self.text_input.text

        # Store current text in inputs dictionary with current hint as key
        self.input.append(current_text)

        # Move to next hint
        self.current_hint_index += 1

        # If there are more hints, update the TextInput hint and clear the text
        if self.current_hint_index < len(self.hints):
            self.text_input.hint_text = self.hints[self.current_hint_index]
            self.text_input.text = ''
        else:
            # If there are no more hints, disable the TextInput and Next button
            self.text_input.hint_text = 'All inputs completed'
            self.text_input.disabled = True
            self.next_button.disabled = True
            # Print inputs to console
            print(self.input)
            print(len(self.input))
            s = self.input


    def crime(self,inputs):

        i = self.ii
        if i == 1:
            self.next_label.text = f"It was a dark and stormy night when {self.input[0]}, a notorious {self.input[1]} criminal, decided to pull off the heist of the century. {self.input[0]} had been planning the robbery for months, and they had gathered a team of {self.input[2]} accomplices to help them carry it out. The target was a {self.input[3]} museum, and they were after a priceless {self.input[4]} that had been on display for years. As the storm raged on outside, {self.input[0]} and their crew snuck into the museum, avoided the {self.input[5]} security systems, and made off with the {self.input[6]}. But as they were making their escape, they heard the sound of sirens in the distance, and they knew they were in trouble."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        # these two stories are different
        if i == 2:
            self.next_label.text = f"Detective {self.input[0]} had seen a lot of {self.input[1]} crime scenes in their time, but this one was different. The victim was a {self.input[2]} millionaire who had been found dead in their {self.input[3]} under {self.input[4]} circumstances. As {self.input[0]} began to investigate the crime, they realized that the victim's {self.input[5]} was missing, and they suspected that the killer was after it. As they delved deeper into the case, {self.input[0]} uncovered a web of {self.input[6]} lies, {self.input[7]} secrets, and {self.input[8]} motives. But in the end, they were able to crack the case and bring the killer to justice."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i == 3:
            self.next_label.text = f"It was a sunny day when {self.input[0]}, a {self.input[1]} private investigator, received a new case. A wealthy client had reported that their {self.input[2]} had been stolen, and they wanted {self.input[0]} to find it. As {self.input[0]} began to investigate the case, they realized that the theft was just the tip of the iceberg. The client had been {self.input[3]} with some {self.input[4]} characters, and they had gotten involved in a {self.input[5]} scheme that could have serious consequences. But with their quick wit and {self.input[6]} detective skills, {self.input[0]} was able to solve the case and put an end to the scheme."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i == 4:
            self.next_label.text = f"In the heart of the city, a {self.input[0]} gang ruled the streets with an iron fist. The leader, known only as {self.input[1]}, was a {self.input[2]} mastermind who had built an empire on the profits of their {self.input[3]}. But their reign of terror came to an end when a new detective, {self.input[4]}, arrived on the scene. {self.input[4]} was determined to take down the gang and put {self.input[1]} behind bars. They gathered evidence, interviewed witnesses, and slowly but surely, they began to dismantle the gang's operation. In the end, they were able to catch {self.input[1]} red-handed and bring them to justice."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i == 5:
            self.next_label.text = f"It was supposed to be an easy job. {self.input[0]} and their crew were hired to steal a {self.input[1]} jewel from a {self.input[2]} mansion in the suburbs. But as they made their way through the house, they realized that they were not alone. The owner had hired a team of {self.input[3]} security guards to protect their precious possessions, and they were armed to the teeth. A {self.input[4]} shootout ensued, and {self.input[0]} and their crew barely made it out alive. But as they fled the scene, they realized that they had left something behind a clue that could lead the police right to them."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
# fairytail
class screen7(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super(screen7, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.current_hint_index = 0
        self.ii = random.randrange(1, 6)
        self.ii = 2
        if self.ii == 1:
            a = ["Enter an adjective: ","Enter a name: ","Enter an adjective: ","Enter an adjective: ","Enter an adjective: "]
            self.hints = a
        if self.ii == 2:
            b = ["Enter an adjective: ","Enter an adjective: ","Enter a name: ","Enter a verb ","Enter an adjective: ","Enter an adjective: "]
            self.hints = b
        if self.ii == 3:
            c = ["Enter an adjective: ","Enter a name: ","Enter an adjective: ","Enter an adjective: "]
        if self.ii == 4:
            d = ["Enter an adjective: ","Enter an adjective: ","Enter a name: ","Enter a verb ","Enter an adjective: ","Enter an adjective: ","Enter an adjective: ","Enter a verb: ","Enter an adjective: "]
            self.hints = d
        if self.ii == 5:
            e = ["enter an adjective ", "enter a name  ", "enter a verb in ing form ", "enter an adjective ", 'enter a name ',
                 'enter a adjective   ']
            self.hints = e

        self.input = []

        # Create TextInput with first hint
        self.text_input = TextInput(hint_text=self.hints[self.current_hint_index])
        self.add_widget(self.text_input)

        # Create 'Next' button
        self.next_button = Button(text='Next')
        self.next_button.bind(on_press=self.next_input)
        self.add_widget(self.next_button)

        self.next_label = Label(text='story')
        self.add_widget(self.next_label)

        self.next_button1 = Button(text='Display content')
        self.next_button1.bind(on_press=self.fairytail)
        self.add_widget(self.next_button1)

    def next_input(self, instance):
        # Get current text from TextInput
        current_text = self.text_input.text

        # Store current text in inputs dictionary with current hint as key
        self.input.append(current_text)

        # Move to next hint
        self.current_hint_index += 1

        # If there are more hints, update the TextInput hint and clear the text
        if self.current_hint_index < len(self.hints):
            self.text_input.hint_text = self.hints[self.current_hint_index]
            self.text_input.text = ''
        else:
            # If there are no more hints, disable the TextInput and Next button
            self.text_input.hint_text = 'All inputs completed'
            self.text_input.disabled = True
            self.next_button.disabled = True
            # Print inputs to console
            print(self.input)
            print(len(self.input))
            s = self.input


    def fairytail(self,inputs):
        i = self.ii
        if i == 1:
            self.next_label.text=f"Once upon a time, in a land far, far away, there lived a {self.input[0]} princess named {self.input[1]}. {self.input[1]} lived in a {self.input[2]} castle with her {self.input[3]} parents, the king and queen. But one day, an {self.input[4]} dragon attacked the kingdom, and the king and queen were unable to defeat it. So {self.input[1]} set out on a quest to find the {self.input[4]} sword that would help her defeat the dragon and save the kingdom."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        # these two stories are different
        if i == 2:
            self.next_label.text=f"In a small village nestled at the foot of a {self.input[0]} mountain, there lived a {self.input[1]} girl named {self.input[2]}. {self.input[2]} lived with her {self.input[3]} grandmother in a cozy little cottage. One day, while {self.input[4]}ing through the forest, {self.input[2]} stumbled upon a {self.input[5]} cottage made of gingerbread and candy. But when she tried to take a bite of the house, she realized that it was actually the home of a {self.input[1]} witch who wanted to eat her!"
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i == 3:
            self.next_label.text=f"Long ago, in a land of myth and legend, there was a {self.input[0]} knight named {self.input[1]}. {self.input[1]} was on a quest to rescue the {self.input[2]} princess who had been captured by a {self.input[3]} dragon. But when {self.input[1]} arrived at the dragon's lair, they realized that the princess had already escaped and was now living in a {self.input[0]} castle on the other side of the kingdom."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i == 4:
            self.next_label.text=f"Once upon a time, in a kingdom ruled by a {self.input[0]} king, there was a {self.input[1]} fairy named {self.input[2]}. {self.input[2]} had the power to grant wishes, but only to those who were {self.input[3]} and {self.input[4]} at heart. One day, a {self.input[5]} man came to {self.input[2]} and asked for wealth and power, but {self.input[2]} refused, knowing that he was not truly {self.input[6]} or {self.input[4]}. But when a {self.input[7]} girl came to {self.input[2]} and asked for the ability to {self.input[8]} and make the world a better place, {self.input[2]} granted her wish and the kingdom was forever changed for the better."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]
        if i == 5:
            self.next_label.text=f"In a kingdom far, far away, there was a {self.input[0]} prince named {self.input[1]}. {self.input[1]} had everything he could ever want, except for true love. One day, while {self.input[2]} in the forest, {self.input[1]} stumbled upon a {self.input[3]} cottage where he met a {self.input[4]} girl named {self.input[5]}. The two of them fell in love and lived happily ever after, despite the objections of the {self.input[3]} witch who had cursed the girl to live in the forest."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = 2
            self.next_label.height = self.next_label.texture_size[1]


Builder.load_string(
"""
<screen1>:
    FloatLayout:
        Image:
            source:r"C:\\Users\postm\Downloads\A_black_image.jpg.webp"
            allow_stretch:True
            keep_ratio:False
        Label:
            text:'Select Genre'
            id:genere
            size_hint:.3,.08
            pos_hint:{'center_x':.5,'center_y':.9}
        Button:
            background_normal:r"C:\\Users\\postm\\Downloads\\adventure3.jpg"
            background_down:'white'
            size_hint:.3,.3
            pos_hint:{'center_x':.3,'center_y':.4}
            on_press:
                root.manager.transition.direction='left'
                root.manager.current='screeneight'

        Button:
            background_normal:r"C:\\Users\\postm\\Downloads\\fantasy.jpg"
            size_hint:.3,.2
            background_down:'white'
            pos_hint:{'center_x':.7,'center_y':.4}
            on_press:
                root.manager.transition.direction='left'
                root.manager.current='screenthree'
        Button:
            background_normal:r"C:\\Users\postm\OneDrive\Pictures\Screenshots\Screenshot 2023-06-08 232615.png"
            size_hint:.3,.2
            background_down:'white'
            pos_hint:{'center_x':.3,'center_y':.7}
            on_press:
                root.manager.transition.direction='left'
                root.manager.current='screenfour'
        Button:
            background_normal:r"C:\\Users\\postm\\Downloads\\crime.jpg"
            size_hint:.3,.2
            background_down:'white'
            pos_hint:{'center_x':.7,'center_y':.7}
            on_press:
                root.manager.transition.direction='left'
                root.manager.current='screenfive'
        Button:
            background_normal:r"C:\\Users\\postm\\Downloads\\fairytail1.jpg"
            background_down:'white'
            size_hint:.4,.2
            pos_hint:{'center_x':.5,'center_y':.15}
            on_press:
                root.manager.transition.direction='left'
                root.manager.current='screenseven'
<screen3>:
    FloatLayout:
        # Image:
        #     source:r"C:\\Users\\postm\\Downloads\\plain.jpg"
        #     allow_stretch:True
        #     keep_ratio:False
        Button:
            text:'back'
            size_hint:.15,.08
            id:cbtn
            background_color:'orange'
            pos_hint:{'center_x':.1,'center_y':.8}
            on_press:
                root.manager.transition.direction='right'
                root.manager.current='screenone'

<screen4>:
    FloatLayout:
        # Image:
        #     source:r"C:\\Users\\postm\\Downloads\\plain.jpg"
        #     allow_stretch:True
        #     keep_ratio:False
        Label:

            id:genere
            size_hint:.3,.08
            pos_hint:{'center_x':.1,'center_y':.8}
        Button:
            text:'back'
            size_hint:.15,.08
            id:cbtn
            background_color:'orange'
            pos_hint:{'center_x':.1,'center_y':.8}
            on_press:
                root.manager.transition.direction='right'
                root.manager.current='screenone'

<screen5>:
    FloatLayout:
        # Image:
        #     source:r"C:\\Users\\postm\\Downloads\\plain.jpg"
        #     allow_stretch:True
        #     keep_ratio:False
        Label:

            id:genere
            size_hint:.3,.08
            pos_hint:{'center_x':.1,'center_y':.8}
        Button:
            text:'back'
            size_hint:.15,.08
            id:cbtn
            background_color:'orange'
            pos_hint:{'center_x':.1,'center_y':.8}
            on_press:
                root.manager.transition.direction='right'
                root.manager.current='screenone'
<screen7>:
    FloatLayout:
        # Image:
        #     source:r"C:\\Users\\postm\\Downloads\\plain.jpg"
        #     allow_stretch:True
        #     keep_ratio:False
        Label:

            id:genere
            size_hint:.3,.08
            pos_hint:{'center_x':.1,'center_y':.8}
        Button:
            text:'back'
            size_hint:.15,.08
            id:cbtn
            background_color:'orange'
            pos_hint:{'center_x':.1,'center_y':.8}
            on_press:
                root.manager.transition.direction='right'
                root.manager.current='screenone'

<MyBoxLayout>:
    FloatLayout:
        # Image:
        #     source:r"C:\\Users\\postm\\Downloads\\plain.jpg"
        #     allow_stretch:True
        #     keep_ratio:False
        Label:
            id:genere
            size_hint:.3,.08
            pos_hint:{'center_x':.1,'center_y':.8}
        Button:
            text:'back'
            size_hint:.15,.08
            id:cbtn
            background_color:'orange'
            pos_hint:{'center_x':.1,'center_y':.8}
            on_press:
                root.manager.transition.direction='right'
                root.manager.current='screenone'


"""
)
sm = ScreenManager()
sm.add_widget(screen1(name='screenone'))
sm.add_widget(screen2(name='screentwo'))
sm.add_widget(screen3(name='screenthree'))
sm.add_widget(screen4(name='screenfour'))
sm.add_widget(screen5(name='screenfive'))
sm.add_widget(screen7(name='screenseven'))
sm.add_widget(MyBoxLayout(name='screeneight'))
class bothApp(App):
    def build(self):
        return sm
myApp = bothApp()
myApp.run()