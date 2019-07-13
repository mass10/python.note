#!/usr/bin/env python3
# coding: utf-8

import PIL.Image
import pyocr
import pyocr.builders

def detect_tool():

	print("[TRACE] 使用可能なソフトウェアを調べています...")
	tools = pyocr.get_available_tools()
	if len(tools) == 0:
		print("[ERROR] OCR ライブラリがみつかりませんでした。パッケージ tesseract-ocr libtesseract-dev をインストールしてください。")
		return None

	tool = tools[0]
	print("[TRACE] DETECTED: [", tool.get_name(), "]", sep="")

	print("[TRACE] 使用可能な言語を調べています...")
	langs = tool.get_available_languages()
	if not "jpn" in langs:
		print("[TRACE] jpn がみつかりませんでした。言語パッケージ tesseract-ocr-jpn をインストールしてください。")
		return None
	print("[TRACE] DETECTED: [jpn]")

	return tool

def scan_image(path):

	tool = detect_tool()

	txt = tool.image_to_string(
		PIL.Image.open(path),
		lang="jpn")

	# txt = tool.image_to_string(
	# 	PIL.Image.open(path),
	# 	lang="jpn",
	# 	builder=pyocr.builders.TextBuilder(tesseract_layout=1))

	print("[TRACE] DETECTED: [", txt, "]", sep="")

def main():

	print("[TRACE] ### BEGIN ###")

	scan_image("images/honshibori-lemon.png")

	print("[TRACE] --- END ---")

main()
