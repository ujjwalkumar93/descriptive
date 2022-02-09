import frappe

def get_context(contex):
    query_params = frappe.form_dict.name
    #frappe.throw(frappe.form_dict.name)
    # query_params = frappe.request.environ.get('QUERY_STRING')
    contex.data = frappe.get_doc("Insights",{"insight_name": query_params})