import frappe

def get_context(contex):
    query_params = frappe.form_dict.name
    contex.data = frappe.get_doc("Industries",{"route" : query_params})
    contex.all_industies = frappe.get_all("Industries",['*'])