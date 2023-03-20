#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""" """
import os

strEmojiList = ["(((angry)))",
"(((cosy)))",
"(((depressing)))",
"(((disgusting)))",
"(((embarrassing)))",
"(((energetic)))",
"(((evil)))",
"(((fearful)))",
"(((frightening)))",
"(((grim)))",
"(((guilty)))",
"(((happy)))",
"(((hopeful)))",
"(((hopeless)))",
"(((lonely)))",
"(((lustful)))",
"(((peaceful)))",
"(((proud)))",
"(((relieving)))",
"(((romantic)))",
"(((sad)))",
"(((satisfying)))",
"(((shameful)))",
"(((surprising)))",
"(((resist)))",
"(((smile)))",
"(((sigh)))",
"(((cry)))",
"(((cry hard)))",
"(((move)))",
"(((laughing out loud)))",
"(((naughty)))",
"(((wink)))",
"(((scold)))",
"(((glutton)))"]

strBasicList = ["masterpiece", "best quality", "high resolution", "ultra detailed", "solo"]
strCustomedList = ["1boy", "(cool boy face)", "in the forest", "dark hair", "short hair", "((symmetrical face))"]
#strLoraSettingList = ["flat color", "big head style", "detailed eyes",
#	"<lora:cartoonyStyle_cartoonyStyleV1:1>"]

strBeforeEmoji = "close front shoot symmetrical photo portrait of one young male werewolf"
strAfterEmoji = " with wolf ears"

def writeToFile(strFolderPath="./"):
	strFilePath = os.path.join(strFolderPath, "prompts_file.txt")
	with open(strFilePath, "w") as f:
		for strEmoji in strEmojiList:

			strPromptLine = strBeforeEmoji + strEmoji + strAfterEmoji + ", " + \
				','.join(strBasicList) + ", " + \
				','.join(strCustomedList)
				#','.join(strCustomedList) + ", " + \
				#','.join(strLoraSettingList)
			f.write(strPromptLine + "\n")
			print(strPromptLine)



if __name__ == '__main__':
	writeToFile()

""" negative
ng_deepnegative_v1_75t,  easynegative, (worst quality, low quality:1.4), logo, text, monochrome, NSFW, mutated hands and fingers, poorly drawn hands, ((bad anatomy))
"""
