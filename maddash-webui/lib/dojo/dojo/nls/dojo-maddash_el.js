require({cache:{
'dijit/form/nls/el/validate':function(){
define(
"dijit/form/nls/el/validate", //begin v1.x content
({
	invalidMessage: "Η τιμή που καταχωρήσατε δεν είναι έγκυρη.",
	missingMessage: "Η τιμή αυτή πρέπει απαραίτητα να καθοριστεί.",
	rangeMessage: "Η τιμή αυτή δεν ανήκει στο εύρος έγκυρων τιμών."
})
//end v1.x content
);

},
'dijit/nls/el/loading':function(){
define(
"dijit/nls/el/loading", //begin v1.x content
({
	loadingState: "Φόρτωση...",
	errorState: "Σας ζητούμε συγνώμη, παρουσιάστηκε σφάλμα"
})
//end v1.x content
);

},
'dojo/cldr/nls/el/number':function(){
define(
"dojo/cldr/nls/el/number", //begin v1.x content
{
	"group": ".",
	"percentSign": "%",
	"exponential": "e",
	"percentFormat": "#,##0%",
	"list": ",",
	"infinity": "∞",
	"patternDigit": "#",
	"minusSign": "-",
	"decimal": ",",
	"nan": "NaN",
	"nativeZeroDigit": "0",
	"perMille": "‰",
	"currencyFormat": "#,##0.00 ¤",
	"plusSign": "+"
}
//end v1.x content
);
},
'dijit/form/nls/el/ComboBox':function(){
define(
"dijit/form/nls/el/ComboBox", //begin v1.x content
({
		previousMessage: "Προηγούμενες επιλογές",
		nextMessage: "Περισσότερες επιλογές"
})
//end v1.x content
);

},
'dijit/nls/el/common':function(){
define(
"dijit/nls/el/common", //begin v1.x content
({
	buttonOk: "ΟΚ",
	buttonCancel: "Ακύρωση",
	buttonSave: "Αποθήκευση",
	itemClose: "Κλείσιμο"
})
//end v1.x content
);

}}});
define("dojo/nls/dojo-maddash_el", [], 1);
