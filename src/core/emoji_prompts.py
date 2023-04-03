#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" """
import os
strHairColorList = ['red hair', 'green hair', 'blue hair',]
strEmojiList = ['happy', 'sad', 'scared', 'angry', 'cosy', 'depressing', 'disgusting', 'embarrasing', 'energetic',
    'evil', 'fearful', 'frightening', 'grim', 'guilty', 'hopeful', 'hopeless', 'lonely', 'lustful', 'peaceful',
    'proud', 'relieving', 'romantic', 'resist', 'smile', 'sigh', 'cry', 'cry hard', 'move', 'laughing out loud',
    'naughty', 'wink', 'scold', 'glutton']
strPromptsStart = '--prompt "'
strNegativesStart = '--negative_prompt "'
strPnNEnd = '" '
strPrompts = 'masterpiece, best quality, highres,\
    simple background, white background,\
    1girl, beautiful, upper body,\
    forehead, pants,\
    <lora:Toru8pWavenChibiStyle_wavenchibiLoraV10:1>,\
    cra, chibi, outline,'
    
strNegatives = 'worst quality, low quality, normal quality, lowres, blurry,\
    badhandv4, bad anatomy, cockeye, walleye,\
    nsfw, monochrome, logo, text, error, signature, watermark, username, artist name,\
    turn pale, gloom \\(expression\\),'

def writeToFile(strFolderPath='./'):
    #提示詞
    strPromptsFilePath = os.path.join(strFolderPath, 'line_prompts_file.txt')
    with open(strPromptsFilePath, 'w') as f:
        for strEmoji in strEmojiList:
            for strHairColor in strHairColorList:
                strPromptsLine = strPromptsStart +\
                '(' + strEmoji + '),(' + strHairColor + '),' +\
                strPrompts + strPnNEnd +\
                strNegativesStart +\
                strNegatives + strPnNEnd
                f.write(strPromptsLine + '\n')
                print(strPromptsLine)

def main():
    writeToFile()

if __name__ == '__main__':
    main()

