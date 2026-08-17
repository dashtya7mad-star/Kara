import os
import requests

# بەستەری ئەو فایلەی دەتوێت دایبەزێنیت
URL = "https://example.com/file-to-download.zip"
SAVE_PATH = "downloaded_file.zip"


def download_file():
    print("دەستپێکردنی دابەزاندن...")
    response = requests.get(URL, stream=True)
    if response.status_code == 200:
        with open(SAVE_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("فایلەکە بەسەرکەوتوویی دابەزی!")
    else:
        print(f"هەڵە ڕوویدا! کۆد: {response.status_code}")


if __name__ == "__main__":
    download_file()
