// ----------------------------------------------------- FUNCTIONS -----------------------------------------------------
function insertAbstractToggle(abs, absnumstr) {
		var absstr = 'abstract' + absnumstr;
		var txt = "<div id=\"hide_part" + absnumstr + "\" style=\"display:none;\"> \n"
				+ "<p class=\"sem_abstract\" style=\"text-align: justify;text-justify: inter-word;\"><strong>Abstract</strong><br> \n"
				+ abs + " \n"
				+ "</p> \n"
				+ "<a href=\"javascript:;\" onClick=\"document.getElementById('show_part" + absnumstr + "').style.display='block';"
				+ "document.getElementById('hide_part" + absnumstr + "').style.display='none';\">&#8657; </a> \n"
				+ "</div> \n"
				+ "<div id=\"show_part" + absnumstr + "\" style=\"display:block;\"> \n"
				+ "<a href=\"javascript:;\" onClick=\"document.getElementById('show_part" + absnumstr + "').style.display='none';"
				+ " document.getElementById('hide_part" + absnumstr + "').style.display='block';\">Abstract &#8659;</a> \n"
				+ "</div> \n";
		
		return txt;
}
