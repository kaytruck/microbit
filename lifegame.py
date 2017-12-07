from microbit import *

# initialization data
init_data = "01000" \
            "00110" \
            "11000" \
            "00100" \
            "00000"

#current_data = [
#        False, True,  False,  False, False,
#        False, False, True,   True,  False,
#        True,  True,  False,  False, False,
#        False, False, True,   False, False,
#        False, False, False,  False, False,
#        ]

def draw(data_str):
    canvas_array = []
    for i in range(0, len(data_str)):
        if data_str[i] == '1':
            canvas_array.append('5')
        else:
            canvas_array.append('0')
        if i % 5 == 4 and i != len(data_str) - 1:
            # insert ':' into every end of line
            canvas_array.append(':')

    canvas_str = ''.join(canvas_array)
    image = Image(canvas_str)
    display.show(image)
    
def next_age(current_data):
    next_data = []
    for i in range(0, len(current_data)):
        # check around cell
        neighbor = 0
        if i % 5 != 0:
            # left
            if current_data[i - 1] == '1':
                neighbor += 1
            # up left
            if i > 4 and current_data[i - 6] == '1':
                neighbor += 1
            # down left
            if len(current_data) - i > 4 and current_data[i + 4] == '1':
                neighbor += 1
        if i > 4:
            # up
            if current_data[i - 5] == '1':
                neighbor += 1
        if i % 5 != 4:
            # right
            if current_data[i + 1] == '1':
                neighbor += 1
            # up right
            if i > 4 and current_data[i - 4] == '1':
                neighbor += 1
            # down right
            if len(current_data) - i > 7 and current_data[i + 6] == '1':
                neighbor += 1
        if len(current_data) - i > 5:
            # down
            if current_data[i + 5] == '1':
                neighbor += 1

        # judge next generation 
        if current_data[i] == '0' and neighbor == 3:
            next_data.append('1')
        elif current_data[i] == '1' and (neighbor == 2 or neighbor == 3):
            next_data.append('1')
        elif current_data[i] == '1' and (neighbor == 1 or neighbor == 4):
            next_data.append('0')
        else:
            next_data.append(current_data[i])
    return ''.join(next_data)

current_data = init_data
while True:
    draw(current_data)
    current_data = next_age(current_data)
    sleep(1000)
