from .module.PIL import Image, ExifTags
from .module.xlsxwriter import Workbook
import sys

def extract_exif(source):
    image = Image.open(source)
    exifdata = image.getexif()

    exportable_exif = { "ImageId": source }

    for tag_id in exifdata:
        try:
            tag = ExifTags.TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            if isinstance(data, bytes):
                data = data.decode()
            exportable_exif[tag] = data
        except:
            continue
    return exportable_exif

def get_headers(exif_images):
    headers = {}
    for exportable_exif in exif_images:
        for header in exportable_exif:
            if header not in headers:
                headers[header] = True
    
    return list(headers.keys())

def export_exif(exif_images):
    wb = Workbook('/Users/mark/Desktop/python-imagemine.xlsx')
    ws = wb.add_worksheet()

    headers = get_headers(exif_images)
    for col in range(len(headers)):
        ws.write(0, col, headers[col])

    row = 1
    for exportable_exif in exif_images:
        for col in range(len(headers)):
            if headers[col] in exportable_exif:
                ws.write(row, col, exportable_exif[headers[col]])
            else:
                ws.write(row, col, "")
        row += 1
    
    wb.close()
