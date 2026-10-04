"""
Folder Watcher

Monitor folder for new images.
"""


from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



class ImageFileHandler(
    FileSystemEventHandler
):


    IMAGE_EXTENSIONS = {

        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".bmp",
        ".tiff"

    }



    def __init__(
        self,
        callback
    ):

        self.callback = callback



    def on_created(
        self,
        event
    ):

        if event.is_directory:

            return


        file_path = Path(
            event.src_path
        )


        if file_path.suffix.lower() in self.IMAGE_EXTENSIONS:

            self.callback(
                str(file_path)
            )




class FolderWatcher:


    def __init__(
        self,
        folder,
        callback
    ):

        self.folder = folder

        self.callback = callback

        self.observer = Observer()



    def start(self):

        handler = ImageFileHandler(
            self.callback
        )


        self.observer.schedule(
            handler,
            self.folder,
            recursive=False
        )


        self.observer.start()



    def stop(self):

        self.observer.stop()

        self.observer.join()