from src.png_algorithm import save_as_png
from src.io_operations import load_image_from_disk, capture_image_from_camera
from app.window import make_window
from app.application import start_app

if __name__ == "__main__":
    # image = capture_image_from_camera()

    # image = load_image_from_disk('img/four_k.png') # to start cli
    # save_as_png(image, 'new_img/output.png', 0, 3) # to start cli

    start_app() # to start gui