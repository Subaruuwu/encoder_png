from src.png_algorithm import save_as_png
from src.io_operations import load_image_from_disk, capture_image_from_camera

if __name__ == "__main__":
    # image = capture_image_from_camera()
    image = load_image_from_disk('img/four_k.png')
    save_as_png(image, 'new_img/output.png', 0, 3)
