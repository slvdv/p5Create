import sys
import argparse
import pathlib
import shutil

#### TEMPLATES ####
indexTpl = """<!DOCTYPE html>
<html lang="en">
  <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.1/p5.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.1/addons/p5.sound.min.js"></script>
    <link rel="stylesheet" type="text/css" href="style.css">
    <meta charset="utf-8" />

  </head>
  <body>
    <main>
    </main>
    <script src="sketch.js"></script>
  </body>
</html>"""

sketchTpl = """function setup()
{
	createCanvas(window.innerWidth, window.innerHeight);
	background(35);
}"""

styleTpl = """html, body {
  margin: 0;
  padding: 0;
}
canvas {
  display: block;
}

function draw()
{

}"""

#### END TEMPLATES ####

def main():
    parser = argparse.ArgumentParser(description='Creates a new p5 project in specified directory.')
    parser.add_argument('target', type=pathlib.Path,
                    help='target destination', default='.')

    args = parser.parse_args()
    target = args.target
    
    if (target is null):
        target = '.'

    
    indexFile = open(f"{target}/index.html", "x")
    indexFile.write(indexTpl)

    sketchFile = open(f"{target}/sketch.js", "x")
    sketchFile.write(sketchTpl)
    
    styleFile = open(f"{target}/style.css", "x")
    styleFile.write(styleTpl)


main()
