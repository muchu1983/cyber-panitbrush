#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""" """
import cv2
import os
import shutil
import src.core.emoji_prompts as emoji_prompts

origin_file = "./inputs/origin.mp4"
inputs_prefix = "./inputs/"
outputs_prefix = "./outputs/"
if not os.path.exists(inputs_prefix):
	os.makedirs(inputs_prefix)
if not os.path.exists(outputs_prefix):
	os.makedirs(outputs_prefix)
fps = 30

def start():
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
			mp4ToPngs()
		case "2":
			#step 2
			mvPngs()
		case "3":
			#step 3
			pngsToMp4()
		case "4":
			#emoji prompts_file.txt
			emoji_prompts.writeToFile(strFolderPath=outputs_prefix)
		case _:
			print("wrong answer.stoped.")

def mp4ToPngs():
	print("./inputs/origin.mp4 >>>>>>> ./outputs/*.png")
	# 讀取影片
	cap = cv2.VideoCapture(origin_file)
	# 取得影片的寬高
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	# 取得總共的影格數
	frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	# 設定影片的 FPS，用來計算每個影格的時間間隔
	cap.set(cv2.CAP_PROP_FPS, fps)

	# 逐個讀取影格
	for i in range(frame_count):
		# 讀取一個影格
		ret, frame = cap.read()
		# 若讀取成功，則儲存成 PNG 檔
		if ret:
			# 計算輸出檔案名稱
			output_file = f"{outputs_prefix}{i:06d}.png"
			# 儲存影格為 PNG 檔
			cv2.imwrite(output_file, frame)

	# 關閉影片檔案
	cap.release()


def pngsToMp4():
	print("./inputs/*.png >>>>>>> ./outputs/target.mp4")
	# 將多個 png 圖像合成一個 mp4 影片
	output_video_path = f"{outputs_prefix}target.mp4"

	img0 = cv2.imread(inputs_prefix + os.listdir(inputs_prefix)[0])
	size = (img0.shape[1], img0.shape[0])
	
	video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, size)

	images = [img for img in os.listdir(inputs_prefix) if img.endswith(".png")]
	images.sort()
	for image in images:
		image_path = os.path.join(inputs_prefix, image)
		img = cv2.imread(image_path)
		video_writer.write(img)

	# 釋放 VideoWriter 資源
	video_writer.release()

def mvPngs():
	source_dir = outputs_prefix
	destination_dir = inputs_prefix
	for filename in os.listdir(source_dir):
		if filename.endswith(".png"):
			shutil.copy(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

