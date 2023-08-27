# Copyright (c) 2023, Hussain Nagaria and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ResendEmailTemplate(Document):
	@frappe.whitelist()
	def get_rendered_html(self, context):
		# regex to replace "##x##" with "{{ x }}" to make it compatible with jinja2
		import re
		regex = r"##(\w+)##"
		template = re.sub(regex, r"{{ \1 }}", self.template)
		return frappe.render_template(template, context)
	

		

