def filter_scanline(scanline, prev_scanline, filter_type):
    if filter_type == 0:  # None
        return scanline
    elif filter_type == 1:  # Sub
        return bytearray((scanline[i] - (scanline[i - 3] if i >= 3 else 0)) & 0xFF for i in range(len(scanline)))
    elif filter_type == 2:  # Up
        return bytearray((scanline[i] - (prev_scanline[i] if prev_scanline else 0)) & 0xFF for i in range(len(scanline)))
    elif filter_type == 3:  # Average
        return bytearray(
            (scanline[i] - ((scanline[i - 3] if i >= 3 else 0) + (prev_scanline[i] if prev_scanline else 0)) // 2) & 0xFF
            for i in range(len(scanline)))
    elif filter_type == 4:  # Paeth
        def paeth_predictor(a, b, c):
            p = a + b - c
            pa = abs(p - a)
            pb = abs(p - b)
            pc = abs(p - c)
            return a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)

        return bytearray(
            (scanline[i] - paeth_predictor(scanline[i - 3] if i >= 3 else 0, prev_scanline[i] if prev_scanline else 0,
                                           prev_scanline[i - 3] if (i >= 3 and prev_scanline) else 0)) & 0xFF for i in
            range(len(scanline)))


def apply_filter(image, filter_type):
    height, width, _ = image.shape
    scanlines = []
    prev_scanline = None

    for y in range(height):
        scanline = image[y, :, :3].tobytes()
        filtered_scanline = filter_scanline(scanline, prev_scanline, filter_type)
        scanlines.append(bytes([filter_type]) + filtered_scanline)
        prev_scanline = scanline

    return b''.join(scanlines)
