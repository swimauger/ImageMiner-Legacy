from lib.module import webview
from lib.api import API
from lib.exif import extract_exif

def init():
    api = API()
    window = webview.create_window('Image Miner', 'src/index.html', js_api=api)

    def open_explorer(message):
        file_types = (['Image Files (*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.svg)'])
        images = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        for image in images:
            extract_exif(image)

    api.on('open_explorer', open_explorer)

    webview.start()

init()
