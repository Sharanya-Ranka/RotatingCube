import turtle
import time
import math

rotator_win=turtle.Screen()
rotator_turtle=turtle.Turtle()
rotator_turtle.shapesize(0.1,0.1,0)
turtle.delay(0)
rotator_win.tracer(False)
def draw_rotatingcube(points):
        global rotator_win,rotator_turtle
        t=rotator_turtle
        t.clear()
        t.penup()
        t.goto(points[3])
        t.pendown()
        t.goto(points[0])
        t.goto(points[1])
        t.goto(points[2])
        t.goto(points[3])
        t.goto(points[7])
        t.goto(points[6])
        t.goto(points[2])
        t.goto(points[1])
        t.goto(points[5])
        t.goto(points[4])
        t.goto(points[0])
        t.goto(points[3])
        t.pencolor("red")
        t.goto(points[7])
        t.pencolor("black")
        t.goto(points[4])
        t.goto(points[5])
        
        t.goto(points[6])
        
        rotator_win.update()
        
        time.sleep(0)
        
        
                        
                        
        
def rotatingcube(x,y):
        side=100
        s=side
        speed=0.0025
        r2=1.414
        points=[[s/r2,-s/2,0],[0,-s/2,-s/r2],[-s/r2,-s/2,0],[0,-s/2,s/r2],
                [s/r2,s/2,0],[0,s/2,-s/r2],[-s/r2,s/2,0],[0,s/2,s/r2]]
        projected_points=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        pictureplanez=200
        #print("input observer x y z")
        obs_coord=[200,200,1000]
         ##list(map(int,input().split()))
        t=0
        while(True):
                t+=speed
                x=s/r2*math.cos(t)              ##Anticlockwise movement
                z=-s/r2*math.sin(t)             ##x z correspond to first point
                for i in [0,4]:
                        points[i][0]=x
                        points[i][2]=z
                        points[i+1][0]=z
                        points[i+1][2]=-x
                        points[i+2][0]=-x
                        points[i+2][2]=-z
                        points[i+3][0]=-z
                        points[i+3][2]=x
                ## To find projected points
                for i,point in enumerate(points):
                        ratio=((pictureplanez-obs_coord[2])/(point[2]-obs_coord[2]))
                        current_point=projected_points[i]
                        current_point[0]=ratio*(point[0]-obs_coord[0])+obs_coord[0]
                        current_point[1]=ratio*(point[1]-obs_coord[1])+obs_coord[1]

                ##To draw projection
                draw_rotatingcube(projected_points)
                        
                
                
        
        
        
	
        
turtle.onscreenclick(rotatingcube)	
