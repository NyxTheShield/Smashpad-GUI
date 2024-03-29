# Smashpad-GUI

![alt text](https://github.com/NyxTheShield/Smashpad-GUI/blob/master/Markdown%20Screenshots/Smashpad.png "Main Screenshot")

## Introduction
GUI Version of Birdwards's Smashpad script! A file padder for SSB Ultimate.
Requires the Zstandard Library, that can be installed by running the cmd:

`pip install zstandard`

## Usage

Simply run the `Smashpad-GUI.pyw` script, select the file you want to compress/decompress and select the respective option!

**This script supports the new naming convention for mods:**

`[Filename.Extension]-[Offset]-[Compressed Size]`

Example: `fighter_param_motion.prc-0x1937A9BF8-0x22FF`

If your filename follows this convention, then the script will automatically detect the desired size and will compress the file automatically. In any other case, a pop up window will appear asking to enter the desired size.

## Screenshots

![alt text](https://github.com/NyxTheShield/Smashpad-GUI/blob/master/Markdown%20Screenshots/Main.png "Main Screenshot")
![alt text](https://github.com/NyxTheShield/Smashpad-GUI/blob/master/Markdown%20Screenshots/Size.png "Size")
![alt text](https://github.com/NyxTheShield/Smashpad-GUI/blob/master/Markdown%20Screenshots/Padded.png "Padded")
