import tkinter as tk
import random
from pygame import mixer
import threading

mixer.init()

meow_files = ['meow1.mp3', 'meow2.mp3', 'meow3.mp3']

behaviors = [
    "is napping in the sun",
    "is the cat feel boring",
    "is the cat telling something",
    "is chasing a laser pointer",
    "is scratching the furniture",
    "is eating some treats",
    "is playing with a ball of yarn",
    "is sitting on a customer's lap",
    "is staring out the window",
    "is climbing the cat tree",
    "is hiding under a table",
    "is knocking things off a shelf"
]

def play_meow():
    random_meow = random.choice(meow_files)
    mixer.Sound(random_meow).play()

def display_behavior(label):
    behavior = random.choice(behaviors)
    label.config(text=f"A cat {behavior}")
    root.after(3000, lambda: display_behavior(label))
    play_meow()

root = tk.Tk()
root.title("Virtual Cat Cafe")
root.geometry("500x300")

behavior_label = tk.Label(root, text="", font=("Helvetica", 16))
behavior_label.pack(expand=True, pady=20)

display_behavior(behavior_label)

root.mainloop()

mixer.quit()
