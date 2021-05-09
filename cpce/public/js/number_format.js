


if (!window.frappe) window.frappe = {};

function format_currency_format(v, currency, decimals, format) {
	var format = format;
	var symbol = get_currency_symbol(currency);
	if(decimals === undefined) {
		decimals = frappe.boot.sysdefaults.currency_precision || null;
	}

	if (symbol)
		return symbol + " " + format_number(v, format, decimals);
	else
		return format_number(v, format, decimals);
}

Object.assign(window, {
	format_currency_format
});




