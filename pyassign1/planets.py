import turtle
import math
sun=turtle.Turtle()
sun.color("yellow")
sun.shape("circle")
sun.shapesize(3)

mercury=turtle.Turtle()
mercury.color("blue")
mercury.shape("circle")
mercury.shapesize(0.382)

venus=turtle.Turtle()
venus.color("#ffff24")
venus.shape("circle")
venus.shapesize(0.949)

earth=turtle.Turtle()
earth.color("#90c8ff")
earth.shape("circle")
earth.shapesize(1)

mars=turtle.Turtle()
mars.color("#934a00")
mars.shape("circle")
mars.shapesize(0.53)

jupiter=turtle.Turtle()
jupiter.color("#ffc890")
jupiter.shape("circle")
jupiter.shapesize(3.34)

saturn=turtle.Turtle()
saturn.color("#ffc890")
saturn.shape("circle")
saturn.shapesize(3.07)

mercury.up()
venus.up()
earth.up()
mars.up()
jupiter.up()
saturn.up()

mercury.goto(69.7,0)
venus.goto(109,0)
earth.goto(152.1,0)
mars.goto(249.1,0)
jupiter.goto(815.7,0)
saturn.goto(1507,0)

mercury.down()
venus.down()
earth.down()
mars.down()
jupiter.down()
saturn.down()

for time in range(360000):
    mercury.goto(57.8*math.cos(math.radians(-250*time/97.97))+11.9,math.sqrt(57.8**2-11.9**2)*math.sin(-math.radians(250*time/97.97)))
    venus.goto(108.2*math.cos(math.radians(-250*time/224.7))+0.8,math.sqrt(108.2**2-0.8**2)*math.sin(-math.radians(250*time/224.7)))
    earth.goto(149.6*math.cos(math.radians(-250*time/365.26))+2.5,math.sqrt(149.6**2-2.5**2)*math.sin(-math.radians(250*time/365.26)))
    mars.goto(227.9*math.cos(math.radians(-250*time/686.98))+21.2,math.sqrt(227.9**2-21.2**2)*math.sin(-math.radians(250*time/686.98)))
    jupiter.goto(778.3*math.cos(math.radians(-250*time/4332.71))+74.8,math.sqrt(778.3**2-74.8**2)*math.sin(-math.radians(250*time/4332.71)))
    saturn.goto(1427*math.cos(math.radians(-250*time/10759.5))+80.2,math.sqrt(1427**2-80**2)*math.sin(-math.radians(250*time/10759.5)))
