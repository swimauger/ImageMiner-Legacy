from .module.PIL import Image, ExifTags

def extract_exif(source):
    image = Image.open(source)
    exifdata = image.getexif()

    print(source)
    for tag_id in exifdata:
        tag = ExifTags.TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")

def export_exif(exif):
    return {}