import os


def get_file_size(file_path):
    return round(os.path.getsize(file_path) / 1024 / 1024, 2)


def calculate_compression_ratio(origin_image, new_image):
    origin_image_size = get_file_size(origin_image)
    new_image_size = get_file_size(new_image)
    return round(new_image_size / origin_image_size, 2)