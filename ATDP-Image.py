import image

img = image.Image("ape.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()
height = img.getHeight()
width = img.getWidth()
blocks = 8
for block1 in range(blocks):
  for block2 in range(blocks):
    for col in range(int(width * block1 / blocks), int(width * (block1 + 1) / blocks)):
      for row in range(int(height * block2 / blocks), int(height * (block2 + 1) / blocks)):
        p = img.getPixel(col, row)
        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
          
        if (block1 + block2) % 2 == 1:
          red = 0
        
        if (block1 * block2) % 2 == 1:
          green = 0
          
        if (block1 - block2) % 2 == 1:
          blue = 0

        newpixel = image.Pixel(red, green, blue)
        newimg.setPixel(col, row, newpixel)
    newimg.draw(win)
    win.exitonclick()
