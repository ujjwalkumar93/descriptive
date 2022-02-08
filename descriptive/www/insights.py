import frappe
def get_context(context):
    data = frappe.get_all("Insights",{"enable":1},['*'],order_by = "sort_order")
    context.insights_list = data