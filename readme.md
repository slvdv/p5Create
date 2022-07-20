# Usage
`ptyhon3 p5Create [target_directory]`

## Example
`python3 p5Create .` -> creates a p5 project in the working directory

## Add alias (linux)
- Move p5Create script somewhere permanent. Personally, I keep my utility scripts inside a folder called ~/scripts
`mv p5Create.py ~/scripts`

`sudo nano ~/.bashrc`

and add a line `alias p5Create='python3 ~/scripts/p5Create.py .`
