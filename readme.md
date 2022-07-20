# Usage
`python3 p5create [target_directory]`

## Example
`python3 p5create .` -> creates a p5 project in the working directory

## Add alias (linux)
- Move p5Create script somewhere permanent. Personally, I keep my utility scripts inside a folder called ~/data/utilities
`mv p5Create.py ~/data/utilities`

`sudo nano ~/.bashrc` and add a line `alias p5c='python3 ~/data/utilities/p5create.py`
