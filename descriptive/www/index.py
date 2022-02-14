import frappe

def get_context(contex):
    contex.data = frappe.get_all("Insights",['*'])