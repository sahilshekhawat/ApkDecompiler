import gtk
import os
import ntpath
import threading
import zipfile
from shutil import copyfile

class processing(threading.Thread):
    def __init__(self, progressbar , file):
        super(processing, self).__init__()
        self.progressbar = progressbar
        self.progressbar.set_fraction(0.05)
        self.file = file

    def run(self):
        parent_dir =  os.path.abspath(os.path.join(__file__, os.pardir))
        app_name =  self.path_leaf(os.path.splitext(self.file)[0])
        dir = parent_dir + os.sep + app_name
        os.mkdir(dir)
        new_apk_dir = dir + os.sep + self.path_leaf(self.file)
        
        #copy apk to folder <apk_name> in the parent directory of this app.
        copyfile(self.file, new_apk_dir)
        
        #copy after changing .apk extension to .zip
        new_apk_zip = dir + os.sep + app_name + ".zip"
        copyfile(new_apk_dir, new_apk_zip)
        
        #extracting zipfile
        output_path = dir + os.sep + app_name
        with zipfile.ZipFile(new_apk_zip, 'r') as z:
            z.extractall(output_path)
        
        #moving classes.dex file to dex2jar folder
        copyfile(output_path + os.sep +  "classes.dex", parent_dir + os.sep + dexjar + os.sep + dex2jar-0.0.9.15 + "classes.dex")
        
        #running dexjar command
        
        
        
    def path_leaf(self,path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
        
