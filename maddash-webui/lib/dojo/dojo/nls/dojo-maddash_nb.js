require({cache:{
'dijit/form/nls/nb/validate':function(){
define(
"dijit/form/nls/nb/validate", //begin v1.x content
({
	invalidMessage: "Den angitte verdien er ikke gyldig.",
	missingMessage: "Denne verdien er obligatorisk.",
	rangeMessage: "Denne verdien er utenfor gyldig område."
})
//end v1.x content
);

},
'dijit/nls/nb/loading':function(){
define(
"dijit/nls/nb/loading", //begin v1.x content
({
	loadingState: "Laster inn...",
	errorState: "Det oppsto en feil"
})
//end v1.x content
);

},
'dojo/cldr/nls/nb/number':function(){
define(
"dojo/cldr/nls/nb/number", //begin v1.x content
{
	"group": " ",
	"percentSign": "%",
	"exponential": "E",
	"scientificFormat": "#E0",
	"percentFormat": "#,##0 %",
	"list": ";",
	"infinity": "∞",
	"patternDigit": "#",
	"minusSign": "-",
	"decimal": ",",
	"nan": "NaN",
	"nativeZeroDigit": "0",
	"perMille": "‰",
	"decimalFormat": "#,##0.###",
	"currencyFormat": "¤ #,##0.00",
	"plusSign": "+"
}
//end v1.x content
);
},
'dijit/form/nls/nb/ComboBox':function(){
define(
"dijit/form/nls/nb/ComboBox", //begin v1.x content
({
		previousMessage: "Tidligere valg",
		nextMessage: "Flere valg"
})
//end v1.x content
);

},
'dijit/nls/nb/common':function(){
define(
"dijit/nls/nb/common", //begin v1.x content
({
	buttonOk: "OK",
	buttonCancel: "Avbryt",
	buttonSave: "Lagre",
	itemClose: "Lukk"
})
//end v1.x content
);

}}});
define("dojo/nls/dojo-maddash_nb", [], 1);
