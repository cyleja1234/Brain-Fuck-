#brain fuck+ by unknown81311#6616 & NotGrey#2415
debug = False# if you are cool
pc, pointer, pointerTwo = 0, 0, 0
WIDTH, HEIGHT = 20, 20
grid= [[0] * WIDTH for _ in range(HEIGHT)]# make grid

code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."# set code here, here is an example

while pc < len(code):# loop over code
    if code[pc] == "<":# <
        pointer = (pointer - 1) % WIDTH
    elif code[pc] == ">":# >
        pointer = (pointer + 1) % WIDTH
    elif code[pc] == "V":# V
        pointerTwo = (pointerTwo - 1) % HEIGHT
    elif code[pc] == "^":# ^
        pointerTwo = (pointerTwo + 1) % HEIGHT
    elif code[pc] == "-":# -
        grid[pointerTwo][pointer] = (grid[pointerTwo][pointer] - 1) % 256
    elif code[pc] == "+":# +
        grid[pointerTwo][pointer] = (grid[pointerTwo][pointer] + 1) % 256

    elif code[pc] == "[":# [
        if grid[pointerTwo][pointer] == 0:
            pairs = 1
            while pairs or code[pc] != "]":
                pc = pc + 1
                if code[pc] == "[":
                    pairs += 1
                elif code[pc] == "]":
                    pairs -= 1

    elif code[pc] == "]":# ]
        if grid[pointerTwo][pointer] != 0:
            pairs = 1
            while pairs or code[pc] != "[":
                pc = pc - 1
                if code[pc] == "]":
                    pairs += 1
                elif code[pc] == "[":
                    pairs -= 1

    elif code[pc] == "`":# `
        var = map(ord, input())
        for char in var:
            grid[pointerTwo][pointer] = char
            pointerTwo = pointerTwo - 1
    elif code[pc] == ".":# .
        print(chr(grid[pointerTwo][pointer]), end='')
    elif code[pc] == ",":# ,
        grid[pointerTwo][pointer] = ord(input()[])

    pc = pc + 1

    if debug == True:# if you are cool
        print (grid," ", code[pc-1])
