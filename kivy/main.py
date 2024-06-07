from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.top_grid = BoxLayout(orientation='vertical')
        self.top_grid.add_widget(Label(text="Имя: "))
        self.name_input = TextInput(multiline=False)
        self.top_grid.add_widget(self.name_input)

        self.top_grid.add_widget(Label(text="Возраст: "))
        self.age_input = TextInput(multiline=False)
        self.top_grid.add_widget(self.age_input)

        self.top_grid.add_widget(Label(text="Email: "))
        self.email_input = TextInput(multiline=False)
        self.top_grid.add_widget(self.email_input)

        self.layout.add_widget(self.top_grid)
        self.submit_button = Button(text="Отправить")
        self.submit_button.bind(on_press=self.submit_data)
        self.layout.add_widget(self.submit_button)

        self.add_widget(self.layout)

    def submit_data(self, instance):
        name = self.name_input.text
        age = self.age_input.text
        email = self.email_input.text
        self.manager.get_screen('second').display_data(name, age, email)
        self.manager.current = 'second'

class Second(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

    def display_data(self, name, age, email):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text=f'Привет, {name}! Тебе {age} лет. Твой email: {email}'))

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(Second(name='second'))
        return sm

if __name__ == '__main__':
    MyApp().run()
