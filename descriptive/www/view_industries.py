import frappe

def get_context(contex):
    query_params = frappe.request.environ.get('QUERY_STRING')
    contex.data = frappe.get_doc("Industries",query_params)