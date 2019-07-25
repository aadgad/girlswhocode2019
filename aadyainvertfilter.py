def aadyainvfilter(flowerimage):
    flowerimage.getdata(band = None)
    f = list(image.getdata())
    invlist = []
    for colors in f:
        x1= 255- colors[0]
        x2= 255- colors[1]
        x3= 255- colors[2]
        invlist.append((x1, x2, x3))

    nflower = flowerimage.putdata(invlist)

    newflower = Image.new("RGB" ,(250,250))
    newflower = flowerimage.putdata(invlist)
    return newflower
