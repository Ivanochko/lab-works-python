#!/usr/bin/python -i
# -*- coding: utf-8 -*-

class color:
	Red = '\033[91m'
	Green = '\033[92m'
	Yellow = '\033[93m'
	Blue = '\033[94m'
	Magenta = '\033[95m'
	Cyan = '\033[96m'
	White = '\033[97m'
	Grey = '\033[90m'
	BOLD = '\033[1m'
	ITALIC = '\033[3m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

print color.Red + "Текст" + color.END
print color.Green + "Текст" + color.END
print color.Yellow + "Текст" + color.END
print color.Blue + "Текст" + color.END
print color.Magenta + "Текст" + color.END
print color.Cyan + "Текст" + color.END
print color.White + "Текст" + color.END
print color.Grey + "Текст" + color.END
print color.BOLD + "Текст" + color.END
print color.ITALIC + "Текст" + color.END
print color.UNDERLINE + "Текст" + color.END