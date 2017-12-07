# Add your Python code here. E.g.
from microbit import *

current_data = [
        False, True,  False,  False, False,
        False, False, True,   True,  False,
        True,  True,  False,  False, False,
        False, False, True,   False, False,
        False, False, False,  False, False,
        ]

def draw(bool_array):
    canvas_array = []
    for i in range(0, len(bool_array)):
        if bool_array[i]:
            canvas_array.append('5')
        else:
            canvas_array.append('0')
        if i % 5 == 4 and i != len(bool_array) - 1:
            canvas_array.append(':')

    canvas_str = ''.join(canvas_array)
    #print(canvas_str)
    canvas = Image(canvas_str)
    display.show(canvas)
    
def next_age(current_data):
    next_data = []
    for i in range(0, len(current_data)):
        neighbor = 0
        if i % 5 != 0:
            # left
            if current_data[i - 1]:
                neighbor += 1
            # up left
            if i > 4 and current_data[i - 6]:
                neighbor += 1
            # down left
            if len(current_data) - i > 4 and current_data[i + 4]:
                neighbor += 1
        if i > 4:
            # up
            if current_data[i - 5]:
                neighbor += 1
        if i % 5 != 4:
            # right
            if current_data[i + 1]:
                neighbor += 1
            # up right
            if i > 4 and current_data[i - 4]:
                neighbor += 1
            # down right
            if len(current_data) - i > 7 and current_data[i + 6]:
                neighbor += 1
        if len(current_data) - i > 5:
            # down
            if current_data[i + 5]:
                neighbor += 1

        if not current_data[i] and neighbor == 3:
            next_data.append(True)
        elif current_data[i] and (neighbor == 2 or neighbor == 3):
            next_data.append(True)
        else:
            next_data.append(False)
    return next_data


while True:
    #display.scroll('Hello, World!')
    #display.show(Image.HEART)
    #display.show(canvas)
    draw(current_data)
    current_data = next_age(current_data)
    sleep(1000)
