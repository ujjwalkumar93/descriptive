import frappe
from frappe.utils import cint
@frappe.whitelist(allow_guest = True)
def handle_form(name=None,email=None,phone=None,reason=None,msg=None):
    if reason == "business-use":
        if name:
            lead_doc=frappe.new_doc('Lead')
            lead_doc.update(
                {
                    "doctype" : 'Lead',
                    "lead_name" : name,
                    "email_id" : email,
                    "mobile_no" : phone,
                    "remark" : msg,
                })
        lead_doc.insert(ignore_permissions = True)
        frappe.db.commit()
    if reason == "career-use":
        if name:
            doc=frappe.new_doc('Job Applicant')
            doc.update(
                {
                    "applicant_name" : name,
                    "email_id" : email,
                    "phone_no" : phone,
                    "remark" : msg,
                })
        doc.insert(ignore_permissions = True)
        frappe.db.commit()
    return True


# @frappe.whitelist()
# def upload_file():
#     ALLOWED_MIMETYPES = ('image/png', 'image/jpeg', 'application/pdf', 'application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document','application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','application/vnd.oasis.opendocument.text', 'application/vnd.oasis.opendocument.spreadsheet')
#     user = None
#     if frappe.session.user == 'Guest':
#         if frappe.get_system_settings('allow_guests_to_upload_files'):
#             ignore_permissions = True
#         else:
#             return
#     else:
#         user = frappe.get_doc("User", frappe.session.user)
#         ignore_permissions = False

#     files = frappe.request.files
#     is_private = frappe.form_dict.is_private
#     doctype = frappe.form_dict.doctype
#     docname = frappe.form_dict.docname
#     fieldname = frappe.form_dict.fieldname
#     file_url = frappe.form_dict.file_url
#     folder = frappe.form_dict.folder or 'Home'
#     method = frappe.form_dict.method
#     content = None
#     filename = None

#     if 'file' in files:
#         file = files['file']
#         content = file.stream.read()
#         filename = file.filename

#     frappe.local.uploaded_file = content
#     frappe.local.uploaded_filename = filename

#     if frappe.session.user == 'Guest' or (user and not user.has_desk_access()):
#         import mimetypes
#         filetype = mimetypes.guess_type(filename)[0]
#         if filetype not in ALLOWED_MIMETYPES:
#             frappe.throw(_("You can only upload JPG, PNG, PDF, or Microsoft documents."))

#     # if method:
#     # 	method = frappe.get_attr(method)
#     # 	is_whitelisted(method)
#     # 	return method()
#     else:
#         ret = frappe.get_doc({
#             "doctype": "File",
#             "attached_to_doctype": doctype,
#             "attached_to_name": docname,
#             "attached_to_field": fieldname,
#             "folder": folder,
#             "file_name": filename,
#             "file_url": file_url,
#             "is_private": cint(is_private),
#             "content": content
#         })
#         ret.save(ignore_permissions=ignore_permissions)
#         return ret