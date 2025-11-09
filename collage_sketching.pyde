size(500, 600)
background(45)

# pastel colors
colors = [
    color(255, 179, 186),  # soft pink
    color(255, 223, 186),  # peach
    color(255, 255, 186),  # light yellow
    color(186, 255, 201),  # mint green
    color(186, 225, 255)   # baby blue
]

# draw overlapping shapes

stroke(15,90,10) # dark green
strokeWeight(1.5)

fill(colors[0], 180) 
ellipse(250, 300, 400, 400) # big circle

fill(colors[1], 180)
rect(150, 150, 350, 200)

fill(colors[2], 180)
triangle(200, 100, 200, 400, 50, 400)

stroke(100,50,165) # purple
fill(colors[3], 180)
arc(150, 200, 250, 250, PI, TWO_PI) # semi circle

fill(colors[4], 180)
ellipse(110, 450, 200, 200)


# add a few smaller ones and lines 
fill(colors[0], 150)
rect(100, 400, 150, 100)

fill(colors[2], 150)
arc(380, 200, 200, 200, 0, PI + QUARTER_PI)

fill(colors[3], 150)
triangle(200, 100, 300, 50, 350, 150)

# accent diagonal lines 
strokeWeight(3)

stroke(150, 80, 200)
line(50, 100, 200, 50)

stroke(60, 100, 220)
line(300, 450, 400, 550)

stroke(90, 200, 170)
line(100, 300, 250, 400)

stroke(220, 100, 180)
line(260, 200, 320, 220)

stroke(15,90,10)
strokeWeight(1.5)
fill(colors[2], 180)
ellipse(65, 200, 55, 55)


# done!
