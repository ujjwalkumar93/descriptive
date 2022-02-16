// Copyright (c) 2022, k2s.co and contributors
// For license information, please see license.txt

frappe.ui.form.on('Industries', {
	before_save: function(frm) {
		frm.doc.route = frm.doc.industry_name.toLowerCase().trim().replace(/\s/g,"-");
		
	}
});
