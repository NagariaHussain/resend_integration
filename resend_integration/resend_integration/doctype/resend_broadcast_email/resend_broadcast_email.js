// Copyright (c) 2023, Hussain Nagaria and contributors
// For license information, please see license.txt

frappe.ui.form.on("Resend Broadcast Email", {
    refresh(frm) {
        if (frm.doc.status !== "Sent") {
            const send_button = frm.add_custom_button("Send Emails", () => {
                frm.call("send_emails").then(() => {
                    frm.msgprint("Emails sent successfully");
                });
            })
        }
    },
});
