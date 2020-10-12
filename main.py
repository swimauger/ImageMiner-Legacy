from lib.module import webview

if __name__ == '__main__':
    window = webview.create_window('Image Miner', 'src/index.html')
    webview.start()
