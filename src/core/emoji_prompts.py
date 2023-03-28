#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""" """
import os

#strEmojiList = ["((😀))","((🤬))","((😂))","((🙄))","((😴))","((😍))","((😜))","((😆))",\
#   "((😉))","((😵))","((😠))","((😎))","((🥱))","((🥶))","((🤮))","((😶))",\
#   "((😐))","((😨))","((🤡))","((😭))","((👿))","((💀))","((😇))","((😏))"]
strEmojiList = ['blush', 'tongue out', 'tears', 'grin', 'embarrassed',\
    'fangs', 'angry', 'smug', 'evil smile', 'sleepy' ]

strNegative = 'easynegative, worst quality, low quality, normal quality, lowres,\
    blurry, girl, woman, female, exposed breast, nipples, NSFW,\
    mutated hands and fingers, poorly drawn hands, bad hands,missing finger, extra digits, fewer digits,\
    monochrome, logo, text, error, signature, watermark, username, artist name,\
    tattoo, weapon, cockeye, walleye, (bad anatomy:2), '

strBeforeEmoji = 'masterpiece, best quality, highres,\
    <lora:Moxin_10:0.5>,  shuimobysim, badashanren,\
    <lora:reinhardtOverwatch_v1:0.8>, 1man, old man, reinhardt,\
    (muscular male:1.3), strong body, male focus, abdominal muscles, '
strAfterEmoji = 'extremely_detailed_eyes_and_face, detailed eyes, Fire in eyes, extremely detailed eyes,\
    ponytail, long hair, brown hair, forehead, \
    beard,  goatee, stubble, \
    upper body, high detailed skin,  looking at viewer,\
    (topless male:1.2), shirtless ,pants,\
    simple background, white background, '

def writeToFile(strFolderPath="./"):
    #正向提示詞
    strPromptsFilePath = os.path.join(strFolderPath, "line_prompts_file.txt")
    with open(strPromptsFilePath, "w") as f:
        for strEmoji in strEmojiList:
            strPromptsLine = strBeforeEmoji + "(" + strEmoji + ":1.5)," + strAfterEmoji
            f.write(strPromptsLine + "\n")
            print(strPromptsLine)

    #反向提示詞
    strNegativeFilePath = os.path.join(strFolderPath, "line_negative_file.txt")
    with open(strNegativeFilePath, "w") as f:
        f.write(strNegative + "\n")

def main():
    writeToFile()

if __name__ == '__main__':
    main()

