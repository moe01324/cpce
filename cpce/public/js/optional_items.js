// TaxesAndTotalsExtend is just variable name
// erpnext.taxes_and_totals is function contain function you want to override
const TaxesAndTotalsExtend = erpnext.taxes_and_totals.extend({
	// calculate_item_values is function you want to override
	calculate_item_values: () => {
		console.log('Hello from extend taxes and total extend !!');
	},
});

// this tell current form to use this override script
$.extend(
	cur_frm.cscript,
	new TaxesAndTotalsExtend({frm: cur_frm}),
);