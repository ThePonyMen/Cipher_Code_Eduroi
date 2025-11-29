import wx
from ui import Desktopui

def main():
    app = wx.App()
    f = Desktopui()
    f.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()