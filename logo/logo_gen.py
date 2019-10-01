"""
Generate GuiTeNet logo.
"""

def main():

    width  = 500
    height = 500

    offset = [250,250]

    inner_coords = [
        [  40,  -50],
        [  80,   10],
        [  30,   60],
        [ -60,   40],
        [ -50,  -40]]
    middle_coords = [
        [  90, -100],
        [ 150,   20],
        [  70,  110],
        [-130,   70],
        [-100,  -80]]
    outer_coords = [
        [ 140, -170],
        [ 240,   20],
        [ 130,  180],
        [-210,  120],
        [-190, -150]]

    with open('logo.svg', 'w') as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(width, height))
        f.write('\n')

        f.write('\t<defs>\n')
        f.write('\t\t<style>\n')
        f.write('\t\t\tsvg { font-family: Arial, Helvetica, sans-serif; }\n')
        f.write('\t\t\t.tensorSymbol { fill: black; }\n')
        f.write('\t\t\t.tensorCaption { fill: white; text-anchor: middle; font-weight: bold; }\n')
        f.write('\t\t\t.tensorLegLine { fill: rgb(255, 171, 0); stroke: rgb(255, 171, 0); stroke-width: 3; stroke-linejoin: round; stroke-linecap: round; }\n')
        f.write('\t\t\t.tensorLegTip { fill: rgb(0, 255, 0); stroke: rgb(255, 171, 0); stroke-width: 3; stroke-linejoin: round; stroke-linecap: round; }\n')
        f.write('\t\t</style>\n')
        f.write('\t</defs>\n')
        f.write('\n')

        f.write('\t<g id="tensorLegs">\n')

        f.write('\t\t<!-- middle ring -->\n')
        for i in range(len(middle_coords)):
            f.write('\t\t<g class="tensorLeg">\n')
            x1 = offset[0] + middle_coords[i-1][0]
            y1 = offset[1] + middle_coords[i-1][1]
            x2 = offset[0] + middle_coords[i][0]
            y2 = offset[1] + middle_coords[i][1]
            f.write('\t\t\t<line class="tensorLegLine" x1="{}" y1="{}" x2="{}" y2="{}"/>\n'.format(x1, y1, x2, y2))
            f.write('\t\t</g>\n')
        f.write('\n')

        f.write('\t\t<!-- inner ring -->\n')
        for i in range(len(inner_coords)):
            f.write('\t\t<g class="tensorLeg">\n')
            x1 = offset[0] + inner_coords[i-1][0]
            y1 = offset[1] + inner_coords[i-1][1]
            x2 = offset[0] + inner_coords[i][0]
            y2 = offset[1] + inner_coords[i][1]
            f.write('\t\t\t<line class="tensorLegLine" x1="{}" y1="{}" x2="{}" y2="{}"/>\n'.format(x1, y1, x2, y2))
            f.write('\t\t</g>\n')
        f.write('\n')

        f.write('\t\t<!-- outer rays -->\n')
        for i in range(len(inner_coords)):
            f.write('\t\t<g class="tensorLeg">\n')
            x1 = offset[0] + middle_coords[i][0]
            y1 = offset[1] + middle_coords[i][1]
            x2 = offset[0] +  outer_coords[i][0]
            y2 = offset[1] +  outer_coords[i][1]
            f.write('\t\t\t<line class="tensorLegLine" x1="{}" y1="{}" x2="{}" y2="{}"/>\n'.format(x1, y1, x2, y2))
            f.write('\t\t</g>\n')
        f.write('\n')

        f.write('\t\t<!-- middle rays -->\n')
        for i in range(len(inner_coords)):
            f.write('\t\t<g class="tensorLeg">\n')
            x1 = offset[0] +  inner_coords[i][0]
            y1 = offset[1] +  inner_coords[i][1]
            x2 = offset[0] + middle_coords[i][0]
            y2 = offset[1] + middle_coords[i][1]
            f.write('\t\t\t<line class="tensorLegLine" x1="{}" y1="{}" x2="{}" y2="{}"/>\n'.format(x1, y1, x2, y2))
            f.write('\t\t\t<circle class="tensorLegTip" cx="{}" cy="{}" r="6"/>\n'.format(x2, y2))
            f.write('\t\t</g>\n')
        f.write('\n')

        f.write('\t\t<!-- inner rays -->\n')
        for c in inner_coords:
            f.write('\t\t<g class="tensorLeg">\n')
            x = offset[0] + c[0]
            y = offset[1] + c[1]
            f.write('\t\t\t<line class="tensorLegLine" x1="{}" y1="{}" x2="{}" y2="{}"/>\n'.format(offset[0], offset[1], x, y))
            f.write('\t\t\t<circle class="tensorLegTip" cx="{}" cy="{}" r="6"/>\n'.format(x, y))
            f.write('\t\t</g>\n')

        f.write('\t</g>\n')
        f.write('\n')

        f.write('\t<g id="tensors">\n')
        f.write('\t\t<g class="tensor" x="{0}" y="{1}" transform="translate({0},{1})">\n'.format(offset[0], offset[1]))
        f.write('\t\t\t<circle class="tensorSymbol" cx="0" cy="0" r="20"/>\n')
        f.write('\t\t\t<text class="tensorCaption" dy="5">T</text>\n')
        f.write('\t\t</g>\n')
        f.write('\t</g>\n')

        f.write('</svg>\n')


if __name__ == '__main__':
    main()
