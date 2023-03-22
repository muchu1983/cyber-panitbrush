#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""" """
import os

strEmojiList = ["((😀))","((🤬))","((😂))","((🙄))","((😴))","((😍))","((😜))","((😆))",\
	"((😉))","((😵))","((😠))","((😎))","((🥱))","((🥶))","((🤮))","((😶))",\
	"((😐))","((😨))","((🤡))","((😭))","((👿))","((💀))","((😇))","((😏))"]

strNegative = "ng_deepnegative_v1_75t,  easynegative, (worst quality, low quality:1.4), logo, text, monochrome, NSFW, mutated hands and fingers, poorly drawn hands, ((bad anatomy))"

strBeforeEmoji = "masterpiece, best quality, highres, line art, comic, anime, colorful, \
	 solo, upper body, kawaii, 1girl, small breasts, Age:18, big head style, detailed eyes, \
	 close front shoot symmetrical photo portrait"
strAfterEmoji = ", medium hair, split-color hair, brown hair, purple hair, straight hair, hair strand, \
	hair wings, crossed bangs,  looking at viewer, fox_ears, green eyes, glowing eyes, boots, \
	simple background, white background"

def writeToFile(strFolderPath="./"):
	#正向提示詞
	strPromptsFilePath = os.path.join(strFolderPath, "prompts_file.txt")
	with open(strPromptsFilePath, "w") as f:
		for strEmoji in strEmojiList:
			strPromptsLine = strBeforeEmoji + strEmoji + strAfterEmoji
			f.write(strPromptsLine + "\n")
			print(strPromptsLine)

	#反向提示詞
	strNegativeFilePath = os.path.join(strFolderPath, "negative_file.txt")
	with open(strNegativeFilePath, "w") as f:
		f.write(strNegative + "\n")


if __name__ == '__main__':
	writeToFile()

