from PIL import Image

# Add commands to import modules here.



# Define your load_img() function here.

# Parameters: The name of the file to be opened (string)

# Returns: The image object with the opened file.
def load_img(nameofimage):
    i = Image.open(nameofimage)
    return i

#load_img("flowers.jpg")
# Define your show_img() function here.

# Parameters: The image object to display.

# Returns: nothing.

def show_img(myImg):
    myImg.show()

# Define your save_img() function here.

#       Parameters: The image object to save, the name to save the file as (string)

#       Returns: nothing.

def save_img(im, fileName):
    im.save(fileName)
# Define your obamicon() function here.

#       Parameters: The image object to apply the filter to.

#       Returns: A New Image object with the filter applied.

def obamicon(flowerimage):
    flowerimage.getdata(band = None)
    og = list(image.getdata())
    darkBlue = (0,51,76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)
    newimg = []
    for x in og:
        intensity = x[0] + x[1] + x[2]

        if intensity < 182:
            newimg.append(darkBlue)
        elif intensity < 364:
            newimg.append(red)

        elif intensity < 546:
            newimg.append(lightBlue)

        elif intensity >= 546:
            newimg.append(yellow)

    newflower = Image.new("RGB" ,(250,250))
    newflower = flowerimage.putdata(newimg)
    return newflower


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
    newflower = image.putdata(invlist)
    return newflower


def halfilter(flowerimage):
    flowerimage.getdata(band=None)

    d = list(image.getdata())
    halflengthlist= []
    halflength = int((len(d))/2)

    for colors in range(halflength):
        x1= 255- colors[0]
        x2= 255- colors[1]
        x3= 255- colors[2]
        halflengthlist.append((x1, x2, x3))

    halfflower = flowerimage.putdata(halflengthlist)
    half2 = Image.new("RGB" ,(250,250))
    half2 = image.putdata(halflengthlist)
    return newflower




load_img("flowers.jpg")
image = load_img("flowers.jpg")
show_img(image)
#save_img(image, "flowers2.jpg")
#obamicon(image)
#show_img(image)
#aadyainvfilter(image)
#show_img(image)
halfilter(image)
show_img(image)
