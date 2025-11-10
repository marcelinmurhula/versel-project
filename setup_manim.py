import os

print("Starting VERSEL Manim setup...")

# Create directories
os.makedirs("media/videos", exist_ok=True)
os.makedirs("media/images", exist_ok=True)
print("✅ Directories created")

# Create manim.cfg
config_content = """[CLI]
video_dir = ./media/videos
images_dir = ./media/images

[output]
video_dir = ./media/videos
images_dir = ./media/images
"""

with open("manim.cfg", "w") as f:
    f.write(config_content)
print("✅ manim.cfg created")

# Create simple test animation
test_code = """from manim import *

class TestAnimation(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        self.play(Create(circle))
        text = Text("VERSEL", font_size=36)
        self.play(Write(text))
        self.wait(2)
"""

with open("test_animation.py", "w") as f:
    f.write(test_code)

print("✅ Test animation created")
print("🎉 Setup complete!")
print("Run: python -m manim -ql test_animation.py TestAnimation")
