import wx


def click_save_button(event):
    save_file = open('data/Py-File.py', 'w')
    save_file.write(text.GetValue())
    save_file.close()


if __name__ == '__main__':
    window = wx.App()
    frame = wx.Frame(None, -1, 'PythonEdit', size=(1000, 750))

    panel = wx.Panel(frame, -1)
    save_button = wx.Button(panel, -1, pos=(10, 10), label='Save')

    text = wx.TextCtrl(panel, -1, pos=(10, 50),
                       size=(965, 650), style=wx.TE_MULTILINE)
    save_button.Bind(wx.EVT_BUTTON, click_save_button)
    frame.Show()
    window.MainLoop()
