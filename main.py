import colorgram

rgb_colours  = []
colours = colorgram.extract('image.jpg',80)

for colour in colours:
    rgb_colours.append(colour.rgb)

print(rgb_colours)