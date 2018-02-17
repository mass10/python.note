#!/usr/bin/env python3
# coding: utf-8

import pptx

def main():

	p = pptx.Presentation()

	title_slide_layout = p.slide_layouts[0]
	slide = p.slides.add_slide(title_slide_layout)
	title = slide.shapes.title
	subtitle = slide.placeholders[1]

	title.text = "Hello, World!"
	subtitle.text = "python-pptx was here!"

	p.save('hello.pptx')

main()
