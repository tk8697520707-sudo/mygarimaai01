from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GarimaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        self.label = Label(text="Garima AI Ready", font_size=20)
        self.input = TextInput(hint_text="Kuch puchiye...", multiline=False)
        btn = Button(text="Sawal Puche", size_hint=(1, 0.2))
        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    GarimaApp().run()
