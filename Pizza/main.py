import wx
from defines import *

class GenerateStyle(wx.Frame):
    def __init__(self, parent, title):
        # Létrehozok néhány adatot, hogy később ne kelljen vele szórakozni
        self.kezdo = ("Milyen italt adhatok hozzá?\n", "Adhatok még mást is?\n")
        self.ar = []
        self.rendeles = []
        self.i = 0


        # Létrehozzuk az alap oldalunkat
        screenWidth, screenHeight = wx.DisplaySize()
        super(GenerateStyle, self).__init__(parent, title=title, size=(screenWidth, screenHeight - 100))
        self.panel = wx.Panel(self)
        # Állítunk egy méretező objektumot amire ráfogunk helyezni minden elemet
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        szoveg = wx.StaticText(self.panel, label="Ide írd be, hogy mit szeretnél küldeni a botnak!")
        szoveg.SetFont(self.font)
        self.vbox.Add(szoveg, flag=wx.ALIGN_CENTER)
        self.chat_bot = wx.TextCtrl(self.panel, size=(200, -1))
        self.vbox.Add(self.chat_bot, flag=wx.ALIGN_CENTER)
        chat = wx.Button(self.panel, label="Chat!")
        self.vbox.Add(chat, flag=wx.ALIGN_CENTER)
        chat.Bind(wx.EVT_BUTTON, self.chat_with_bot)
        message = wx.StaticText(self.panel, label="Bot: Szia! Áron vagyok a Tubi Étterem és Pizzéria ChatBotja. Milyen pizzát adhatok neked a mai nap?")
        message.SetFont(self.font)
        self.vbox.Add(message, flag=wx.ALIGN_CENTER)
        self.panel.SetSizer(self.vbox)

    # Ez a függvény adja hozzá a bot és a user sorokat is.
    def chat_with_bot(self, _):
        # Kiszedjük az adatot a szövegdobozból
        data = self.chat_bot.GetValue()
        # Beillesztjük ezt egy Text objektumba és kirakjuk az oldalra
        usermessage = wx.StaticText(self.panel, label=f"User: {data}")
        self.chat_bot.Clear()
        usermessage.SetFont(self.font)
        self.vbox.Add(usermessage, flag=wx.ALIGN_CENTER)
        osszeg, pizza, ital = ellenorzes(data.lower())
        self.ar.append(osszeg)
        if pizza != "":
            self.rendeles.append(pizza)
        if ital != "":
            self.rendeles.append(ital)
        if len(self.kezdo) > self.i:
            botmessage = wx.StaticText(self.panel, label=f"Bot: {self.kezdo[self.i]}")
            botmessage.SetFont(self.font)
            self.vbox.Add(botmessage, flag=wx.ALIGN_CENTER)
        if self.i >= 2 and not("nem" in data.lower()):
            botmessage = wx.StaticText(self.panel, label=f"Bot: Mit adhatok még?")
            botmessage.SetFont(self.font)
            self.vbox.Add(botmessage, flag=wx.ALIGN_CENTER)
            osszeg, pizza, ital = ellenorzes(data)
            self.i -= 2
        self.i += 1
        if self.i >= 2 and "nem" in data.lower():
            print(self.rendeles)
            teljes_ar = 0
            teljes_rendeles = ""
            for data in self.rendeles:
                teljes_rendeles += data
            for i in self.ar:
                teljes_ar += i
            botmessage = wx.StaticText(self.panel, label=f"A rendelésed felvételre került. Rendelés részletei: {teljes_rendeles} Ár: {teljes_ar}")
            botmessage.SetFont(self.font)
            self.vbox.Add(botmessage, flag=wx.ALIGN_CENTER)
        self.generate_panel(self.vbox)

    # Egy a függvény lefrissíti a teljes oldalt ezzel real-time-nak hat a program.
    def generate_panel(self, sizer):
        # Megjelenítések
        self.panel.SetSizer(sizer)
        self.Show()
        # Panel újra rajzolása 
        self.panel.Layout()

if __name__ == "__main__":
    app = wx.App()
    frame = GenerateStyle(None, "Tubi Étterem és Pizzéria")
    frame.Show()
    app.MainLoop()


# Parancs soros verzió.
'''from defines import *

kezdo = ("Milyen italt adhatok hozzá?\n", "Adhatok még mást is?\n")
plusz_penz = ("és", "még", "plusz")
data = input(f"Szia! Áron vagyok a Tubi Étterem és Pizzéria ChatBotja. Milyen pizzát adhatok neked a mai nap?\n").lower()
ar = []
rendeles = []
i = 0
while data != "nem":
    osszeg, pizza, ital = ellenorzes(data)
    ar.append(osszeg)
    if pizza != "":
        rendeles.append(pizza)
    if ital != "":
        rendeles.append(ital)
    print(ar)
    data = input(kezdo[i]).lower()
    if i >= 1 and data.lower() != "nem":
        data = input("Mit adhatok még?")
        osszeg, pizza, ital = ellenorzes(data)
        i -= 1
    if i != 1:
        i += 1

teljes_ar = 0
teljes_rendeles = ""
for data in rendeles:
    teljes_rendeles += data
for i in ar:
    teljes_ar += i

print(f"A rendelésed felvételre került. Rendelés részletei: {teljes_rendeles} Ár: {teljes_ar}")'''