import sys
import json
from PIL import Image

print("Preparing...")

layoutPath = "tileset_layout.json"
template = []
tiles = []

# check if path to template has been given as an arguement, otherwise try the default path 
if len(sys.argv) >= 2:
    inputTemplate = sys.argv[1]
else:
    inputTemplate = "template.png"


def slice(img):

    sliceSize = img.size[1] / 4
    sliceID = 0

    for i in range(4):
        for j in range(6):
            left = j * sliceSize
            upper = i * sliceSize
            right = (j + 1) * sliceSize
            lower = (i + 1) * sliceSize

            sliceImg = img.crop((left, upper, right, lower))
            template.append(sliceImg)

            sliceID += 1

def sliceOutput(img):

    sliceSize = templateImg.size[1] / 2
    sliceID = 0

    for i in range(6):
        for j in range(8):
            left = j * sliceSize
            upper = i * sliceSize
            right = (j + 1) * sliceSize
            lower = (i + 1) * sliceSize

            sliceImg = img.crop((left, upper, right, lower))
            tiles.append(sliceImg)

            sliceID += 1

def buildTiles():

    print("Constructing tiles...")

    tileID = 0
    layout = json.loads(open(layoutPath).read())

    for tile in tiles:

        try:
            layoutTile = layout["tileset"][str(tileID)]
        except:
            continue
            
        templatePiece = None
        pieceSize = templateImg.size[1] // 4

        # NW
        d = 0
        p = (0, 0)

        if layoutTile[d] == "base":                             # switch statement when? :>
            templatePiece = layout["template"]["base"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "edgeNS":
            templatePiece = layout["template"]["edgeNS"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "edgeWE":
            templatePiece = layout["template"]["edgeWE"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "corner":
            templatePiece = layout["template"]["corner"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "innerCorner":
            templatePiece = layout["template"]["innerCorner"][d]
            tile.paste(template[templatePiece], p)

        # NE
        d = 1
        p = (pieceSize, 0)

        if layoutTile[d] == "base":
            templatePiece = layout["template"]["base"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "edgeNS":
            templatePiece = layout["template"]["edgeNS"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "edgeWE":
            templatePiece = layout["template"]["edgeWE"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "corner":
            templatePiece = layout["template"]["corner"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "innerCorner":
            templatePiece = layout["template"]["innerCorner"][d]
            tile.paste(template[templatePiece], p)
    
        # SW
        d = 2
        p = (0, pieceSize)

        if layoutTile[d] == "base":
            templatePiece = layout["template"]["base"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "edgeNS":
            templatePiece = layout["template"]["edgeNS"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "edgeWE":
            templatePiece = layout["template"]["edgeWE"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "corner":
            templatePiece = layout["template"]["corner"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "innerCorner":
            templatePiece = layout["template"]["innerCorner"][d]
            tile.paste(template[templatePiece], p)

        # SE
        d = 3
        p = (pieceSize, pieceSize)

        if layoutTile[d] == "base":
            templatePiece = layout["template"]["base"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "edgeNS":
            templatePiece = layout["template"]["edgeNS"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "edgeWE":
            templatePiece = layout["template"]["edgeWE"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "corner":
            templatePiece = layout["template"]["corner"][d]
            tile.paste(template[templatePiece], p)
        elif layoutTile[d] == "innerCorner":
            templatePiece = layout["template"]["innerCorner"][d]
            tile.paste(template[templatePiece], p)

        tileID += 1

def outputFile():
    
    tileSize = output.size[0] // 8
        
    for i, tile in enumerate(tiles):
        x = (i % 8) * tileSize
        y = (i // 8) * tileSize
        output.paste(tile, (x, y))

    # check if a name has been given as an arguement, otherwise use the default name
    if len(sys.argv) >= 3:
        name = sys.argv[2] + '.png'
        output.save(f'{name}')
    else:
        output.save(f'tileset.png')

# make sure the template exists
try:
    templateImg = Image.open(inputTemplate)
except:
    print("Could not open template image :(")
    sys.exit()

# cut the template into its individual pieces
slice(templateImg)

# make a new image and cut it into tiles for later the final tileset
output = Image.new("RGBA", (templateImg.size[1] * 4, templateImg.size[1] * 3))
sliceOutput(output)

# use the tileset layout to construct each tile using the pieces from the provided template
buildTiles()

# stitch the finished tiles into the output file and save it
outputFile()

print("Finished!")