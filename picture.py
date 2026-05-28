from rembg import remove
from PIL import Image

input_path = "python.png"
output_path = "python_nobg.png"

inp = Image.open(input_path)
out = remove(inp)
out.save(output_path)