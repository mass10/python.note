#!/usr/bin/env python
# coding: utf-8

import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate


def _main():

	subject = "テストです(^。^)y-.。o○"
	mail_from = "ec2-user"
	rcpt_to = "ec2-user"
	body = """hello-------
o
o
o
o
...........
"""

	message = MIMEText(body)
	message['Subject'] = smtplib.email.Header.Header(subject, "utf-8")
	message['From'] = mail_from
	message['To'] = rcpt_to
	message['Date'] = formatdate()
	message.add_header('Content-Type', 'text/plain; charset=UTF-8')

	s = smtplib.SMTP('127.0.0.1:25')
	s.sendmail(mail_from, [rcpt_to], message.as_string())

	s.close()

_main()

