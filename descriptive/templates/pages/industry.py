import frappe

def get_context(contex):
    query_params = frappe.form_dict.name
    contex.data = frappe.get_doc("Industries",{"industry_name" : query_params})