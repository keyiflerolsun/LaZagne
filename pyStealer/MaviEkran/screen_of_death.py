# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import tkinter as tk

mesaj = """
				! Please Wait !


A problem has been detected and windows has been shutdown to prevent damage to your computer.

If this is the first time you've seen this stop error screen, restart your computer, If this screen appears again, follow these steps:

Check to make sure any new hardware or software is properly installed. If this is a new installation, ask your hardware or software manufacturer for any windows updates you might need.

If problems continue, disable or remove any newly installed hardware or software. Disable BIOS memory options such as caching or shadowing. If you need to use Safe Mode to remove or disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode.

Technical information:

        *** gv3.sys - Address F86B5A89 base at F86B5000, DateStamp 3dd9919eb

Beginning dump of physical memory

Physical memory dump complete.

Contact your system administrator or technical support group for further assistance.
"""

pencere = tk.Tk()

import platform
hedef_sistem = platform.system()
if hedef_sistem == "Windows":    
	import winsound
	pencere.after(100, lambda: winsound.PlaySound("SystemHand", winsound.SND_ALIAS))
	pencere.config(cursor = "circle")
else:
    pencere.config(cursor = "none")

pencere.attributes("-fullscreen", True)
pencere.config(bg = "#000088")
# pencere.bind("<Escape>", lambda event: pencere.destroy())

cerceve = tk.Frame(pencere, bg = "#000088")
cerceve.place(relx = 0, rely = 0)

etiket = tk.Label(cerceve, text = mesaj, bg = "#000088", fg = "white", justify = "left", wraplength = 1000, font = ("Lucida Console", "16"))
etiket.pack(ipadx = 75, ipady = 75, fill = "y")

if __name__ == '__main__':
    pencere.mainloop()