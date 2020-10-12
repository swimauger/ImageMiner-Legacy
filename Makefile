# Install Dependencies
install:
	pip3 install --target=./lib/module/ pywebview pillow xlsxwriter pyinstaller

# Uninstall Dependencies
uninstall:
	rm -rf lib/module

# Run App in Development
run:
	python3 main.py
