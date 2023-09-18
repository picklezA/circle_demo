# version: 0.0.3
# author: picklez
# purpose: just to test the creation of a circle function and the display of stuff

import numpy
import math
import tkinter
from PIL import Image,ImageTk
from tqdm import tqdm
import time

height = 900
width = 900

# remember that numpy stuff uses [y,x]

class Gen:
    def line(point1, point2):
        all_points_between = []
        dtop = point2[0] - point1[0]
        dbot = point2[1] - point1[1]
        m = dtop / (dbot + 0.0000000000000001)
        b = point1[0] - (m * point1[1])
        if point1[1] < point2[1]:
            for i in range(point1[1], point2[1]):
                hy = (m*i)+b
                hy = round(hy, 2)
                hy = math.trunc(hy)
                hold = [int(hy), int(i)]
                all_points_between.append(hold)
            if point1[0] < point2[0]:
                for j in range(point1[0], point2[0]):
                    hx = (j-b)/m
                    hx = round(hx, 2)
                    hx = math.trunc(hx)
                    hold = [int(j), int(hx)]
                    all_points_between.append(hold)
            if point1[0] > point2[0]:
                for j in range(point2[0], point1[0]):
                    hx = (j-b)/m
                    hx = round(hx, 2)
                    hx = math.trunc(hx)
                    hold = [int(j), int(hx)]
                    all_points_between.append(hold)
        if point1[1] > point2[1]:
            for i in range(point2[1],point1[1]):
                hy = (m*i)+b
                hy = math.trunc(hy)
                hold = [int(hy), int(i)]
                all_points_between.append(hold)
            if point1[0] < point2[0]:
                for j in range(point1[0], point2[0]):
                    hx = (j-b)/m
                    hx = round(hx, 2)
                    hx = math.trunc(hx)
                    hold = [int(j), int(hx)]
                    all_points_between.append(hold)
            if point1[0] > point2[0]:
                for j in range(point2[0], point1[0]):
                    hx = (j-b)/m
                    hx = round(hx, 2)
                    hx = math.trunc(hx)
                    hold = [int(j), int(hx)]
                    all_points_between.append(hold)
        return all_points_between
        
    def draw_lines(new_image, center1, circle_edge1, center2, circle_edge2, center3, circle_edge3):
        all_images = []
        # revolutions: c1=6, c2=3, c3=2
        frame_number = len(circle_edge1 * 6)
        c1_line = Gen.line(center1, circle_edge1[0])
        c2_line = Gen.line(center2, circle_edge2[0])
        c3_line = Gen.line(center3, circle_edge3[0])
        original_copy = new_image.copy()
        for i in tqdm(range(frame_number)):
            new_image = original_copy.copy()
            if i % 1 == 0:
                c1_line = Gen.line(center1, circle_edge1[i%len(circle_edge1)])
            if i % 2 == 0:
                c2_line = Gen.line(center2, circle_edge2[i%len(circle_edge2)])
            if i % 3 == 0:
                c3_line = Gen.line(center3, circle_edge3[i%len(circle_edge3)])
                
            for point1 in c1_line:
                new_image[point1[0]][point1[1]][0] = 255
                new_image[point1[0]][point1[1]][1] = 0
                new_image[point1[0]][point1[1]][2] = 0
            for point2 in c2_line:
                new_image[point2[0]][point2[1]][0] = 0
                new_image[point2[0]][point2[1]][1] = 255
                new_image[point2[0]][point2[1]][2] = 0
            for point3 in c3_line:
                new_image[point3[0]][point3[1]][0] = 0
                new_image[point3[0]][point3[1]][1] = 0
                new_image[point3[0]][point3[1]][2] = 255
            
            all_images.append(new_image)
        return all_images
        
    def circle(radius, center, new_image):
        circle_edge = []
        for i in range(1, 360):
            # calculate opposite side
            opposite = radius * math.sin(math.radians(i))
            # calculate adjacent side
            adjacent = radius * math.cos(math.radians(i))
            # now create an edge point
            edge_point = [int(center[0] + opposite), int(center[1] + adjacent)]
            new_image[int(edge_point[0])][int(edge_point[1])][0] = 255
            new_image[int(edge_point[0])][int(edge_point[1])][1] = 255
            new_image[int(edge_point[0])][int(edge_point[1])][2] = 255
            circle_edge.append(edge_point)
        return new_image, circle_edge
    
def window_on_run(new_image, center1, circle_edge1, center2, circle_edge2, center3, circle_edge3):
    window = tkinter.Tk()
    window.title("Circle Testing")
    window.configure(width=width,height=height)
    window.configure(bg='black')
    winWidth = window.winfo_reqwidth()
    winHeight = window.winfo_reqheight()
    posRight = int(window.winfo_screenwidth() / 2 - winWidth /2)
    posDown = int(window.winfo_screenheight() / 2 - winHeight / 2)
    window.geometry("+{}+{}".format(posRight, posDown))
    
    canvas = tkinter.Canvas(window)
    canvas = tkinter.Canvas(window, width=width, height=height)
    canvas.pack()
    
    # pre-initialized run data
    index = 0
    original_copy = new_image.copy()
    c1_line = Gen.line(center1, circle_edge1[0])
    c2_line = Gen.line(center2, circle_edge2[0])
    c3_line = Gen.line(center3, circle_edge3[0])
    
    while True:
        # do our test to update stuff
        new_image = original_copy.copy()
        if index % 1 == 0:
            c1_line = Gen.line(center1, circle_edge1[index%len(circle_edge1)])
        if index % 2 == 0:
            c2_line = Gen.line(center2, circle_edge2[index%len(circle_edge2)])
        if index % 3 == 0:
            c3_line = Gen.line(center3, circle_edge3[index%len(circle_edge3)])
        # add lines to image
        for point1 in c1_line:
            new_image[point1[0]][point1[1]][0] = 255
            new_image[point1[0]][point1[1]][1] = 0
            new_image[point1[0]][point1[1]][2] = 0
        for point2 in c2_line:
            new_image[point2[0]][point2[1]][0] = 0
            new_image[point2[0]][point2[1]][1] = 255
            new_image[point2[0]][point2[1]][2] = 0
        for point3 in c3_line:
            new_image[point3[0]][point3[1]][0] = 0
            new_image[point3[0]][point3[1]][1] = 0
            new_image[point3[0]][point3[1]][2] = 255
        # display image
        img2 = ImageTk.PhotoImage(image=Image.fromarray((new_image.copy()).astype(numpy.uint8)))
        canvas.create_image(0, 0, anchor=tkinter.NW, image=img2)
        canvas.update()
        index += 1
    
    window.mainloop()
    
# we will pregen a few things before initialization
# first, we need to define the image we are writing too
new_image = numpy.empty((height,width,3))
# then we need to define the center points for the circles we would like to create
center1 = [int(height/2), int(width/2)]
center2 = [int(height/2), int(width/4)]
center3 = [int(height/2), int(3*width/4)]
# next we need to define the outer edges of the circles and also write them to the canvas
new_image, circle_edge1 = Gen.circle(100, center1, new_image)
new_image, circle_edge2 = Gen.circle(100, center2, new_image)
new_image, circle_edge3 = Gen.circle(100, center3, new_image)
# then we need to pass them to the canvas display program so that we can run the animation at run time
window_on_run(new_image, center1, circle_edge1, center2, circle_edge2, center3, circle_edge3)

# Basically this demo just shows really cool stuff with python animations from scratch and also
# the difference in frame rates. It's a pretty cool demo if I say so myself lol