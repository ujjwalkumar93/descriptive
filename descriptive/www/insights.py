import frappe
def get_context(contex):
    data = frappe.get_all("Insights",{"enable":1},['*'],order_by = "sort_order")
    contex.insights_list = data