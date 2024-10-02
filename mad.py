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

Builder.load_string(
"""
<screen1>:
    FloatLayout:
        Image:
            source:r"C:\\Users\\postm\\Downloads\\plain.jpg"
            allow_stretch:True
            keep_ratio:False
        Label:
            text:'select genere'
            id:genere
            size_hint:.3,.08
            pos_hint:{'center_x':.1,'center_y':.8}
        Button:
            background_normal:r"C:\\Users\\postm\\Downloads\\adv.jpg"
            background_down:'white'
            size_hint:.3,.2
            pos_hint:{'center_x':.3,'center_y':.4}
            on_press:
                root.manager.transition.direction='left'
                root.manager.current='screeneight'
        Button:
            background_normal:r"C:\\Users\\postm\\Downloads\\adv.jpg"
            size_hint:.3,.2
            background_down:'white'
            pos_hint:{'center_x':.7,'center_y':.4}
            on_press:
                root.manager.transition.direction='left'
                root.manager.current='screenthree'
        Button:
            background_normal:r"C:\\Users\\postm\\Downloads\\adv.jpg"
            size_hint:.3,.2
            background_down:'white'
            pos_hint:{'center_x':.3,'center_y':.7}
            on_press:
                root.manager.transition.direction='left'
                root.manager.current='screenfour'
        Button:
            background_normal:r"C:\\Users\\postm\\Downloads\\adv.jpg"
            size_hint:.3,.2
            background_down:'white'
            pos_hint:{'center_x':.7,'center_y':.7}
            on_press:
                root.manager.transition.direction='left'
                root.manager.current='screenfive'




<screen3>:
    FloatLayout:
        Image:
            source:r"C:\\Users\\postm\\Downloads\\plain.jpg"
            allow_stretch:True
            keep_ratio:False
        Label:
            text:'select genere'
            id:genere
            size_hint:.3,.08
            pos_hint:{'center_x':.1,'center_y':.8}
        Button:
            text:'back'
            size_hint:.15,.08
            id:cbtn
            background_color:'orange'
            pos_hint:{'center_x':.4,'center_y':.2}
            on_press:
                root.manager.transition.direction='right'
                root.manager.current='screenone'

<screen4>:
    FloatLayout:
        Image:
            source:r"C:\\Users\\postm\\Downloads\\plain.jpg"
            allow_stretch:True
            keep_ratio:False
        Label:
            text:'select genere'
            id:genere
            size_hint:.3,.08
            pos_hint:{'center_x':.1,'center_y':.8}
        Button:
            text:'back'
            size_hint:.15,.08
            id:cbtn
            background_color:'orange'
            pos_hint:{'center_x':.4,'center_y':.2}
            on_press:
                root.manager.transition.direction='right'
                root.manager.current='screenone'

<screen5>:
    FloatLayout:
        Image:
            source:r"C:\\Users\\postm\\Downloads\\plain.jpg"
            allow_stretch:True
            keep_ratio:False
        Label:
            text:'select genere'
            id:genere
            size_hint:.3,.08
            pos_hint:{'center_x':.1,'center_y':.8}
        Button:
            text:'back'
            size_hint:.15,.08
            id:cbtn
            background_color:'orange'
            pos_hint:{'center_x':.4,'center_y':.2}
            on_press:
                root.manager.transition.direction='right'
                root.manager.current='screenone'
<screen6>:
    FloatLayout:
        Image:
            source:r"C:\\Users\\postm\\Downloads\\plain.jpg"
            allow_stretch:True
            keep_ratio:False
        Label:
            text:'select genere'
            id:genere
            size_hint:.3,.08
            pos_hint:{'center_x':.1,'center_y':.8}
        Button:
            text:'back'
            size_hint:.15,.08
            id:cbtn
            background_color:'orange'
            pos_hint:{'center_x':.4,'center_y':.2}
            on_press:
                root.manager.transition.direction='right'
                root.manager.current='screenone'


"""
)

class screen1(Screen):
    pass
class screen2(Screen):
    pass
class MyBoxLayout(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.current_hint_index = 0
        self.hints = ['Enter an adjective:','Enter a name:','Enter a verb:','Enter a noun:','Enter an adjective2:']
        self.inputs = []

        # Create TextInput with first hint
        self.text_input = TextInput(hint_text=self.hints[self.current_hint_index])
        self.add_widget(self.text_input)

        popup = Popup(title='Your Story', content=self.text_input, size_hint=(0.8, 0.8))

        # Open the popup
        popup.open()

        # Create 'Next' button
        self.next_button = Button(text='Next')
        self.next_button.bind(on_press=self.next_input)
        self.add_widget(self.next_button)

        self.next_label = Label(text='store')
        self.add_widget(self.next_label)

        self.next_button1 = Button(text='Next1')
        self.next_button1.bind(on_press=self.adven)
        self.add_widget(self.next_button1)

    def next_input(self, instance):
        # Get current text from TextInput
        current_text = self.text_input.text

        # Store current text in inputs dictionary with current hint as key
        self.inputs.append(current_text)

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
            print(self.inputs)
            print(len(self.inputs))
            s=self.inputs


    def adven(self,inputs):
        i = random.randrange(1, 6)
        i=1
        if i == 1:
            self.next_label.text=f" Once upon a time, there was a {self.inputs[0]} adventurer named {self.inputs[1]}. {self.inputs[1]} had always dreamed of {self.inputs[2]}ing to the top of the tallest {self.inputs[3]} in the world. After months of training and preparation, {self.inputs[1]} set out on their journey. As they climbed higher and higher, they faced countless {self.inputs[4]} challenges and nearly gave up many times. But in the end, they persevered and finally reached the summit, where they were greeted by a {self.inputs[4]} view that took their breath away."
            self.next_label.text_size = (self.next_label.width, None)
            self.next_label.size_hint_y = None
            self.next_label.height = self.next_label.texture_size[1]


class screen3(Screen):
    pass
class screen4(Screen):
    pass
class screen5(Screen):
    pass
class screen6(Screen):
    pass
class screen7(Screen):
    pass






sm = ScreenManager()
sm.add_widget(screen1(name='screenone'))
sm.add_widget(screen2(name='screentwo'))
sm.add_widget(screen3(name='screenthree'))
sm.add_widget(screen4(name='screenfour'))
sm.add_widget(screen5(name='screenfive'))
sm.add_widget(screen6(name='screensix'))
sm.add_widget(screen7(name='screenseven'))
sm.add_widget(MyBoxLayout(name='screeneight'))
class bothApp(App):
    def build(self):
        return sm
myApp = bothApp()
myApp.run()