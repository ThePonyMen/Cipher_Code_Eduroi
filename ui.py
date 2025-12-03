import wx
from typing import Optional
from encryption import Algorithm_Eduroi

class Desktopui(wx.Frame):
    def __init__(self, parent = None):
        super().__init__(parent, title="Cipher Eduroi", size=wx.Size(400, 600))

        panel = wx.Panel(self)

        self.saint_button = wx.Button(panel, label="Open Saint")
        self.signal_button = wx.Button(panel, label="Open Signal")
        self.msg_button = wx.Button(panel, label="Open Message")
        self.exec_button = wx.Button(panel, label="Execute")

        self.Edu = Algorithm_Eduroi()

        self.conten_saint = None
        self.conten_signal = None
        self.conten_msg = None

        self.saint_button.Bind(wx.EVT_BUTTON, self.on_open_click)
        self.signal_button.Bind(wx.EVT_BUTTON, self.on_open_click)
        self.msg_button.Bind(wx.EVT_BUTTON, self.on_open_click)
        self.exec_button.Bind(wx.EVT_BUTTON, self.explotion)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.saint_button)
        sizer.Add(self.signal_button)
        sizer.Add(self.msg_button)
        sizer.Add(self.exec_button)
        panel.SetSizer(sizer)



    def on_open_click(self, event) -> None:
        button = event.GetEventObject()

        if button is self.saint_button:
            print("Abriendo archivo para Saint...")
            self.conten_saint = self.open_archive()

        elif button is self.signal_button:
            print("Abriendo archivo para Signal...")
            self.conten_signal = self.open_archive()

        elif button is self.msg_button:
            print("Abriendo archivo para Signal...")
            self.conten_msg = self.open_archive()

    def explotion(self):
        self.conten_signal = self.Edu.Encript(self.conten_saint, self.conten_msg)
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