from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager

class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.ni_input = TextInput(text='5', multiline=False)
        layout.add_widget(Label(text='Enter an odd number for line size:'))
        layout.add_widget(self.ni_input)

        self.vt_input = TextInput(text='*', multiline=False)
        layout.add_widget(Label(text='Enter 3 signs to design:'))
        layout.add_widget(self.vt_input)

        self.mj_input = TextInput(text='Hello', multiline=False)
        layout.add_widget(Label(text='Enter your desired center word:'))
        layout.add_widget(self.mj_input)

        button = Button(text="Generate Pattern", on_press=self.on_generate_pattern)
        layout.add_widget(button)

        self.add_widget(layout)

    def on_generate_pattern(self, instance):
        ni = int(self.ni_input.text)
        vt = self.vt_input.text
        mj = self.mj_input.text

        pattern = self.generate_your_pattern(ni, vt, mj)

        # Switch to the PatternScreen and pass the pattern to it
        self.manager.get_screen('pattern').update_pattern(pattern)
        self.manager.current = 'pattern'

    def generate_your_pattern(self, ni, vt, mj):
        # Your existing pattern generation code goes here
        pattern_lines = []
        for i in range(1, ni, 2):
            pattern_lines.append((vt * i).center(ni * 3, "-"))
        pattern_lines.append(mj.center(ni * 3, '-'))
        for i in range(ni - 2, 0, -2):
            pattern_lines.append((vt * i).center(ni * 3, "-"))
        return '\n'.join(pattern_lines)

class PatternScreen(Screen):
    def __init__(self, **kwargs):
        super(PatternScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.pattern_label = Label(text='', halign='center', valign='middle', font_size='20sp')
        layout.add_widget(self.pattern_label)

        button = Button(text="Back to Input", on_press=self.on_back_to_input)
        layout.add_widget(button)

        self.add_widget(layout)

    def update_pattern(self, pattern):
        self.pattern_label.text = pattern

    def on_back_to_input(self, instance):
        # Switch back to the InputScreen
        self.manager.current = 'input'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        input_screen = InputScreen(name='input')
        pattern_screen = PatternScreen(name='pattern')
        sm.add_widget(input_screen)
        sm.add_widget(pattern_screen)
        return sm

if __name__ == '__main__':
    MyApp().run()
