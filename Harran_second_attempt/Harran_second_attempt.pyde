# set up canvas
size(650,400)
background(200,200,200)
noStroke()

# RGB color palette
colors = [
          color(216,15,39), # red
          color(232, 119,33),   # orange
          color(234, 220, 85),   # yellow
          color(99,142,76),     # green
          color(49,124,142),     # blue
          color(152,147,148),    # grey
          color(238, 130, 238)  # violet
          ]

# top left semi circle
x = 210
y = 200
diam = 380  # diameter should be around double

# simple loop to create a rainbow of arcs
for i in range (len(colors)):
    fill(colors[i])
    arc(x, y, diam - i * 40, diam - i * 40, PI, TWO_PI, PIE)
    
# create a border with 3 straight sides and a curved edge
stroke(222, 157, 221)
strokeWeight(20)
noFill()
line(200, 0, 200, 200) # right edge
line(0, 200, 200, 200) # bottom edge
arc(215, 200, 400, 400, PI, PI+HALF_PI);

# top middle section - overlapping arcs
noStroke()
for i in range(len(colors)):
    fill(colors[i])
    arc(410, 200, diam - i * 45, diam - i * 45, PI, TWO_PI, PIE)
 
# top middle arcs filling the box
noStroke()
for i in range(len(colors)):
    fill(colors[i])
    # this draws arcs from top-left to bottom-right quadrant
    arc(410, 200, diam - i*45, diam - i*45, -PI/2, 0, PIE)

# middle square border
noFill()
stroke(224, 143, 81)
strokeWeight(20)
rect(220, 0, 200, 200)

# quarter circle again on right side
noStroke()
for i in range(len(colors)):
    fill(colors[i])
    # mirror horizontally: center is on the right side, same diameter logic
    arc(440, 200, diam - i * 45, diam - i * 45, PI + HALF_PI, TWO_PI, PIE)

# pink border on top right section
stroke(237, 148, 208)
strokeWeight(20)
noFill()
line(435, 0, 435, 200)
line(435, 200, 800, 200)
# use diameters slightly larger than biggest arc
arc(440, 180, 390, 350, -HALF_PI, 0)

# new colors for bottom part
colors = [
          color(193,35,72), # red
          color(255, 165, 0),   # orange
          color(230, 232, 160),   # yellow
          color(25, 145, 10),     # green
          color(162, 192, 255),  # baby blue
          color(75, 0, 130),    # indigo
          color(238, 130, 238)  # violet
          ]

# big arc for the bottom
noStroke()
for i in range(len(colors)):
    fill(colors[i])
    arc(210, 210, diam - i * 40, diam - i * 40, 0, PI, PIE)
    
    
# another rainbow to overlap with the left one
for i in range(len(colors)):
    fill(colors[i])
    arc(425, 210, diam - i * 41, diam - i * 41, 0, PI, PIE)
    
    
# bottom left arcs
for i in range(len(colors)):
    fill(colors[i])
    arc(210, 210, diam - i * 40, diam - i * 40, 0, PI, PIE)

# bottom right arcs
for i in range(len(colors)):
    fill(colors[i])
    arc(425, 210, diam - i * 41, diam - i * 41, 0, PI, PIE)

# straight borders for bottom part
stroke(224, 143, 81)
strokeWeight(20)
noFill()
line(0, 210, 210, 210)    # bottom left horizontal
line(210, 210, 210, 400)  # bottom left vertical
line(425, 210, 650, 210)  # bottom right horizontal
line(425, 210, 425, 400)  # bottom right vertical

# add arched borders (bottom)
stroke(224, 143, 81)
strokeWeight(20)
noFill()
arc(200, 210, diam + 1, diam + 1, HALF_PI, PI, OPEN) # left
arc(435, 212, diam + 1, diam + 1, 0, HALF_PI, OPEN) # right

stroke(237, 148, 208)
rect(225, 210, 190, 190)

# in hindsight i couldve just made two full circles but i was just changing how it looked as i went along
