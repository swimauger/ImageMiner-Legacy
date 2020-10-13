from lib.module import webview
from lib.api import API
from lib.exif import extract_exif, export_exif

def init():
    api = API()
    window = webview.create_window('Image Miner', 'app/index.html', js_api=api)

    def open_explorer(message):
        file_types = (['Image Files (*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.svg)'])
        images = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        return images
        
    def export(images):
        exif_images = []
        for image in images:
            exif_images.append(extract_exif(image))
        export_exif(exif_images)

    api.on('open_explorer', open_explorer)
    api.on('export', export)

    webview.start()

init()
