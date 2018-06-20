# 代码来自https://segmentfault.com/q/1010000007477984?_ea=1371012
import os, sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_modified(self, event):
        if not event.is_directory:
            path = os.path.realpath(event.src_path)
            print("被修改的文件> {0}".format(path))
            ext = os.path.splitext(path)[1]
            if ext == '.txt':
                txt = open(path).read()
                print("文件内容>")
                print(txt)

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print('正在监视文件夹：%s' % os.path.realpath(path))
    print('Ctrl-C 退出程序!')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
