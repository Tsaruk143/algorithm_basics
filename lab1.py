from PIL import Image

def read_dataset(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            y, x = map(int, line.strip().split())
            data.append((x, y))
    return data

image_width = 960
image_height = 540

dataset_file = 'DS9.txt'
data = read_dataset(dataset_file)

image = Image.new('L', (image_width, image_height), 255)
pixels = image.load()

for x, y in data:
    pixels[x, image_height - y - 1] = 0

output_file = 'DS9_image.png'
image.save(output_file)
print(f"Зображення збережено у файлі: {output_file}")
