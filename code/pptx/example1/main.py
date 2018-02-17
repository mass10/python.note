#!/usr/bin/env python3
# coding: utf-8

import pptx

def main():

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
