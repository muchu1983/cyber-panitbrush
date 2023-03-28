#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""" """
import os
strPromptsStart = '--prompt "'
strProList = ['cra', 'eniripsa', 'iop', 'osamodas', 'sacrier', 'sram', 'xelor']
strEmojiList = ['happy', 'sad', 'scared']

strPrompts = 'masterpiece, best quality, highres,\
    1girl, beautiful, full body, looking at viewer,\
    extremely_detailed_eyes_and_face,\
    ponytail, long hair, brown hair, forehead,\
    high detailed skin,\
    pants,\
    simple background, white background,\
    <lora:Toru8pWavenChibiStyle_wavenchibiLoraV10:0.8>, " '
    #colored skin, bandages,

strNegatives = ' --negative_prompt "easynegative, ng_deepnegative_v1_75t,\
    worst quality, low quality, normal quality, lowres, blurry,\
    exposed breast, nipples, NSFW, (bad anatomy:2),\
    mutated hands and fingers, poorly drawn hands, bad hands, missing finger, extra digits, fewer digits,\
    cockeye, walleye,\
    monochrome, logo, text, error, signature, watermark, username, artist name,\
    tattoo, weapon,\
    turn pale, gloom (expression), "'




def writeToFile(strFolderPath="./"):
    #提示詞
    strPromptsFilePath = os.path.join(strFolderPath, "line_prompts_file.txt")
    with open(strPromptsFilePath, "w") as f:
        for strPro in strProList:
            for strEmoji in strEmojiList:
                strPromptsLine = strPromptsStart +\
                "(" + strPro + ")," +\
                "(" + strEmoji + ")," +\
                strPrompts +\
                strNegatives
                f.write(strPromptsLine + "\n")
                print(strPromptsLine)

def main():
    writeToFile()

if __name__ == '__main__':
    main()

