import wx
import wx.lib.colourselect as csel
import random

import LabelBook as LB
from Resources import *


_pageTexts = ["Hello", "From", "wxPython", "LabelBook", "Demo"]
_pageIcons = ["roll.png", "charge.png", "add.png", "decrypted.png", "news.png"]
_pageColours = [wx.RED, wx.GREEN, wx.WHITE, wx.BLUE, "Pink"]

#----------------------------------------------------------------------
def GetMondrianData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\
\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\x00qID\
ATX\x85\xed\xd6;\n\x800\x10E\xd1{\xc5\x8d\xb9r\x97\x16\x0b\xad$\x8a\x82:\x16\
o\xda\x84pB2\x1f\x81Fa\x8c\x9c\x08\x04Z{\xcf\xa72\xbcv\xfa\xc5\x08 \x80r\x80\
\xfc\xa2\x0e\x1c\xe4\xba\xfaX\x1d\xd0\xde]S\x07\x02\xd8>\xe1wa-`\x9fQ\xe9\
\x86\x01\x04\x10\x00\\(Dk\x1b-\x04\xdc\x1d\x07\x14\x98;\x0bS\x7f\x7f\xf9\x13\
\x04\x10@\xf9X\xbe\x00\xc9 \x14K\xc1<={\x00\x00\x00\x00IEND\xaeB`\x82' 


def GetMondrianBitmap():
    return wx.BitmapFromImage(GetMondrianImage())


def GetMondrianImage():
    import cStringIO
    stream = cStringIO.StringIO(GetMondrianData())
    return wx.ImageFromStream(stream)


def GetMondrianIcon():
    icon = wx.EmptyIcon()
    icon.CopyFromBitmap(GetMondrianBitmap())
    return icon


#------------------------------------------------------------
# Show how to derive a custom wxLog class
#------------------------------------------------------------

class MyLog(wx.PyLog):

    def __init__(self, textCtrl, logTime=0):

        wx.PyLog.__init__(self)
        self.tc = textCtrl
        self.logTime = logTime


    def DoLogString(self, message, timeStamp):

        if self.tc:
            self.tc.AppendText(message + '\n')


#----------------------------------------------------------------------
class SamplePane(wx.Panel):
    """
    Just a simple test window to put into the LabelBook.
    """
    def __init__(self, parent, colour, label):

        wx.Panel.__init__(self, parent, style=wx.BORDER_SUNKEN)
        self.SetBackgroundColour(colour)

        label = label + "\nEnjoy the LabelBook && FlatImageBook demo!"
        static = wx.StaticText(self, -1, label, pos=(10, 10))        

#----------------------------------------------------------------------
            
class LabelBookDemo(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY,
                 title="LabelBook & FlatImageBook wxPython Demo ;-)"):

        wx.Frame.__init__(self, parent, id, title)

        self.initializing = True        

        # Add log window
        self.log = wx.TextCtrl(self, wx.ID_ANY, "", size=(-1, 100),
                          style=wx.TE_MULTILINE|wx.TE_READONLY|
                          wx.SUNKEN_BORDER)
        wx.Log_SetActiveTarget(MyLog(self.log))

        self.splitter = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER|
                                          wx.SP_LIVE_UPDATE|wx.SP_3DSASH)
        self.mainpanel = wx.Panel(self.splitter, -1)
        self.leftpanel = wx.Panel(self.splitter, -1, style=wx.SUNKEN_BORDER)

        self.sizer_3_staticbox = wx.StaticBox(self.leftpanel, -1, "Book Styles")
        self.sizer_4_staticbox = wx.StaticBox(self.leftpanel, -1, "Colours")

        radioList = ["LabelBook", "FlatImageBook"]
        self.labelbook = wx.RadioBox(self.leftpanel, -1, "Book Type", wx.DefaultPosition,
                                     wx.DefaultSize, radioList, 2, wx.RA_SPECIFY_ROWS)

        radioList = ["Left", "Right", "Top", "Bottom"]
        self.bookdirection = wx.RadioBox(self.leftpanel, -1, "Book Orientation",
                                         wx.DefaultPosition, wx.DefaultSize, radioList,
                                         2, wx.RA_SPECIFY_ROWS)

        self.border = wx.CheckBox(self.leftpanel, -1, "Draw Book Border")
        self.onlytext = wx.CheckBox(self.leftpanel, -1, "Show Only Text")
        self.onlyimages = wx.CheckBox(self.leftpanel, -1, "Show Only Images")
        self.shadow = wx.CheckBox(self.leftpanel, -1, "Draw Shadows")
        self.pin = wx.CheckBox(self.leftpanel, -1, "Use Pin Button")
        self.gradient = wx.CheckBox(self.leftpanel, -1, "Draw Gradient Shading")
        self.web = wx.CheckBox(self.leftpanel, -1, "Web Highlight")
        self.background = csel.ColourSelect(self.leftpanel, -1, "Choose...",
                                            wx.Colour(127, 169, 241), size=(-1, 20))
        self.activetab = csel.ColourSelect(self.leftpanel, -1, "Choose...",
                                           wx.Colour(251, 250, 247), size=(-1, 20))
        self.tabsborder = csel.ColourSelect(self.leftpanel, -1, "Choose...",
                                            wx.Colour(172, 168, 153), size=(-1, 20))
        self.textcolour = csel.ColourSelect(self.leftpanel, -1, "Choose...",
                                            wx.BLACK, size=(-1, 20))
        self.activetextcolour = csel.ColourSelect(self.leftpanel, -1, "Choose...",
                                                  wx.BLACK, size=(-1, 20))
        self.hilite = csel.ColourSelect(self.leftpanel, -1, "Choose...",
                                        wx.Colour(191, 216, 216), size=(-1, 20))
        
        self.__set_properties()

        self.CreateLabelBook()
        
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBOX, self.OnBookType, self.labelbook)
        self.Bind(wx.EVT_RADIOBOX, self.OnBookOrientation, self.bookdirection)
        
        self.Bind(wx.EVT_CHECKBOX, self.OnStyle, self.border)
        self.Bind(wx.EVT_CHECKBOX, self.OnStyle, self.onlytext)
        self.Bind(wx.EVT_CHECKBOX, self.OnStyle, self.onlyimages)
        self.Bind(wx.EVT_CHECKBOX, self.OnStyle, self.shadow)
        self.Bind(wx.EVT_CHECKBOX, self.OnStyle, self.pin)
        self.Bind(wx.EVT_CHECKBOX, self.OnStyle, self.gradient)
        self.Bind(wx.EVT_CHECKBOX, self.OnStyle, self.web)

        self.Bind(csel.EVT_COLOURSELECT, self.OnBookColours, self.background)
        self.Bind(csel.EVT_COLOURSELECT, self.OnBookColours, self.activetab)
        self.Bind(csel.EVT_COLOURSELECT, self.OnBookColours, self.activetextcolour)
        self.Bind(csel.EVT_COLOURSELECT, self.OnBookColours, self.tabsborder)
        self.Bind(csel.EVT_COLOURSELECT, self.OnBookColours, self.textcolour)
        self.Bind(csel.EVT_COLOURSELECT, self.OnBookColours, self.hilite)

        self.Bind(LB.EVT_IMAGENOTEBOOK_PAGE_CHANGING, self.OnPageChanging)
        self.Bind(LB.EVT_IMAGENOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(LB.EVT_IMAGENOTEBOOK_PAGE_CLOSING, self.OnPageClosing)
        self.Bind(LB.EVT_IMAGENOTEBOOK_PAGE_CLOSED, self.OnPageClosed)
        
        
        statusbar = self.CreateStatusBar(2, wx.ST_SIZEGRIP)
        statusbar.SetStatusWidths([-2, -1])
        # statusbar fields
        statusbar_fields = [("LabelBook & FlatImageBook wxPython Demo, Andrea Gavana @ 03 Nov 2006"),
                            ("Welcome To wxPython!")]

        for i in range(len(statusbar_fields)):
            statusbar.SetStatusText(statusbar_fields[i], i)
            
        self.CreateMenu()

        xvideo = wx.SystemSettings_GetMetric(wx.SYS_SCREEN_X)
        yvideo = wx.SystemSettings_GetMetric(wx.SYS_SCREEN_Y)

        self.SetSize((3*xvideo/4, 6*yvideo/7))

        self.SetIcon(GetMondrianIcon())  
        self.CenterOnScreen()

        self.initializing = False
        self.SendSizeEvent()
        
        
    def __set_properties(self):

        self.pin.SetValue(1)
        self.splitter.SetMinimumPaneSize(120)


    def __do_layout(self):

        mainsizer = wx.BoxSizer(wx.VERTICAL)
        panelsizer = wx.BoxSizer(wx.VERTICAL)
        leftsizer = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.VERTICAL)
        sizer_4 = wx.StaticBoxSizer(self.sizer_4_staticbox, wx.VERTICAL)
        gridsizer = wx.FlexGridSizer(6, 2, 5, 5)
        
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.labelbook, 0, wx.ALL, 3)
        leftsizer.Add(sizer_1, 0, wx.ALL|wx.EXPAND, 5)
        sizer_2.Add(self.bookdirection, 0, wx.ALL, 3)
        leftsizer.Add(sizer_2, 0, wx.ALL|wx.EXPAND, 5)

        sizer_3.Add(self.border, 0, wx.ALL, 3)        
        sizer_3.Add(self.onlytext, 0, wx.LEFT|wx.BOTTOM, 3)
        sizer_3.Add(self.onlyimages, 0, wx.LEFT|wx.BOTTOM, 3)
        sizer_3.Add(self.shadow, 0, wx.LEFT|wx.BOTTOM, 3)
        sizer_3.Add(self.pin, 0, wx.LEFT|wx.BOTTOM, 3)
        sizer_3.Add(self.gradient, 0, wx.LEFT|wx.BOTTOM, 3)
        sizer_3.Add(self.web, 0, wx.LEFT|wx.BOTTOM, 3)
        leftsizer.Add(sizer_3, 0, wx.ALL|wx.EXPAND, 5)

        label1 = wx.StaticText(self.leftpanel, -1, "Tab Area Background Colour: ")
        label2 = wx.StaticText(self.leftpanel, -1, "Active Tab Colour: ")
        label3 = wx.StaticText(self.leftpanel, -1, "Tabs Border Colour: ")
        label4 = wx.StaticText(self.leftpanel, -1, "Text Colour: ")
        label5 = wx.StaticText(self.leftpanel, -1, "Active Tab Text Colour: ")
        label6 = wx.StaticText(self.leftpanel, -1, "Tab Highlight Colour: ")

        gridsizer.Add(label1, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 3)
        gridsizer.Add(self.background, 0)
        gridsizer.Add(label2, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 3)
        gridsizer.Add(self.activetab, 0)
        gridsizer.Add(label3, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 3)
        gridsizer.Add(self.tabsborder, 0)
        gridsizer.Add(label4, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 3)
        gridsizer.Add(self.textcolour, 0)
        gridsizer.Add(label5, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 3)
        gridsizer.Add(self.activetextcolour, 0)
        gridsizer.Add(label6, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 3)
        gridsizer.Add(self.hilite, 0)

        sizer_4.Add(gridsizer, 1, wx.EXPAND)
        gridsizer.Layout()
        leftsizer.Add(sizer_4, 0, wx.ALL|wx.EXPAND, 5)

        self.leftpanel.SetSizer(leftsizer)
        leftsizer.Layout()
        leftsizer.SetSizeHints(self.leftpanel)
        leftsizer.Fit(self.leftpanel)

        panelsizer.Add(self.book, 1, wx.EXPAND, 0)
        self.mainpanel.SetSizer(panelsizer)
        panelsizer.Layout()

        self.splitter.SplitVertically(self.leftpanel, self.mainpanel, 200)
        mainsizer.Add(self.splitter, 1, wx.EXPAND, 0)
        mainsizer.Add(self.log, 0, wx.EXPAND)

        self.SetSizer(mainsizer)
        mainsizer.Layout()
        self.Layout()


    def CreateLabelBook(self, btype=0):

        if not self.initializing:
            self.Freeze()
            panelsizer = self.mainpanel.GetSizer()
            panelsizer.Detach(0)
            self.book.Destroy()
        else:
            self.imagelist = self.CreateImageList()

        style = self.GetBookStyles()
        
        if btype == 0: # it is a labelbook:
            self.book = LB.LabelBook(self.mainpanel, -1, style=style)
            if self.bookdirection.GetSelection() > 1:
                self.bookdirection.SetSelection(0)

            self.SetUserColours()                

        else:
            self.book = LB.FlatImageBook(self.mainpanel, -1, style=style)

        self.EnableChoices(btype)            

        self.book.AssignImageList(self.imagelist)

        for indx, txts in enumerate(_pageTexts):
            label = "This is panel number %d"%(indx+1)
            self.book.AddPage(SamplePane(self.book, _pageColours[indx], label),
                              txts, True, indx)

        self.book.SetSelection(0)            
 
        if not self.initializing:
            panelsizer.Add(self.book, 1, wx.EXPAND)
            panelsizer.Layout()
            self.GetSizer().Layout()
            self.Layout()
            self.Thaw()

        self.SendSizeEvent()


    def EnableChoices(self, btype):

        self.bookdirection.EnableItem(2, btype)
        self.bookdirection.EnableItem(3, btype)
        self.onlyimages.Enable(btype)
        self.onlytext.Enable(btype)
        self.gradient.Enable(not btype)
        self.web.Enable(not btype)
        self.shadow.Enable(not btype)
        self.background.Enable(not btype)
        self.activetab.Enable(not btype)
        self.activetextcolour.Enable(not btype)
        self.textcolour.Enable(not btype)
        self.hilite.Enable(not btype)
        self.tabsborder.Enable(not btype)
        

    def GetBookStyles(self):

        style = INB_FIT_BUTTON
        style = self.GetBookOrientation(style)
        
        if self.onlytext.IsEnabled() and self.onlytext.GetValue():
            style |= INB_SHOW_ONLY_TEXT
        if self.onlyimages.IsEnabled() and self.onlyimages.GetValue():
            style |= INB_SHOW_ONLY_IMAGES
        if self.pin.GetValue():
            style |= INB_USE_PIN_BUTTON
        if self.shadow.GetValue():
            style |= INB_DRAW_SHADOW
        if self.web.GetValue():
            style |= INB_WEB_HILITE
        if self.gradient.GetValue():
            style |= INB_GRADIENT_BACKGROUND
        if self.border.GetValue():
            style |= INB_BORDER
            
        return style            
        

    def CreateImageList(self):

        imagelist = wx.ImageList(32, 32)
        for img in _pageIcons:
            bmp = wx.Bitmap(img, wx.BITMAP_TYPE_PNG)
            imagelist.Add(bmp)
        
        return imagelist

        
    def GetBookOrientation(self, style):

        selection = self.bookdirection.GetSelection()
        if selection == 0:
            style |= INB_LEFT
        elif selection == 1:
            style |= INB_RIGHT
        elif selection == 2:
            style |= INB_TOP
        else:
            style |= INB_BOTTOM

        return style
    
        
    def OnBookType(self, event):

        self.CreateLabelBook(event.GetInt())
        event.Skip()


    def OnBookOrientation(self, event):

        style = self.GetBookStyles()
        self.book.SetWindowStyleFlag(style)
        
        event.Skip()


    def OnStyle(self, event):

        style = self.GetBookStyles()
        self.book.SetWindowStyleFlag(style)
        
        event.Skip()


    def OnBookColours(self, event):

        obj = event.GetId()
        colour = event.GetValue()
        
        if obj == self.background.GetId():
            self.book.SetColour(INB_TAB_AREA_BACKGROUND_COLOR, colour)
        elif obj == self.activetab.GetId():
            self.book.SetColour(INB_ACTIVE_TAB_COLOR, colour)
        elif obj == self.tabsborder.GetId():
            self.book.SetColour(INB_TABS_BORDER_COLOR, colour)
        elif obj == self.textcolour.GetId():
            self.book.SetColour(INB_TEXT_COLOR, colour)
        elif obj == self.activetextcolour.GetId():
            self.book.SetColour(INB_ACTIVE_TEXT_COLOR, colour)
        else:
            self.book.SetColour(INB_HILITE_TAB_COLOR, colour)

        self.book.Refresh()
        

    def SetUserColours(self):

        self.book.SetColour(INB_TAB_AREA_BACKGROUND_COLOR, self.background.GetColour())
        self.book.SetColour(INB_ACTIVE_TAB_COLOR, self.activetab.GetColour())
        self.book.SetColour(INB_TABS_BORDER_COLOR, self.tabsborder.GetColour())
        self.book.SetColour(INB_TEXT_COLOR, self.textcolour.GetColour())
        self.book.SetColour(INB_ACTIVE_TEXT_COLOR, self.activetextcolour.GetColour())
        self.book.SetColour(INB_HILITE_TAB_COLOR, self.hilite.GetColour())


    def OnPageChanging(self, event):

        oldsel = event.GetOldSelection()
        newsel = event.GetSelection()
        self.log.AppendText("Page Changing From: " + str(oldsel) + " To: " + str(newsel) + "\n")
        event.Skip()


    def OnPageChanged(self, event):

        newsel = event.GetSelection()
        self.log.AppendText("Page Changed To: " + str(newsel) + "\n")
        event.Skip()


    def OnPageClosing(self, event):

        newsel = event.GetSelection()
        self.log.AppendText("Closing Page: " + str(newsel) + "\n")
        event.Skip()


    def OnPageClosed(self, event):

        newsel = event.GetSelection()
        self.log.AppendText("Closed Page: " + str(newsel) + "\n")
        event.Skip()


    def OnAddPage(self, event):

        pageCount = self.book.GetPageCount()
        indx = random.randint(0, 4)
        label = "This is panel number %d"%(pageCount+1)
        self.book.AddPage(SamplePane(self.book, _pageColours[indx], label),
                          "Added Page", True, indx)
        

    def OnDeletePage(self, event):

        msg = "Please Enter The Page Number You Want To Remove:"
        dlg = wx.TextEntryDialog(self, msg, "Enter Page")

        if dlg.ShowModal() != wx.ID_OK:
            dlg.Destroy()
            return
        
        userString = dlg.GetValue()
        dlg.Destroy()
        
        try:
            page = int(userString)
        except:
            return

        if page < 0 or page > self.book.GetPageCount() - 1:
            return
        
        self.book.DeletePage(page)


    def OnDeleteAllPages(self, event):

        self.book.DeleteAllPages()        

        
    def CreateMenu(self):

        menuBar = wx.MenuBar(wx.MB_DOCKABLE)
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        helpMenu = wx.Menu()
        
        item = wx.MenuItem(fileMenu, wx.ID_ANY, "E&xit")
        self.Bind(wx.EVT_MENU, self.OnQuit, item)
        fileMenu.AppendItem(item)

        item = wx.MenuItem(editMenu, wx.ID_ANY, "Add Page")
        self.Bind(wx.EVT_MENU, self.OnAddPage, item)
        editMenu.AppendItem(item)

        editMenu.AppendSeparator()
        
        item = wx.MenuItem(editMenu, wx.ID_ANY, "Delete Page")
        self.Bind(wx.EVT_MENU, self.OnDeletePage, item)
        editMenu.AppendItem(item)
        
        item = wx.MenuItem(editMenu, wx.ID_ANY, "Delete All Pages")
        self.Bind(wx.EVT_MENU, self.OnDeleteAllPages, item)
        editMenu.AppendItem(item)
                        
        item = wx.MenuItem(helpMenu, wx.ID_ANY, "About")
        self.Bind(wx.EVT_MENU, self.OnAbout, item)
        helpMenu.AppendItem(item)

        menuBar.Append(fileMenu, "&File")
        menuBar.Append(editMenu, "&Edit")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)


    def OnQuit(self, event):

    	self.Destroy()


    def OnAbout(self, event):

        msg = "This Is The About Dialog Of The LabelBook & FlatImageBook Demo.\n\n" + \
              "Author: Andrea Gavana @ 03 Nov 2006\n\n" + \
              "Please Report Any Bug/Requests Of Improvements\n" + \
              "To Me At The Following Adresses:\n\n" + \
              "andrea.gavana@gmail.com\n" + "gavana@kpo.kz\n\n" + \
              "Welcome To wxPython " + wx.VERSION_STRING + "!!"
              
        dlg = wx.MessageDialog(self, msg, "LabelBook wxPython Demo",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        

def main():

    app = wx.PySimpleApp()
    frame = LabelBookDemo(None, -1)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
    
