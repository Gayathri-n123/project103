import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="E:\White hat jr\python\python  (projects)\c102\document_files\document_files"
to_dir="E:\White hat jr\python\python  (projects)\c102\c102"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey,{event.src_path}has been created!")

    
    def on_modified(self,event):
        print(f"Hey! Someone modified {event.src_path}")

    def on_moved(self,event):
        print(f"Hey,{event.src_path}has been moved!")
        
    def on_deleted(self,event):
        print(f"Oops! Someone deleted {event.src_path}")

event_handler = FileEventHandler() 
 # Initialize Observer
observer = Observer() 
  # Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)
    # Start the Observer 
observer.start()

try: 
    while True: 
        time.sleep(2) 
        print("running...") 
except KeyboardInterrupt:
     print ("stopped!")
     observer.stop()