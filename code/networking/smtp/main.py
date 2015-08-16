#!/usr/bin/env python
# coding: utf-8

import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate


def _main():

	subject = 'this is subjet...'
	mail_from = 'aaa@example.jp'
	rcpt_to = 'bbb@example.jp'
	body = 'hello-------'

	message = MIMEText(body)
	message['Subject'] = subject
	message['From'] = mail_from
	message['To'] = rcpt_to
	message['Date'] = formatdate()

	s = smtplib.SMTP('127.0.0.1:25')
	s.sendmail(mail_from, [rcpt_to], message.as_string())

	s.close()

_main()

