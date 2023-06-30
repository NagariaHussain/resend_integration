frappe.listview_settings['Resend Email Record'] = {
    get_indicator: (doc) => {
        const status_colors = {
            "Delivered": "green",
            "Sent": "blue",
            "Delivery Delayed": "pink",
            "Bounced": "red",
            "Complained": "orange",
            "Opened": "cyan",
        };
        return [doc.status || "Draft", status_colors[doc.status] || "gray", "status,=," + doc.status];
    }
}