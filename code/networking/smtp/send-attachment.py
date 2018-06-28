#!/usr/bin/env python3
# coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase

def _read_text_file(path):

	with open(path, "rb") as f:
		return f.read()

def _send(subject, mail_from, rcpt_to, body, filename):

	root_message = MIMEMultipart()
	root_message["Subject"] = smtplib.email.Header.Header(subject, "utf-8")
	root_message["From"] = mail_from
	root_message["To"] = rcpt_to
	root_message["Date"] = formatdate()

	# 本文
	message = MIMEText(body)
	message.add_header("Content-Type", "text/plain; charset=UTF-8")
	root_message.attach(message)

	# 添付ファイル
	attachment = MIMEBase("text", "")
	attachment_body = _read_text_file(filename)
	attachment.set_payload(attachment_body)
	encoders.encode_base64(attachment)
	attachment.add_header("Content-Disposition", "attachment", filename=filename)
	root_message.attach(attachment)

	s = smtplib.SMTP("127.0.0.1:25")
	composed = root_message.as_string()
	s.sendmail(mail_from, [rcpt_to], composed)

	s.close()

def _main():

	subject = "[test][ec2] 日本語 UTF-8, 8bit のテストです。"
	mail_from = "ec2-user"
	rcpt_to = "jimi.hendrix@gmail.com"
	body = """こんにちは。
テスト
テスト
テスト
テスト
テスト
テスト
テスト
テスト
テスト
テスト

"""
	filename = "send-attachment.py"
	_send(subject, mail_from, rcpt_to, body, filename)

_main()
