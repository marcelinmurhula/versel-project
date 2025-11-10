from manim import *

class TestAnimation(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        self.play(Create(circle))
        text = Text("VERSEL", font_size=36)
        self.play(Write(text))
        self.wait(2)
