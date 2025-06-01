# image-gif-to-ascii-art
A simple pythong program that converts image or gif to ascii art in terminal


## Run

Clone the project

```bash
git clone https://github.com/svl10/image-gif-to-ascii-art.git
```

Go to the project directory

```bash
cd image-gif-to-ascii-art
```

For Images

```bash
python ascii_art.py path_to_image.jpg
```

For Static GIF

```bash
python ascii_art.py path_to_gif.gif --gif

```
For Animated GIF

```bash
python ascii_art.py path_to_gif.gif --gif --animated

```
To Resize an image or gif

```bash
python ascii_art.py path_to_image.jpg --width 20

```
Remember to replace `path_to_image.jpg` or `path_to_gif.gif` with the actual image/gif path

Sample

```bash
python img-to-ascii.py sample\teto.jpg --width 30

```
```bash
python img-to-ascii.py sample\tetoris.gif --gif --animated --width 30

```
