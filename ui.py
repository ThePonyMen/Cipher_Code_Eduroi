import wx
from typing import Optional

class Desktopui(wx.Frame):
    def __init__(self, parent = None):
        super().__init__(parent, title="Cipher Eduroi", size=wx.Size(400, 600))

        panel = wx.Panel(self)

        self.saint_button = wx.Button(panel, label="Open Saint")
        self.signal_button = wx.Button(panel, label="Open Signal")

        self.saint_button.Bind(wx.EVT_BUTTON, self.on_open_click)
        self.signal_button.Bind(wx.EVT_BUTTON, self.on_open_click)

        self.cont_archive = None

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.saint_button)
        sizer.Add(self.signal_button)
        panel.SetSizer(sizer)



    def on_open_click(self, event: wx.CommandEvent) -> None:
        button = event.GetEventObject()

        if button is self.saint_button:
            print("Abriendo archivo para Saint...")
        elif button is self.signal_button:
            print("Abriendo archivo para Signal...")

        contenido = self.open_archive()
        if contenido is not None:
            self.cont_archive = contenido
            print("Archivo cargado correctamente.")


    def open_archive(self) -> Optional[str]:
        with wx.FileDialog(
            self,
            message="Selecciona un Archivo",
            wildcard="Archivo de texto (*.txt)|*.txt",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        ) as dlg:
            
            if dlg.ShowModal() == wx.ID_CANCEL:
                return None
            
            cont_archive = dlg.GetPath()

            with open(cont_archive, "r", encoding="utf-8") as f:
                lecture = f.read()

            print("Archivo seleccionado:", cont_archive)
            print(lecture)
            return lecture
    
    def save_archive(self) -> None:
        with wx.FileDialog(
            self,
            message="Guardar",
            wildcard="Archivo de texto (*.txt)|*.txt",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        ) as dlg:
            
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            
            cont_archive = dlg.GetPath()
            
            with open(cont_archive, "w") as f:
                f.write("Hi")