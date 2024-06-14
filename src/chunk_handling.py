import struct
import zlib


def create_png_signature():
    return b'\x89PNG\r\n\x1a\n'


def create_ihdr_chunk(width, height):
    chunk_type = b'IHDR'
    data = struct.pack("!2I5B", width, height, 8, 2, 0, 0, 0)
    return create_chunk(chunk_type, data)


def create_idat_chunk(image_data, compression_level):
    compressor = zlib.compressobj(compression_level)
    compressed_data = compressor.compress(image_data) + compressor.flush()
    return create_chunk(b'IDAT', compressed_data)


def create_iend_chunk():
    return create_chunk(b'IEND', b'')


def create_chunk(chunk_type, data):
    chunk_length = len(data)
    chunk = struct.pack("!I", chunk_length) + chunk_type + data
    crc = zlib.crc32(chunk_type + data) & 0xffffffff
    chunk += struct.pack("!I", crc)
    return chunk
