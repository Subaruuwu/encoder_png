from src.chunk_handling import create_png_signature, create_ihdr_chunk, create_idat_chunk, create_iend_chunk
from src.filters import apply_filter
from src.io_operations import save_file
# from app.labels import config_text
import os


def save_as_png(image, filename, filter_type, compression_level):
    if filter_type == 5:
        res = []
        height, width, _ = image.shape
        for filter_iter in range(0, 5):
        # print('start png')
            png_data = create_png_signature()
            png_data += create_ihdr_chunk(width, height)
            scanlines = apply_filter(image, filter_iter)
            png_data += create_idat_chunk(scanlines, compression_level)
            png_data += create_iend_chunk()
            curr_file = save_file(filename, png_data)
            res.append(os.path.getsize(curr_file))
            print(res)
        min_weight = min(res)
        best_filter = res.index(min_weight)

        png_data = create_png_signature()
        png_data += create_ihdr_chunk(width, height)
        scanlines = apply_filter(image, best_filter)
        png_data += create_idat_chunk(scanlines, compression_level)
        png_data += create_iend_chunk()
        save_file(filename, png_data)

    else:
        height, width, _ = image.shape
        png_data = create_png_signature()
        png_data += create_ihdr_chunk(width, height)
        scanlines = apply_filter(image, filter_type)
        png_data += create_idat_chunk(scanlines, compression_level)
        png_data += create_iend_chunk()
        save_file(filename, png_data)
        # print('png finish')
    print('Done')
    return filename

