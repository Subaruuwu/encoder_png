def get_new_patch(patch, new_patch):
    return new_patch + '/' + patch.split('/')[-1].split('.')[0] + 'converted.png'
