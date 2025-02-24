import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4",".mkv"],
    "Music": [".mp3"]
}

DOWNLOADS_FOLDER = r"C:\Users\YourUsername\Downloads"

def organize_files():
    if not os.path.exists(DOWNLOADS_FOLDER):
        print("Directory does not exist!")
        return

    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)


        if os.path.isdir(file_path):
            continue


        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()


        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_path = os.path.join(DOWNLOADS_FOLDER, category)


                if not os.path.exists(category_path):
                    os.makedirs(category_path)


                shutil.move(file_path, os.path.join(category_path, filename))
                print(f"Moved: {filename} → {category}/")
                break

if __name__ == "__main__":
    organize_files()
