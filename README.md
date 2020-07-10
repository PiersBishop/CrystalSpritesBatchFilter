# Crystal Sprites Batch Filter
This script is intended as an extra tool when making custom hacks of Pokemon Crystal Version when using ![pret/pokecrystal](https://github.com/pret/pokecrystal) as source code.

Long story short, the makefile requires the sprites to be in png format and using no more than 4 indexed colors. 

A lot of image editing software may allow these specific settings when saving or exporting the image, but it is not something that is easy for eveyone. Even if it were, doing so manually for all of the game's sprites is long and tedious. This script is presented here as a solution to this issue, by batch-filtering all of the images in the gfx/pokemon folders.

### How to use
For the time being, it is just a python script with a hard-coded path written into it. It has to be lauched from Pycharm or however you usually execute your python lines of code.

I do realise the irony of wanting to make an a tool accessible to people who don't have knowledge of image encoding, and only making is accessible to people who know how to launch a python script. The current state of the script suits my needs, but I'll probably make a custom executable in the future, something that you'd just have to move to the gfx/pokemon folder and launch from there.

If anybody reading this wants to make this tool themselves, feel free to do so. I wouldn't be sharing on github otherwise.

### How it works (and what issues it may have)
The algorithm scans the whole gfx/pokemon directory, and in each of the folders, does the following operation on both front.png and back.png :

1/ Checks if the file exists. Unown has different folders for its forms, so the unown folder will be ignored.

2/ Converts the image to using indexed colors, and counts the indexes on the palette. If the image uses 4 colors or less, it saves it as it is, in indexed colors mode.

3/ If the image has more than 4 colors, a first pass is done to eliminate any colors that are too close to white or black. It then checks if the image now has 4 colors and can be saved, or if the next step is necessary. In my personal experience, most of the issues were with pixels that were randomly written as "almost white" or "almost black", but your mileage may vary.

4/ The script will list the 4 most used colors in the image, and any pixel of a different color than one of these 4 will be rounded to which ever of these 4 colors is the closest to it. At this point, the image will have only 4 colors, and is saved.

Do note that color comparision is only done by comparing the totals of the RGB values added to each other. Meaning a pure green pixel will be estimated as equal to a pure red pixel, even if it "should" be rounded to an indexed "slightly green" color instead. My reasoning is that this script is to be considered a "final cleanup" for removing any noise or impurities, and not as a filter for any image whatsoever.

It should also be noted that listing colors by the most used ones in priority can cause issues with sprites that use a color in their palette only for a small detail, such as bulbasaur's red pixels only being used for its eye and mouth. As I said, this script is intended for images that only suffer from slight noise or weird unused palette values.

__Disclaimer__ : this script will screw up a bit on occasion. In my tests, a few sprites, including some of the original sprites that already don't have any issues, were saved with the right amount of colors in the image, but not in the palette. these had to be reopenned in paint in order to write white pixels where there already was a white background, and re-save the image. In any case, I would recomend using it in the gfx/pokemon folder only if you plan on using custom sprites exclusively. In other cases, I'd recommend having a custom folder that uses the same heirarchy as the original gfx/pokemon folder, with individuals folders for each pokemon, containging a font.png and a back.png.

__Disclaimer 2__ : As it turns out, the resulting images look fine, and the game compiles fine, but it turns out for some reason they're imported with palette issues. I shared this here before fully testing it. Oops. If you have any suggetsions, feel free to join in, my Python is really rusty and I'm unfamiliar with PIL / Pillow.
