from src.chunk_handling import create_png_signature, create_ihdr_chunk, create_idat_chunk, create_iend_chunk
from src.filters import apply_filter
from src.io_operations import save_file


def save_as_png(image, filename, filter_type, compression_level):
    height, width, _ = image.shape
    png_data = create_png_signature()
    png_data += create_ihdr_chunk(width, height)
    scanlines = apply_filter(image, filter_type)
    png_data += create_idat_chunk(scanlines, compression_level)
    png_data += create_iend_chunk()
    save_file(filename, png_data)
