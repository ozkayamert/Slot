import qrcode

kod = qrcode.make("https://www.youtube.com/channel/UCCKf6PD6XTBZDysuhzVybgQ")
kod.save("qrcode.png")