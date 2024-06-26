from data.patch import FilePatch


dict_of_filters = {
    0: 'None',
    1: 'Sub',
    2: 'Up',
    3: 'Average',
    4: 'Paeth',
    5: 'Auto-best'
}

inverted_dict_of_filters = {
    'None': 0,
    'Sub': 1,
    'Up': 2,
    'Average': 3,
    'Paeth': 4,
    'Auto-best': 5
}

levels_of_compression = {i: str(i) for i in range(10)}

file_patch = FilePatch()
