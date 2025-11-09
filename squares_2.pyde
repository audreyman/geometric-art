size (600, 600)
background (214, 203, 203)
noFill()

# Color palette using color(r,g,b)
colors = [
          color(150, 75, 0), # brown
          color(255, 0, 0), # red
          color(255, 128, 0), # orange
          color(255,128,0), # yellow
          color(0, 128, 0), # green
          color(0, 0, 255), # blue
          color (0, 0, 0), # black
]

# Nested squares centered
strokeWeight(12)
for i in range(13):
    stroke(colors[i % len(colors)])
    s = 50 + i * 40
    rectMode(CENTER)
    rect(width/2, height/2, s, s) 
        
# Add filled square in the middle to fill the gap
strokeWeight(1)
fill(0, 0, 0)
stroke(0,0,0)
rect(width/2, height/2, 25, 25)
