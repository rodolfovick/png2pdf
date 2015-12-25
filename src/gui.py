#! /usr/bin/python

# PNG2PDF - Graphic interface related class and methods.

from convert import imgConvert
from gi.repository import Gtk, Gio

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
            self.fileList.append(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def saveFile(self, widget):
        """
        Save file name (PDF) dialog.
        """
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            fileName = dialog.get_filename()+'/ww.pdf'
            imgConvert(self.fileList, fileName)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

def guiStart():
    """
    Create object instance and initiate main window.
    """
    win = GuiWindow()
    win.connect('delete-event', Gtk.main_quit)
    win.show_all()
    Gtk.main()
    return win
