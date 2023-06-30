# Copyright (c) 2023, Hussain Nagaria and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from resend_integration.api import send_resend_emails


class ResendBroadcastEmail(Document):
	@frappe.whitelist()
	def send_emails(self):
		send_resend_emails(
			self.subject,
			from_email=self.from_email,
			to_emails=self.recipients,
			email_html=self.email_html,
			reply_to=self.reply_to,
			broadcast=self.name
		)
		self.status = "Sent"
		self.save()
