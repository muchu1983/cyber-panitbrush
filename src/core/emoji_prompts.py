#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""" """
import os
strPromptsStart = '--prompt "'
#strProList = ['cra', 'eniripsa', 'iop', 'osamodas', 'sacrier', 'sram', 'xelor']
strProList = ['cra']
strEmojiList = ['happy', 'sad', 'scared']

strPrompts = 'masterpiece, best quality, highres,\
    chibi, flat color, outline,\
    1girl, beautiful, full body, standing,\
    ponytail, short hair, red hair, forehead,\
    high detailed skin, extremely_detailed_eyes_and_face,\
    pants,\
    simple background, white background,\
    <lora:Toru8pWavenChibiStyle_wavenchibiLoraV10:1>, " '
    #colored skin, looking at viewer, bandages, bandaged head, 
    
strNegatives = ' --negative_prompt "easynegative, ng_deepnegative_v1_75t,\
    worst quality, low quality, normal quality, lowres, blurry,\
    exposed breast, nipples, NSFW, (bad anatomy:2),\
    mutated hands and fingers, poorly drawn hands, bad hands, missing finger, extra digits, fewer digits,\
    cockeye, walleye,\
    monochrome, logo, text, error, signature, watermark, username, artist name,\
    tattoo, \
    turn pale, gloom \\(expression\\), "'
    #weapon,




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

