import os
from PIL import Image

white_range = 30
black_range = 30

print("")
print("----------")
print("CODE START")
print("----------")
print("")

path = "Q:\\PROJECTS\\PERSONAL\\GAMES\\2020_XX_Typh\\TyphV1\\pokecrystal-master\\gfx\\pokemon"
print("Main path is " + path)

scan = os.scandir(path)
paths = [f.path for f in scan]
print(str(len(paths)) + " mons found.")
print("This value should be 278 : 251 mons + 26 unown + 1 egg. Yes, unown's main folder is separate from its 26 forms.")

print("")
print("Starting full loop.")
print("")

for p in paths:
    print("")
    print("Current path is " + p)  # "Q:\...\abra"
    splitPath = p.split('\\')
    pokName = splitPath[len(splitPath) - 1]
    print("Currently checking " + pokName + "'s folder.")

    spritesNames = ["front", "back"]

    for sn in spritesNames:
        assemble_path = p + "\\" + sn + ".png"

        if os.path.isfile(assemble_path):
            print(pokName + "'s " + sn + ".png exists.")
            img = Image.open(assemble_path)
            p_img = img.convert("P")
            pal_size = len(p_img.getcolors())
            if pal_size > 4:
                print("There are more than 4 colors in " + pokName + "'s " + sn + ".png")
                print(str(len(img.getcolors())) + " colors found.")
                # 1/ right off the bat, start rounding colors that are too close to white/black
                img = img.convert("RGBA")
                # print(img.getcolors())
                pixels = img.load()
                for i in range(img.width):
                    for j in range(img.height):
                        px = pixels[i, j]
                        px_val = px[0] + px[1] + px[2]
                        if px_val > (255 * 3 - white_range):
                            pixels[i, j] = (255, 255, 255)
                        if px_val < black_range:
                            pixels[i, j] = (0, 0, 0)

                # 2/ count colors again, if <= 4 you're done. If not...
                p_img = img.convert("P")
                pal_size = len(p_img.getcolors())
                if pal_size > 4:
                    # 3/ list all colors, sort them by most used to least used
                    list_of_colors = img.getcolors()

                    # sort by amount of uses
                    list_of_colors.sort()
                    list_of_colors.reverse()

                    # 4/ for each color after the 4th, compare it to the first 4
                    for idx1 in range(4, len(list_of_colors)):
                        col_val = list_of_colors[idx1][1]
                        col_tot_val = col_val[0] + col_val[1] + col_val[2]
                        # 5/ find the color, of the 4, that is closest to the current index color
                        closest_idx = 0
                        curr_dist = 255 * 3
                        for idx0 in range(4):
                            this_col_val = list_of_colors[idx0][1]
                            this_col_tot_val = this_col_val[0] + this_col_val[1] + this_col_val[2]
                            this_dist = abs(col_tot_val - this_col_tot_val)
                            if this_dist < curr_dist:
                                curr_dist = this_dist
                                closest_idx = idx0
                        # 6/ then check every pixel of the picture that is of this index,
                        # and change it for the closest color index
                        for i in range(img.width):
                            for j in range(img.height):
                                px = pixels[i, j]
                                if px == list_of_colors[idx1][1]:
                                    pixels[i, j] = list_of_colors[closest_idx][1]

                    list_of_colors = img.getcolors()
                    # sort by regular color order
                    list_of_colors = sorted(list_of_colors, key=lambda coco: coco[1])
                    list_of_colors.reverse()

                    print(pokName + "'s " + sn + ".png has been converted to the proper amount of colors.")
                    print("Saving " + pokName + "'s " + sn + ".png as an indexed colors png.")
                    img.save(assemble_path)

                else:
                    print(pokName + "'s " + sn + ".png has been converted to the proper amount of colors.")
                    print("Saving " + pokName + "'s " + sn + ".png as an indexed colors png.")
                    p_img.save(assemble_path)

            else:
                print(pokName + "'s " + sn + ".png has a proper amount of colors.")
                print("Saving " + pokName + "'s " + sn + ".png as an indexed colors png.")
                p_img.save(assemble_path)

        else:
            print("WARNING : " + pokName + "'s " + sn + ".png does not exist.")

print("")
print("----------")
print("CODE OVER")
print("----------")
