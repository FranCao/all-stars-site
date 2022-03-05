function isNullOrWhitespace(input){
	return !input || !input.trim();
}

function cleanUp(){
	$("#search_box").val("")
	$("#search_box").focus()
}

function search_players(){
    let search = $("#search_box").val()
    let error = false

    if (isNullOrWhitespace(search)){
		cleanUp()
		error = true
	}

    if (error == false) {
        window.location.href="/search_results/" + search
    }
}

$(document).ready(function() {
    $("#search_box").autocomplete({
        source: names
    })

	$("#search_button").click(function(){
        search_players()
        cleanUp()
	})

	$("#search_box").keyup(function(event){
		if (event.keyCode == 13) {
			search_players()
            cleanUp()
		}
	})
})