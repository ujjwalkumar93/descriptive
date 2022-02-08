import frappe

def get_context(contex):
    query_params = frappe.form_dict.name
    contex.data = frappe.get_doc("Industries",{"name" : query_params})