from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)  # White

class Calculator(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=55,
            background_color=(0.9, 0.9, 0.9, 1),  # Background color of TextInput
            foreground_color=(0, 0, 0, 1)  # Text color
        )
        main_layout.add_widget(self.solution)

#numbers and operators buttons
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)  # Spacing between buttons
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    background_color=self.get_button_color(label),
                    color=(1, 1, 1, 1),  # Text color of the button
                    font_size=24,
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        #backspace button
        backspace_button = Button(
            text="Backspace",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            background_color=(0.9, 0.6, 0, 1),  # Color for backspace button
            color=(1, 1, 1, 1),  # Text color
            font_size=24,
        )
        backspace_button.bind(on_press=self.on_backspace)
        main_layout.add_widget(backspace_button)

        # Add calculate button
        equals_button = Button(
            text="Calculate",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            background_color=(0, 0.7, 0, 1),  # Green color for the "Calculate" button
            color=(1, 1, 1, 1),  # Text color
            font_size=24,
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def get_button_color(self, label):
        #different colors for the buttons
        if label in self.operators:
            return (1, 0.5, 0, 1)  # Orange for operators
        elif label == "C":
            return (1, 0, 0, 1)  # Red for the "C" button
        else:
            return (0.2, 0.6, 0.8, 1)  # Blue for numbers

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear widget
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # Don’t add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text

            self.last_button = button_text
            self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                # Safely evaluate the expression
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception:
                self.solution.text = "Error"

    def on_backspace(self, instance):
        current = self.solution.text
        if current:
            # Remove the last character from the input
            self.solution.text = current[:-1]

if __name__ == '__main__':
    Calculator().run()
