import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label

kivy.require('1.9.0')

class Dovey(App):
    
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint=(0.6,0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}
        
        #add widgets to window
        
        #image widget
        self.window.add_widget(Image(source="GH.jpg"))
        #label widget
        self.greeting = Label(
            text="What is your name?",
            font_size = 16,
            color = "purple",
            
            )
        self.window.add_widget(self.greeting)
        
        #text input
        self.user =TextInput(
            multiline=False,
            padding_y =(15,15),
            size_hint =(1,0.5)
            )
        self.window.add_widget(self.user)
        
        #Button widget
        self.button = Button(
            text="What's up",
            size_hint =(1,0.5),
            bold =True,
            background_color ="violet",
            background_normal = ""
            
            )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        
        
        return self.window
        
        
        
    def callback(self, instance):
        self.greeting.text = "Hi " + self.user.text +"!"
        
        
        
        
        
       
    
if __name__ == "__main__":
    Dovey().run()