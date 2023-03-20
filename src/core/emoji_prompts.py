#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""" """

"""
masterpiece, best quality, high resolution, ultra detailed, solo, 1girl,
red eyes, silver hair, ponytail, black dress, fox ears,
((insecure)),
flat color, upper body, pure white background, big head style, detailed eyes,
<lora:cartoonyStyle_cartoonyStyleV1:1>
"""
strEmojiList = ["(((happy)))", "(((angry)))", "(((crying)))", "(((laughing out loud)))"]
strBasicList = ["masterpiece", "best quality", "high resolution", "ultra detailed", "solo"]
strCustomedList = ["1boy", "blue eyes", "orange hair", "short hair", "white dress", "bear ears"]
strLoraSettingList = ["flat color", "upper body", "pure white background", "big head style", "detailed eyes",
	"<lora:cartoonyStyle_cartoonyStyleV1:1>"]


def main():
	with open("prompts_file.txt", "w") as f:
		for strEmoji in strEmojiList:
			strPromptLine = ','.join(strBasicList) + \
				", " + strEmoji + ", " + \
				','.join(strCustomedList) + \
				','.join(strLoraSettingList)
			f.write(strPromptLine + "\n")
			print(strPromptLine)



if __name__ == '__main__':
	main()