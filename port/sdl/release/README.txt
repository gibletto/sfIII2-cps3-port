Street Fighter III 2nd Impact for Windows
=========================================

A native port of the arcade game (not an emulator). This zip contains NO game data: you need your own copy of
the arcade ROM set.

https://github.com/gibletto/sfiii2-cps3-port

1. Add the ROM set
------------------
Put the MAME ROM set sfiii2n.zip (non-merged) in the roms folder, as it is. Nothing to convert:

    roms/sfiii2n.zip

2. Play
-------
Run sf2i.exe. The settings and high scores are saved in roms/eeprom.bin.

    Arrows            move
    A  S  D           light / medium / heavy punch
    Z  X  C           light / medium / heavy kick
    5 then 1          insert a coin, then start (6 and 2 for player 2)
    F2                operator (test) menu: settings, free play
    9                 service coin (a free credit)
    Alt+Enter, F11    full screen
    F12               screenshot (frame.bmp)
    Escape            quit

Game controllers work too (the first is player 1, the second player 2): D-pad or left stick to move, X Y RB
punches, A B RT kicks, Start, and Back for a coin.

In the operator menu (F2), CONFIGURATION has the game and coin settings, including free play.

Region: the game plays in the region of the ROM set's BIOS (Asia). To play in another, set REGION in
roms/settings.ini (written the first time the game runs) to JAPAN, ASIA, EUROPE, USA, HISPANIC, BRAZIL or
OCEANIA (BIOS goes back). The region also sets the language of the text: Japanese in Japan, Spanish in
Hispanic, Portuguese in Brazil, English elsewhere. In Europe the operator menu (SYSTEM CONFIGURATION,
LANGUAGE) can switch it to Spanish. Changing the region resets the operator settings to that region's, as on
the arcade.

Screen: SCREEN in roms/settings.ini is SQUARE (the default, square pixels) or 4:3 (the shape a 4:3 arcade
monitor gave them, a narrower picture). SCALE is INTEGER (the default: the height a whole multiple of the
game's, so lines stay sharp), PERFECT (every pixel the same size; with 4:3 the nearest whole-number shape) or
FIT (as big as the window). On a 4K screen, 4:3 with INTEGER is exactly 7x9 screen pixels per game pixel.

You can also start it as sf2i.exe <path to sfiii2n.zip>.

Street Fighter and Capcom are trademarks of Capcom. This project is not affiliated with or endorsed by Capcom.
