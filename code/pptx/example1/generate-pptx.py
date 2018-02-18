#!/usr/bin/env python3
# coding: utf-8

import os
import json
import pptx
import pptx.chart.data

def load_json_as_python_object(path):
	
	with open(path) as file:
		return json.load(file)

def load_chart_data():
	
	unknown = load_json_as_python_object("data/data.json")

	labels = []
	series_01 = []
	series_02 = []
	
	for e in unknown:
		labels.append(e["label"])
		series_01.append(e["2016"])
		series_02.append(e["2017"])

	return labels, series_01, series_02

def main():

	### loading chart data ###
	series_labels_01, series_01, series_02 = load_chart_data()

	### Presentation ###
	presentation = pptx.Presentation()

	### Title Slide ###
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[0]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル
		title = shapes.title
		title.text = "もうこわくない！\nパワポ！パワポ！\nパ・ワ・ポ！"
		# サブタイトル
		subtitle = slide.placeholders[1]
		subtitle.text = "2018年2月14日\n社内勉強会"

	### セクション 見出し
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[6]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# textbox を挿入
		left, top = pptx.util.Inches(0.8), pptx.util.Inches(2.8)
		cx, cy = pptx.util.Inches(8.0), pptx.util.Inches(1.0)
		textbox = shapes.add_textbox(left, top, cx, cy)
		text_frame = textbox.text_frame
		text_frame.word_wrap = False
		p = text_frame.add_paragraph()
		run = p.add_run()
		run.text = "こんなことありませんか..."
		run.font.color.rgb = pptx.dml.color.RGBColor(0x60, 0x60, 0x60)
		run.font.size = pptx.util.Pt(55)

	### Bullet Slide ###
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[1]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "こんなことありませんか..."
		# 下の部分
		body_shape = shapes.placeholders[1]
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "上司がパワポが好き"

	### Bullet Slide ###
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[1]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "こんなことありませんか..."
		# 下の部分
		body_shape = shapes.placeholders[1]
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "上司がパワポが好き"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "あなたがパワポが好き"

	### Bullet Slide ###
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[1]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "こんなことありませんか..."
		# 下の部分
		body_shape = shapes.placeholders[1]
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "上司がパワポが好き"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "あなたがパワポが好き"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "パワポを作る定期作業がある"

	### Bullet Slide ###
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[1]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "こんなことありませんか..."
		# 下の部分
		body_shape = shapes.placeholders[1]
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "上司がパワポが好き"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "あなたがパワポが好き"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "パワポを作る定期作業がある"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "毎回数字をちょっと書き換えて提出している"

	### Bullet Slide ###
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[1]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "こんなことありませんか..."
		# 下の部分
		body_shape = shapes.placeholders[1]
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "上司がパワポが好き"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "あなたがパワポが好き"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "パワポを作る定期作業がある"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "毎回数字をちょっと書き換えて提出している"
		# textbox を挿入
		left, top = pptx.util.Inches(6.2), pptx.util.Inches(4.7)
		cx, cy = pptx.util.Inches(2.0), pptx.util.Inches(2.0)
		textbox = slide.shapes.add_textbox(left, top, cx, cy)
		text_frame = textbox.text_frame
		p = text_frame.add_paragraph()
		run = p.add_run()
		run.text = "(-\"-)"
		# run.font.color.rgb = pptx.dml.color.RGBColor(0x50, 0x80, 0x90)
		run.font.size = pptx.util.Pt(100)

	### セクション 見出し
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[6]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# textbox を挿入
		left, top, cx, cy = pptx.util.Inches(1.0), pptx.util.Inches(2.5), pptx.util.Inches(8.0), pptx.util.Inches(1.0)
		textbox = shapes.add_textbox(left, top, cx, cy)
		text_frame = textbox.text_frame
		text_frame.word_wrap = True
		p = text_frame.add_paragraph()
		run = p.add_run()
		run.text = "それでは"
		run.font.color.rgb = pptx.dml.color.RGBColor(0x60, 0x60, 0x60)
		run.font.size = pptx.util.Pt(64)

	### セクション 見出し
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[6]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# textbox を挿入
		left, top, cx, cy = pptx.util.Inches(2.3), pptx.util.Inches(2.5), pptx.util.Inches(8.0), pptx.util.Inches(1.0)
		textbox = shapes.add_textbox(left, top, cx, cy)
		text_frame = textbox.text_frame
		text_frame.word_wrap = True
		p = text_frame.add_paragraph()
		run = p.add_run()
		run.text = "python-pptx"
		run.font.size = pptx.util.Pt(74)

	### Bullet Slide ###
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[1]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "What is python-pptx?"
		# 下の部分
		body_shape = shapes.placeholders[1]
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "Microsoft PowerPoint のスライドを Python アプリケーション内から作成するためのライブラリです。"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "pip で簡単インストール"

	### セクション 見出し
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[1]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "インストール"
		# textbox を挿入
		left, top, cx, cy = pptx.util.Inches(0.9), pptx.util.Inches(2.5), pptx.util.Inches(8.0), pptx.util.Inches(1.0)
		textbox = slide.shapes.add_textbox(left, top, cx, cy)
		text_frame = textbox.text_frame
		text_frame.word_wrap = True
		p = text_frame.add_paragraph()
		run = p.add_run()
		run.text = "pip install python-pptx"
		run.font.size = pptx.util.Pt(40)

	### Blank Slide
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[5]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル
		shapes.title.text = "サンプル: ハイパーリンク"
		# textbox を挿入
		left, top = pptx.util.Inches(0.8), pptx.util.Inches(1.6)
		cx, cy = pptx.util.Inches(9.0), pptx.util.Inches(5)
		textbox = shapes.add_textbox(left, top, cx, cy)
		text_frame = textbox.text_frame
		text_frame.word_wrap = True
		p = text_frame.add_paragraph()
		# link
		run = p.add_run()
		run.text = "https://github.com/scanny/python-pptx"
		run.hyperlink.address = "https://github.com/scanny/python-pptx"
		#
		run = p.add_run()
		run.text = "\n"
		# link
		run = p.add_run()
		run.text = "https://github.com/mass10/python.note/tree/master/code/pptx/example1"
		run.hyperlink.address = "https://github.com/mass10/python.note/tree/master/code/pptx/example1"
		#
		run = p.add_run()
		run.text = "\n"
		# link
		run = p.add_run()
		run.text = "http://www.metro.tokyo.jp"
		run.hyperlink.address = "http://www.metro.tokyo.jp"

	### Title Only Slide ###
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[5]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル
		shapes.title.text = "サンプル:タイトルのみ"

	### 画像を挿入する
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[5]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		shapes.title.text = "サンプル: 画像を挿入する"
		# textbox を挿入
		if True:
			left, top, cx, cy = pptx.util.Inches(0.8), pptx.util.Inches(1.1), pptx.util.Inches(8.4), pptx.util.Inches(1)
			textbox = shapes.add_textbox(left, top, cx, cy)
			text_frame = textbox.text_frame
			text_frame.word_wrap = True
			# 段落を追加
			p = text_frame.add_paragraph()
			run = p.add_run()
			run.text = "Python コードから .pptx を生成することができます。無地、タイトルのみ、タイトルとボディあり、など、いくつかのテンプレートがあります。また、企業ロゴなどを埋め込みたい場合にはテンプレート読み出しも可能です。"
			run.font.color.rgb = pptx.dml.color.RGBColor(0x50, 0x80, 0x90)
		# 画像を挿入
		if True:
			left, top = pptx.util.Inches(1), pptx.util.Inches(2.7)
			picture_box = slide.shapes.add_picture("images/image-01.png", left, top)

	### 表 ###
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[1]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル
		shapes.title.text = "サンプル:表"
		# 表を挿入
		if True:
			rows = 2
			cols = 3
			left, top = pptx.util.Inches(2.0), pptx.util.Inches(2.0)
			width, height = pptx.util.Inches(6.0), pptx.util.Inches(0.6)
			table = shapes.add_table(rows, cols, left, top, width, height).table
			# table.columns[0].width = pptx.util.Inches(2.0)
			# table.columns[1].width = pptx.util.Inches(4.0)
			# table.columns[2].width = pptx.util.Inches(4.0)
			table.cell(0, 0).text = 'ラーメン'
			table.cell(0, 1).text = 'カレーライス'
			table.cell(0, 2).text = 'うどん'
			table.cell(1, 0).text = '2,300 kcal'
			table.cell(1, 1).text = '1,800 kcal'
			table.cell(1, 2).text = '900 kcal'
		# 箇条書き部分
		if True:
			body = shapes.placeholders[1]
			body.left = pptx.util.Inches(0.9)
			body.top = pptx.util.Inches(5.0)
			body.width = pptx.util.Inches(8.0)
			body.height = pptx.util.Inches(2.0)
			text_frame = body.text_frame
			# text_frame.word_wrap = True
			#
			p = text_frame.add_paragraph()
			r = p.add_run()
			r.text = "ラーメンはハイカロリー！"
			r.font.size = pptx.util.Pt(19)
			#
			p = text_frame.add_paragraph()
			r = p.add_run()
			r.text = "カレーライスだいすき"
			r.font.size = pptx.util.Pt(19)
			#
			p = text_frame.add_paragraph()
			r = p.add_run()
			r.text = "ラーメンに比べてうどんが低いのはスープ？？"
			r.font.size = pptx.util.Pt(19)

	### Bullet Slide ###
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[1]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "サンプル: 年間平均気温(2017年)"
		# チャート
		chart_data = pptx.chart.data.ChartData()
		chart_data.categories = series_labels_01
		chart_data.add_series('2016年', series_01)
		chart_data.add_series('2017年', series_02)
		x, y = pptx.util.Inches(1.0), pptx.util.Inches(2)
		cx, cy = pptx.util.Inches(8), pptx.util.Inches(4.5)
		chart = slide.shapes.add_chart(
			pptx.enum.chart.XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data
		).chart
		chart.has_legend = True

	### セクション 見出し
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[6]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# textbox を挿入
		if True:
			left, top = pptx.util.Inches(1.0), pptx.util.Inches(2.5)
			cx, cy = pptx.util.Inches(8.0), pptx.util.Inches(1.0)
			textbox = shapes.add_textbox(left, top, cx, cy)
			text_frame = textbox.text_frame
			text_frame.word_wrap = True
			p = text_frame.add_paragraph()
			run = p.add_run()
			run.text = "まとめ"
			run.font.color.rgb = pptx.dml.color.RGBColor(0x60, 0x60, 0x60)
			run.font.size = pptx.util.Pt(64)

	### セクション 見出し
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[1]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "まとめ"
		# 下の部分
		body_shape = shapes.placeholders[1]
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "定型作業は自動化"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "人は必ず間違える"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "目視確認を排除"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "作業ではなく本質的なことに時間を"

	### セクション 見出し
	if True:

		# スライドを生成
		new_slide = presentation.slide_layouts[6]
		# 挿入
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# textbox を挿入
		left, top = pptx.util.Inches(1.0), pptx.util.Inches(2.5)
		cx, cy = pptx.util.Inches(8.0), pptx.util.Inches(1.0)
		textbox = shapes.add_textbox(left, top, cx, cy)
		text_frame = textbox.text_frame
		text_frame.word_wrap = True
		p = text_frame.add_paragraph()
		run = p.add_run()
		run.text = "おわり"
		run.font.color.rgb = pptx.dml.color.RGBColor(0x60, 0x60, 0x60)
		run.font.size = pptx.util.Pt(64)

	### 書き出し
	presentation.save('example1.pptx')

main()
