import time, random, keyboard

paragraph = "Let us learn to appreciate there will be times when the trees will be bare, and look forward to the time when we may pick the fruit."

progress = 0
for i, char in enumerate(paragraph):
    keyboard.write(char)
    progress = (i + 1) / len(paragraph) * 100
    print(f"\rProgress: {progress:.2f}%", end="")
    time.sleep(random.uniform(0.01, 0.05))
