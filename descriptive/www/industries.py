import frappe
def get_context(contex):
    all_industies = []
    for p,i in enumerate(frappe.get_all("Industries",['*'])):
        i['id'] = p+1
        all_industies.append(i)
    contex.data = all_industies
    
