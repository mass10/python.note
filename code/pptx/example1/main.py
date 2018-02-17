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
		title = slide.shapes.title
		title.text = "〇△□ 月次報告"
		subtitle = slide.placeholders[1]
		subtitle.text = "2018年 2月 14日\npowered by python-pptx"

	### Bullet Slide ###
	if True:
		new_slide = presentation.slide_layouts[1]
		slide = presentation.slides.add_slide(new_slide)
		shapes = slide.shapes
		# タイトル部分
		shapes.title.text = "Bullet Slide です"
		# 下の部分
		body_shape = shapes.placeholders[1]
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "あいうえお"
		pa = body_shape.text_frame.add_paragraph()
		pa.text = "かきくけこ"

	### Blank Slide
	if True:
		new_slide = presentation.slide_layouts[6]
		slide = presentation.slides.add_slide(new_slide)
		left = top = width = height = pptx.util.Inches(1)
		textbox = slide.shapes.add_textbox(
			pptx.util.Inches(0.8),
			pptx.util.Inches(0.8),
			pptx.util.Inches(3),
			pptx.util.Inches(1))
		text_frame = textbox.text_frame
		text_frame.word_wrap = True
		# 段落を追加
		p = text_frame.add_paragraph()
		run = p.add_run()
		run.text = "Ansh ash a skjwidhnqm xnajhwslzm widh aslk al Najhsbleei. Le a Kan Najweee ka. Has ashqie nclk aiqw djfseok naxbad jqhdu asfifjnzxs kasjles jas wee le ag das."
		run.font.color.rgb = pptx.dml.color.RGBColor(0x50, 0x80, 0x90)

	presentation.save('hello.pptx')

main()
