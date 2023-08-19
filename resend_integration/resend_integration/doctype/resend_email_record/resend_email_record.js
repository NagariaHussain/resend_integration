// Copyright (c) 2023, Hussain Nagaria and contributors
// For license information, please see license.txt

frappe.ui.form.on("Resend Email Record", {
  refresh(frm) {
    let email_html = cur_frm.doc.email_html;
    if (email_html) {
      const label_html = `<label class="control-label mb-1" style="padding-right: 0px;">HTML Preview</label>`;
      email_html = label_html + email_html;
      cur_frm.get_field("html_preview").$wrapper.html(email_html);
    }
  },
});
