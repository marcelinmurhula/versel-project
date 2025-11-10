from manim import *

class FalkirkDemo(Scene):
    def construct(self):
        # Title
        title = Text('VERSEL DEMO: Falkirk Wheel', color=BLUE, font_size=36)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        # Create wheel
        wheel = Circle(radius=2, color=WHITE, stroke_width=4)
        axle = Dot(radius=0.1, color=YELLOW)
        
        # Caissons (water bowls)
        caisson1 = Rectangle(height=1.5, width=1, color=BLUE, fill_opacity=0.5)
        caisson1.move_to(wheel.point_at_angle(45 * DEGREES))
        
        caisson2 = Rectangle(height=1.5, width=1, color=BLUE, fill_opacity=0.5)
        caisson2.move_to(wheel.point_at_angle(225 * DEGREES))
        
        self.play(Create(wheel), Create(axle))
        self.play(Create(caisson1), Create(caisson2))
        self.wait(1)
        
        # Rotate the wheel
        wheel_group = VGroup(wheel, caisson1, caisson2, axle)
        self.play(Rotate(wheel_group, angle=180 * DEGREES, run_time=4))
        self.wait(1)
        
        # Success message
        success = Text('VERSEL Educational Video Complete!', color=GREEN, font_size=24)
        self.play(Write(success))
        self.wait(2)
