// Copyright (c) 2022, k2s.co and contributors
// For license information, please see license.txt

frappe.ui.form.on('Insights', {
	before_save: function(frm) {
		if(frm.doc.dissable_auto_route === 0){
			frm.doc.route = frm.doc.insight_name.toLowerCase().trim().replace(/\s/g,"-");
		}		
	}
});
