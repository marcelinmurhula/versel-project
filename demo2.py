from manim import *
class BinarySearchDemo(Scene):
    def construct(self):
        title = Text('Binary Search Algorithm', color=GREEN)
        self.play(Write(title))
        self.wait(2)
        # Add binary search animation
        success = Text('Computer Science Demo!', color=GREEN)
        self.play(Write(success))
        self.wait(2)
