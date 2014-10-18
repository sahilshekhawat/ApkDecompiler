#Author: Sahil Shekhawat 
#https://github.com/sahilshekhawat

#imports
import sys
import os
import gtk
from shutil import copyfile

details = "            APK DECOMPILER\n\n   Author: SAHIL SHEKHAWAT\n sahilshekhawat01@gmail.com"

def main():
    try:
        file = str(sys.argv[1])[:-4] + "/"
    except:
        file = ""
        print("Usage: \n'python apkdecompiler.py <apk_path>'\n")

    if(file != ""):
        dir = os.path.dirname(file)
        os.mkdir(dir)
        #copyfile(file, dir)
    
class ApkDecompilerApp(gtk.Window):
    def __init__(self):
        super(ApkDecompilerApp, self).__init__()

        self.file = ""
        self.set_title("Apk Decompiler")        
        self.connect("destroy", gtk.main_quit)
        self.set_size_request(690,350)
        self.set_position(gtk.WIN_POS_CENTER)
        self.progressbar = gtk.ProgressBar(adjustment=None)
        hbox = gtk.Fixed()

        try:
            self.icon_image = gtk.gdk.pixbuf_new_from_file("apkdecompiler_icon.png")
        except Exception, e:
            print e.message
            sys.exit(1)

        iconImage = gtk.Image()
        iconImage.set_from_pixbuf(self.icon_image)
        hbox.put(iconImage, 10, 10)
        #Setting up the apkdecompiler ico
        try:
            self.set_icon_from_file("apkdecompiler_icon.png")
        except Exception, e:
            print e.message
            sys.exit(1)
        
        label = gtk.Label(details)
        hbox.put(label, 400, 80)

        self. progressbar.set_text("Select Apk First")
        self.progressbar.set_size_request(350, 30)
        hbox.put(self.progressbar, 320, 270)

        next = gtk.Button("Decompile Apk")
        next.connect("clicked", self.decompile)
        cancel = gtk.Button(stock=gtk.STOCK_CANCEL)
        cancel.connect("clicked", self.cancel)
        fileChooser = gtk.Button("Select apk")
        fileChooser.connect("clicked", self.display_file_chooser)
        hbox.put(fileChooser, 10,315)
        hbox.put(cancel, 500, 315)
        hbox.put(next, 565, 315)
        self.add(hbox)
        self.show_all()

    def display_file_chooser(self, fileChooser):
        #creating apk chossing dialog
        dialog = gtk.FileChooserDialog("Open..", None,
                                        gtk.FILE_CHOOSER_ACTION_OPEN,
                                        (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                         gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        filter = gtk.FileFilter()
        filter.set_name(".apk")
        filter.add_pattern("*.apk")
        dialog.add_filter(filter)

        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            self.file = dialog.get_filename()
        elif response == gtk.RESPONSE_CANCEL:
            print 'closed, no files selected'
        dialog.destroy()

    def decompile(self, button):
        self.progressbar.set_text("decompiling apk ")
        

    def cancel(self, button):
        gtk.main_quit(self, button)

ApkDecompilerApp()
gtk.main()
