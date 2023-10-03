QUOTES =[
    "First, solve the problem. Then, write the code. – John Johnson",
    "Code is like humor. When you have to explain it, it’s bad. – Cory House",
    "The best way to learn to code is to code. Dive in and learn it by doing.",
    "Programming isn't about what you know; it's about what you can figure out.",
    "Every great developer you know got there by solving problems they were unqualified to solve until they did it. – Patrick McKenzie",
    "In the coding journey, every error is a step closer to a solution.",
    "The beautiful thing about learning is that no one can take it away from you. – B.B. King",
    "A year from now, you'll wish you had started today. Start coding!",
    "Code is the next universal language. Embrace the future and learn it!",
    "The road to mastering programming is paved with lines of code and error messages. Keep going!"
]

import random

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex_color

colours = get_random_color()
