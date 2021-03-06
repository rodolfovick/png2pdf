#!/usr/bin/env python

# PNG2PDF - Graphic interface related class and methods.

from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf, InterpType
from wand.image import Image
from wand.exceptions import BlobError

class GuiWindow(Gtk.Window):
    """
    PNG2PDF main window class, derivates from Gtk window class.
    """
    def __init__(self):
        """
        Creates main window.
        """
        Gtk.Window.__init__(self, title='PNG2PDF')
        self.set_border_width(10)
        self.set_default_size(400, 200)

        # self.set_icon_from_file("../misc/png2pdf.svg")

        self.fileList = []

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = 'PNG2PDF'
        self.set_titlebar(hb)

        addButton = Gtk.Button()
        addButton.connect('clicked', self.addFile)
        addIcon = Gio.ThemedIcon(name='list-add')
        addImage = Gtk.Image.new_from_gicon(addIcon, Gtk.IconSize.BUTTON)
        addButton.add(addImage)
        hb.pack_start(addButton)

        saveButton = Gtk.Button()
        saveButton.connect('clicked', self.saveFile)
        saveIcon = Gio.ThemedIcon(name='document-save')
        saveImage = Gtk.Image.new_from_gicon(saveIcon, Gtk.IconSize.BUTTON)
        saveButton.add(saveImage)
        hb.pack_end(saveButton)

        self.listStore = Gtk.ListStore(Pixbuf)
        iconView = Gtk.IconView.new()
        iconView.set_model(self.listStore)
        iconView.set_pixbuf_column(0)
        self.add(iconView)
        
    def imgConvert(self, fileList=[], fileName=''):
        """
        Convert images from fileList in pdf file named fileName.
        """
        with Image() as img:
            for file in fileList:
                try:
                    img.read(filename=file)
                except BlobError as e:
                    x = e.args[0]
                    raise IOError(x)
                with img.convert('pdf') as converted:
                    try:
                        converted.save(filename=fileName)
                    except BlobError as e:
                        x = e.args[0]
                        raise IOError(x)
                    except IOError as e:
                        x = e.args[0]
                        raise IOError(x)

    def addFile(self, widget):
        """
        Add file (image) dialog.
        """
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        #self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            fileName = dialog.get_filename()
            self.fileList.append(fileName)
            pixBuf = Pixbuf.new_from_file_at_size(fileName, 120, 120)
            self.listStore.append([pixBuf])
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def saveFile(self, widget):
        """
        Save file name (PDF) dialog.
        """
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SAVE,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        dialog.set_current_name('document.pdf')

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            fileName = dialog.get_filename()
            self.imgConvert(self.fileList, fileName)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

class Converter:
    def __init__(self):
        self.win = GuiWindow()
        self.win.connect('delete-event', Gtk.main_quit)
        self.win.show_all()
        Gtk.main()