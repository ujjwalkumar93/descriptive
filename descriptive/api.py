import frappe

@frappe.whitelist(allow_guest = True)
def handle_form(name="uk"):
    print("##############!!!!!!!!"*200)
    print(name)
    return True