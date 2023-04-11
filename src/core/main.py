#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""" """

import os
import shutil
import cv2
from src.core import emoji_prompts

ORIGIN_FILE = "./inputs/origin.mp4"
INPUTS_PREFIX = "./inputs/"
OUTPUTS_PREFIX = "./outputs/"
if not os.path.exists(INPUTS_PREFIX):
    os.makedirs(INPUTS_PREFIX)
if not os.path.exists(OUTPUTS_PREFIX):
    os.makedirs(OUTPUTS_PREFIX)
FPS = 30

def start():
    """ start """
    print("started")
    print("./inputs/origin.mp4 > ./outputs/*.png :input '1'")
    print("./outputs/*.png > ./inputs/*.png      :input '2'")
    print("./inputs/*.png > ./outputs/target.mp4 :input '3'")
    print("emoji prompts_file.txt > ./outputs/   :input '4'")
    user_input = input("[1|2|3]?:")
    print("your input is: " + user_input)
    match user_input:
        case "1":
            #step 1
            mp4_to_pngs()
        case "2":
            #step 2
            mv_pngs()
        case "3":
            #step 3
            pngs_to_mp4()
        case "4":
            #emoji prompts_file.txt
            emoji_prompts.writeToFile(strFolderPath=OUTPUTS_PREFIX)
        case _:
            print("wrong answer.stoped.")

def mp4_to_pngs():
    """ mp4 to pngs """
    print("./inputs/origin.mp4 >>>>>>> ./outputs/*.png")
    # 讀取影片
    cap = cv2.VideoCapture(ORIGIN_FILE)
    # 取得總共的影格數
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # 設定影片的 FPS，用來計算每個影格的時間間隔
    cap.set(cv2.CAP_PROP_FPS, FPS)

    # 逐個讀取影格
    for i in range(frame_count):
        # 讀取一個影格
        ret, frame = cap.read()
        # 若讀取成功，則儲存成 PNG 檔
        if ret:
            # 計算輸出檔案名稱
            output_file = f"{OUTPUTS_PREFIX}{i:06d}.png"
            # 儲存影格為 PNG 檔
            cv2.imwrite(output_file, frame)

    # 關閉影片檔案
    cap.release()


def pngs_to_mp4():
    """ pngs to mp4 """
    print("./inputs/*.png >>>>>>> ./outputs/target.mp4")
    # 將多個 png 圖像合成一個 mp4 影片
    output_video_path = f"{OUTPUTS_PREFIX}target.mp4"

    img0 = cv2.imread(INPUTS_PREFIX + os.listdir(INPUTS_PREFIX)[0])
    size = (img0.shape[1], img0.shape[0])
    
    video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), FPS, size)

    images = [img for img in os.listdir(INPUTS_PREFIX) if img.endswith(".png")]
    images.sort()
    for image in images:
        image_path = os.path.join(INPUTS_PREFIX, image)
        img = cv2.imread(image_path)
        video_writer.write(img)

    # 釋放 VideoWriter 資源
    video_writer.release()

def mv_pngs():
    """ move pngs"""
    source_dir = OUTPUTS_PREFIX
    destination_dir = INPUTS_PREFIX
    for filename in os.listdir(source_dir):
        if filename.endswith(".png"):
            shutil.copy(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

