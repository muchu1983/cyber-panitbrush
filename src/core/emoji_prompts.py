#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" """
import os
strHairColorList = ['red hair', 'green hair', 'blue hair',]
strEmojiList = ['happy', 'sad', 'scared', 'angry', 'cosy', 'depressing', 'disgusting', 'embarrasing', 'energetic',
    'evil', 'fearful', 'frightening', 'grim', 'guilty', 'hopeful', 'hopeless', 'lonely', 'lustful', 'peaceful',
    'proud', 'relieving', 'romantic', 'resist', 'smile', 'sigh', 'cry', 'cry hard', 'move', 'laughing out loud',
    'naughty', 'wink', 'scold', 'glutton', 'blush', 'smile', 'open mouth', 'red eyes', 'closed eyes', ':d',
    'parted lips', 'one eye closed', 'teeth', 'tongue', 'fang', 'tears', 'tongue out', 'grin', ':o', 'v-shaped eyebrows',
    'symbol-shaped pupils', 'saliva', 'facial hair', 'embarrassed', 'fangs', 'mouth hold', 'heart-shaped pupils',
    'wavy mouth', 'half-closed eyes', 'trembling', ';d', 'crying', '> <', 'slit pupils', 'clenched teeth', 'drooling',
    'covering', 'glowing eyes', 'anger vein', ':p', 'tareme', 'heavy breathing', 'skin fang', 'tearing up', 'naughty face',
    ':q', 'crying with eyes open', 'o o', '+ +', 'serious', 'smirk', '@ @', 'full-face blush', 'pout', 'raised eyebrows',
    'covering mouth', 'licking lips', 'wince', 'ahegao', 'food on face', 'saliva trail', 'bags under eyes',
    'star-shaped pupils', 'nosebleed', 'annoyed', ':/', 'sleepy', 'nervous', 'ear blush', 'covering face', 'moaning',
    'solid circle eyes', 'glaring', 'crazy eyes', 'streaming tears', 'half-closed eye', 'heart in eye', 'mouth drool',
    'screaming', 'smelling', 'happy tears', 'cheek bulge', 'spit take', 'upturned eyes', 'sad smile']
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
    turn pale, gloomy, '

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

