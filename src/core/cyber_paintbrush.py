#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""" """
import os

#strEmojiList = ["((😀))","((🤬))","((😂))","((🙄))","((😴))","((😍))","((😜))","((😆))",\
#	"((😉))","((😵))","((😠))","((😎))","((🥱))","((🥶))","((🤮))","((😶))",\
#	"((😐))","((😨))","((🤡))","((😭))","((👿))","((💀))","((😇))","((😏))"]
strEmojiList = ["blush", "tears", "tongue out", "grin", "aqua eyes", "fangs", "heart-shaped pupils",\
 "angry", "jitome", "pout", "excited", "crazy", "sigh", "heart in eye", "shy", "seductive smile",\
 "sad", "sleepy", "nosebleed", "drunk", "dark_persona", "embarrassed", "cute face"]

strNegative = "ng_deepnegative_v1_75t,  easynegative,\
	(worst quality, low quality:1.4),\
	logo, text, monochrome, NSFW,\
	mutated hands and fingers, poorly drawn hands, ((bad anatomy)),\
	cockeye, walleye"

strBeforeEmoji = "masterpiece, best quality, highres, line art, comic, anime, colorful,\
	solo, upper body, kawaii, 1girl, small breasts, young,\
	close front shoot symmetrical photo portrait,\
	detailed eyes, glowing eyes, heterochromia green golden,\
	emoji,chibi,"
strAfterEmoji = "medium hair, red hair, straight hair, forehead,\
	looking at viewer, fox_ears,\
	simple background, white background,\
	<lora:animeEMOJIStyleLora_v10:1>"

def writeToFile(strFolderPath="./"):
	#正向提示詞
	strPromptsFilePath = os.path.join(strFolderPath, "prompts_file.txt")
	with open(strPromptsFilePath, "w") as f:
		for strEmoji in strEmojiList:
			strPromptsLine = strBeforeEmoji + "(" + strEmoji + ":1.8)," + strAfterEmoji
			f.write(strPromptsLine + "\n")
			print(strPromptsLine)

	#反向提示詞
	strNegativeFilePath = os.path.join(strFolderPath, "negative_file.txt")
	with open(strNegativeFilePath, "w") as f:
		f.write(strNegative + "\n")


if __name__ == '__main__':
	writeToFile()

