import frappe
def get_context(contex):
    contex.data = frappe.get_all("Industries",{"enable":1},['*'],order_by = "sort_order")
    #contex.insights_list = data