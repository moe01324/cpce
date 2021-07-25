def make_sales_order(doc, handler=""):
    se = frappe.new_doc("Sales Order")
    for se_item in doc.items:
        se.append("items", { "item_code":se_item.item_code, "item_group": se_item.item_group, "item_name":se_item.item_name, "amount":se_item.amount, "qty": se_item.qty , "uom":se_item.uom, "conversion_factor": se_item.conversion_factor }) 
    frappe.msgprint('Sales Order is created.')
    se.insert()