# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cpce"
app_title = "Cpce"
app_publisher = "Gregor Mogeritsch"
app_description = "Customizations for CPCE"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "gregor.mogeritsch@gmail.com"
app_license = "MIT"
app_logo_url = "/assets/cpce/images/CP_Logo-web.png"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/cpce/css/cpce.css"

# include js, css files in header of web template
# web_include_css = "/assets/cpce/css/cpce.css"
# web_include_js = "/assets/cpce/js/cpce.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "cpce/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Quotation" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cpce.install.before_install"
# after_install = "cpce.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cpce.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"File": {
		"validate": "cpce.utils.check_file_format"
	},
    'Purchase Order': {
        'on_submit': [
            'erpnext.buying.doctype.purchase_order.purchase_order.make_sales_order_cpce_again'
        ]
    },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cpce.tasks.all"
# 	],
# 	"daily": [
# 		"cpce.tasks.daily"
# 	],
# 	"hourly": [
# 		"cpce.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cpce.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cpce.tasks.monthly"
# 	]
# }


website_context = {
	"favicon": 	"/assets/cpce/images/favicon-32x32.png",
	"splash_image": "/assets/cpce/images/erpnext-logo.png"
}




# Testing
# -------

# before_tests = "cpce.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cpce.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "cpce.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


jenv = {
    "methods": [
        "cpce_number_format:cpce.utils.cpce_number_format"
    ]
}


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

