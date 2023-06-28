import frappe

EMAIL_STATUS_UPDATE_EVENTS = [
	"sent",
	"delivered",
	"delivery_delayed",
	"complained",
	"bounced",
	"opened",
]

@frappe.whitelist(allow_guest=True)
def handle_resend_webhook():
	data = frappe.form_dict
	# verify_signing_secret()
	entity, event = data.type.split(".")
	
	if entity == "email" and event in EMAIL_STATUS_UPDATE_EVENTS:
		resend_id = data.data.get("email_id")
		email_delivery_status = " ".join(part.title() for part in event.split("_"))
		
		# update the status of the Resend Email Record
		frappe.db.set_value(
			"Resend Email Record", 
			{"resend_id": resend_id}, 
			"status", email_delivery_status
		)
	
	return email_delivery_status

@frappe.whitelist()
def send_email(subject, from_email=None, to_emails=[], email_html="", reply_to=""):
	# if to_emails is a string, convert it to a list by splitting at ","
	if isinstance(to_emails, str):
		to_emails = to_emails.split(",")
	
	for to_email in to_emails:
		# create a new Resend Email Record for each email sent
		resend_email_record = frappe.new_doc("Resend Email Record")
		resend_email_record.from_email = from_email
		resend_email_record.to_emails = to_email
		resend_email_record.subject = subject
		resend_email_record.email_html = email_html
		resend_email_record.reply_to = reply_to
		resend_email_record.save()
		resend_email_record.submit()

	return True



def verify_signing_secret():
	from frappe.utils.password import get_decrypted_password
	signing_secret = get_decrypted_password("Resend Settings", "Resend Settings", "signing_secret")

	if frappe.request.headers["Svix-Signature"] != signing_secret:
		frappe.throw("Invalid signing secret.")






	