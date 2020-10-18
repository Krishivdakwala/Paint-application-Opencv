import cv2
import numpy as np

x_start, y_start, x_end, y_end = 0, 0, 0, 0
xe_start, ye_start, xe_end, ye_end = 0, 0, 0, 0
xc_start, yc_start = 0, 0
move = False
move_e = False
flag1 = False
flag_blue = False
flag_red = False
flag_yellow = False
flag_green = False
img = np.zeros((864, 1536, 3), np.uint8)
img.fill(255)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'DOODLE', (600, 80), font, 3, (0, 0, 255), 2, cv2.LINE_AA)
cv2.putText(img, 'INSTRUCTIONS-', (10, 200), font, 1.5, (50, 205, 50), 2, cv2.LINE_AA)
cv2.putText(img, 'Left Click-->Doodle', (10, 250), font, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'Double Right Click-->New Blank Page', (10, 350), font, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'Press s-->Save Doodle', (10, 400), font, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'Press Esc-->Exit Without Saving', (10, 450), font, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'DOUBLE CLICK TO START!!', (10, 500), font, 1.5, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'Developed by Krishiv Dakwala', (750, 780), font, 1.5, (255, 0, 255), 2, cv2.LINE_AA)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), (255, 255, 255), (0, 0, 0), (148, 0, 211)
          , (220, 220, 220)]
brush_color = colors[5]
x1 = 0
x2 = 0
y1 = 0
y2 = 0
x3 = 0
x4 = 0
y3 = 0
y4 = 0
t2 = 0
t = 0
def_color = colors[4]
brush_size = 5
border_color = colors[5]


def gui():
    global img, colors, x1, x2, y1, y2, x3, x4, y3, y4, t2, brush_color, def_color
    img = cv2.rectangle(img, (160, 1), (255, 65), colors[0], -1)
    img = cv2.rectangle(img, (275, 1), (370, 65), colors[1], -1)
    img = cv2.rectangle(img, (390, 1), (485, 65), colors[2], -1)
    img = cv2.rectangle(img, (505, 1), (600, 65), colors[3], -1)
    img = cv2.rectangle(img, (620, 1), (715, 65), colors[5], -1)
    img = cv2.rectangle(img, (735, 1), (830, 65), colors[7], -1)
    cv2.putText(img, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 2, cv2.LINE_AA)
    cv2.putText(img, "BLACK", (642, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "ERASER", (750, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.rectangle(img, (x1, y1), (x2, y2), def_color, t)
    img = cv2.rectangle(img, (1, 200), (60, 260), colors[7], -1)
    img = cv2.rectangle(img, (1, 262), (60, 320), colors[7], -1)
    img = cv2.rectangle(img, (1, 322), (60, 380), colors[7], -1)
    img = cv2.rectangle(img, (1, 382), (60, 440), colors[7], -1)
    cv2.rectangle(img, (x3, y3), (x4, y4), def_color, t2)
    cv2.circle(img, (30, 230), 5, brush_color, -1)
    cv2.circle(img, (30, 290), 10, brush_color, -1)
    cv2.circle(img, (30, 350), 15, brush_color, -1)
    cv2.circle(img, (30, 410), 20, brush_color, -1)


def click_event(event, x, y, flags, param):
    global x_start, y_start, x_end, y_end, move
    global xe_start, ye_start, xe_end, ye_end, move_e
    global xc_start, yc_start, brush_color, x3, x4, y3, y4, t2
    global img, flag1, x1, x2, y1, y2, t, brush_size, border_color, def_color
    if event == cv2.EVENT_RBUTTONDBLCLK:
        flag1 = True
        img = np.zeros((864, 1536, 3), np.uint8)
        img.fill(255)
        gui()
        cv2.imshow('Doodle', img)
    if event == cv2.EVENT_LBUTTONDOWN and flag1 is True and x in range(160, 244) and y in range(1, 65):
        xc_start, yc_start = x, y
        brush_color = colors[0]
        x1 = 165
        y1 = 6
        x2 = 250
        y2 = 60
        t = 9
        def_color = colors[6]
        gui()
    elif event == cv2.EVENT_LBUTTONDOWN and flag1 is True and x in range(275, 370) and y in range(1, 65):
        xc_start, yc_start = x, y
        brush_color = colors[1]
        x1 = 280
        y1 = 6
        x2 = 365
        y2 = 60
        t = 9
        def_color = colors[6]
        gui()
    elif event == cv2.EVENT_LBUTTONDOWN and flag1 is True and x in range(390, 485) and y in range(1, 65):
        xc_start, yc_start = x, y
        brush_color = colors[2]
        x1 = 395
        y1 = 6
        x2 = 480
        y2 = 60
        t = 9
        def_color = colors[6]
        gui()
    elif event == cv2.EVENT_LBUTTONDOWN and flag1 is True and x in range(505, 600) and y in range(1, 65):
        xc_start, yc_start = x, y
        brush_color = colors[3]
        x1 = 510
        y1 = 6
        x2 = 595
        y2 = 60
        t = 9
        def_color = colors[6]
        gui()
    elif event == cv2.EVENT_LBUTTONDOWN and flag1 is True and x in range(620, 715) and y in range(1, 65):
        xc_start, yc_start = x, y
        brush_color = colors[5]
        x1 = 625
        y1 = 6
        x2 = 710
        y2 = 60
        t = 9
        def_color = colors[6]
        gui()

    elif event == cv2.EVENT_LBUTTONDOWN and flag1 is True and x in range(725, 830) and y in range(1, 65):
        xc_start, yc_start = x, y
        brush_color = colors[4]
        x1 = 740
        y1 = 6
        x2 = 825
        y2 = 60
        t = 9
        def_color = colors[6]
        gui()

    if event == cv2.EVENT_LBUTTONDOWN and flag1 is True and x in range(1, 60) and y in range(200, 260):
        xc_start, yc_start = x, y
        brush_size = 5
        x3 = 4
        y3 = 203
        x4 = 57
        y4 = 257
        t2 = 6
        def_color = colors[6]
        gui()
    elif event == cv2.EVENT_LBUTTONDOWN and flag1 is True and x in range(1, 60) and y in range(260, 320):
        xc_start, yc_start = x, y
        brush_size = 10
        x3 = 4
        y3 = 265
        x4 = 57
        y4 = 317
        t2 = 6
        def_color = colors[6]
        gui()
    elif event == cv2.EVENT_LBUTTONDOWN and flag1 is True and x in range(1, 60) and y in range(320, 380):
        xc_start, yc_start = x, y
        brush_size = 15
        x3 = 4
        y3 = 325
        x4 = 57
        y4 = 377
        t2 = 6
        def_color = colors[6]
        gui()
    elif event == cv2.EVENT_LBUTTONDOWN and flag1 is True and x in range(1, 60) and y in range(380, 440):
        xc_start, yc_start = x, y
        brush_size = 20
        x3 = 4
        y3 = 385
        x4 = 57
        y4 = 437
        t2 = 6
        def_color = colors[6]
        gui()

    if event == cv2.EVENT_LBUTTONDOWN and flag1 is True:
        x_start, y_start, x_end, y_end = x, y, x, y
        move = True
        cv2.circle(img, (x, y), brush_size, brush_color, -1)
        gui()
        cv2.imshow('Doodle', img)

    elif event == cv2.EVENT_MOUSEMOVE and flag1 is True:
        if move is True:
            x_end, y_end = x, y
            cv2.circle(img, (x, y), brush_size, brush_color, -1)
            gui()
            cv2.imshow('Doodle', img)
    elif event == cv2.EVENT_LBUTTONUP and flag1 is True:
        x_end, y_end = x, y
        move = False
    if event == cv2.EVENT_RBUTTONDBLCLK and flag1 is True:
        img = np.zeros((864, 1536, 3), np.uint8)
        img.fill(255)
        gui()
        cv2.imshow('Doodle', img)


cv2.imshow('Doodle', img)

cv2.setMouseCallback('Doodle', click_event)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Doodle.png', img)
    cv2.destroyAllWindows()
