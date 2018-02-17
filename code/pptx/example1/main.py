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

		new_slide = presentation.slide_layouts[0]

		slide = presentation.slides.add_slide(new_slide)
		title = slide.shapes.title.text = "もうこわくない！パワポ！パワポ！パ・ワ・ポ！"
		subtitle = slide.placeholders[1]
		subtitle.text = "2018年2月14日\n社内勉強会"

	### Bullet Slide ###
	if True:

		new_slide = presentation.slide_layouts[1]

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

		new_slide = presentation.slide_layouts[1]

		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "こんなことありませんか..."
		# 下の部分
		body_shape = shapes.placeholders[1]
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "上司がパワポが好き"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "毎月パワポで報告作れ"

	### Bullet Slide ###
	if True:

		new_slide = presentation.slide_layouts[1]

		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "年間平均気温(2017年)"
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

	### Bullet Slide ###
	if True:

		new_slide = presentation.slide_layouts[1]

		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "こんなことありませんか..."
		# 下の部分
		body_shape = shapes.placeholders[1]
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "上司がパワポが好き"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "毎月パワポで報告作れ"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "あなたがパワポが好き"

	### Bullet Slide ###
	if True:

		new_slide = presentation.slide_layouts[1]

		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "こんなことありませんか..."
		# 下の部分
		body_shape = shapes.placeholders[1]
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "上司がパワポが好き"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "毎月パワポで報告作れ"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "あなたがパワポが好き"

		textbox = slide.shapes.add_textbox(
			pptx.util.Inches(6.0),
			pptx.util.Inches(4.6),
			pptx.util.Inches(2.0),
			pptx.util.Inches(2.0))
		text_frame = textbox.text_frame
		# 段落を追加
		p = text_frame.add_paragraph()
		run = p.add_run()
		run.text = "(-\"-)"
		# run.font.color.rgb = pptx.dml.color.RGBColor(0x50, 0x80, 0x90)
		run.font.size = pptx.util.Pt(100)

	### Blank Slide
	if True:

		new_slide = presentation.slide_layouts[6]

		slide = presentation.slides.add_slide(new_slide)
		left = top = width = height = pptx.util.Inches(1)
		textbox = slide.shapes.add_textbox(
			pptx.util.Inches(0.8),
			pptx.util.Inches(0.8),
			pptx.util.Inches(8.4),
			pptx.util.Inches(1))
		text_frame = textbox.text_frame
		text_frame.word_wrap = True
		# 段落を追加
		p = text_frame.add_paragraph()
		run = p.add_run()
		run.text = "Ansh ash a skjwidhnqm xnajhwslzm widh aslk al Najhsbleei. Le a Kan Najweee ka. Has ashqie nclk aiqw djfseok naxbad jqhdu asfifjnzxs kasjles jas wee le ag das."
		run.font.color.rgb = pptx.dml.color.RGBColor(0x50, 0x80, 0x90)

		picture_box = slide.shapes.add_picture(
			"images/image-01.png",
			pptx.util.Inches(1),
			pptx.util.Inches(2.4))

	presentation.save('hello.pptx')

main()
