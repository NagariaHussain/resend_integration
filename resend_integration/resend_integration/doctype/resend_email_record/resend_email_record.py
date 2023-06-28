# Copyright (c) 2023, Hussain Nagaria and contributors
# For license information, please see license.txt

import frappe
import resend
from frappe.model.document import Document
from frappe.utils.password import get_decrypted_password

def get_resend_api_key():
	return get_decrypted_password("Resend Settings", "Resend Settings", "api_key")

class ResendEmailRecord(Document):
	def before_submit(self):
		if self.status == "Sent":
			frappe.throw("Email has already been sent.")

		resend.api_key = get_resend_api_key()
		email = resend.Emails.send({
			"from": self.from_email,
			"to": self.to_emails.strip().split(","),
			"subject": self.subject,
			"html": self.email_html
		})

		self.status = "Sent"
		self.resend_id = email["id"]


