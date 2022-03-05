function display_player(){
    $("#player-id").val(player['id'])
    $("#first-name-input").val(player['first_name'])
    $("#last-name-input").val(player['last_name'])
    $("#image-url-input").val(player['image'])
    $("#year-born-input").val(player['year_born'])
    $("#nba-draft-input").val(player['nba_draft'])
    $("#position-input").val(player['position'])
    $("#college-input").val(player['college'])
    $("#teams-input").val(player['team'])
    $("#nba-champion-input").val(player['nba_champion'])
    $("#bio-input").val(player['summary'])
}

function isNullOrWhitespace(input){
	return !input || !input.trim();
}

function isNumber(input){
	return /^\d+$/.test(input)
}

function containsNumber(input){
	return /\d/.test(input)
}

function isImage(input){
	return /^https?:\/\/.+\.(jpg|jpeg|png|webp|avif|gif|svg)$/.test(input)
}

function return_error(field_name, message){
	let field = $(field_name)
	field.addClass('is-invalid')
	let warning = $('<div class="invalid-feedback"></div>')
	warning.html(message)
	field.after(warning)
}

function valid_string(field, user_input, field_name){
	let error = false
	if (isNullOrWhitespace(user_input)){
		return_error(field,  field_name + " cannot be blank or only contain whitespace")
		$(field).focus()
		$(field).val("")
		error = true
	}
	if (containsNumber(user_input)){
		return_error(field, field_name + " cannot contain numbers")
		$(field).focus()
		error = true
	}
	return error
}

function valid_college(field, user_input, field_name){
	let input = user_input.toLowerCase()
	let error = false
	if (user_input.length != 0 && user_input.trim() == 0){
		return_error(field,  field_name + " cannot contain only whitespace")
		$(field).focus()
		$(field).val("")
		error = true
	}
	if (input == "none" || input == "n/a" || input == "dna" || input == "no"){
		return_error(field,  "Please leave " + field_name + " field blank if player did not attend college")
		error = true
	}
	if (containsNumber(user_input)){
		return_error(field, field_name + " cannot contain numbers")
		$(field).focus()
		error = true
	}
	return error
}

function valid_image(field, user_input, field_name){
	let error = false
	if (isNullOrWhitespace(user_input)){
		return_error(field,  field_name + " cannot be blank or only contain whitespace")
		$(field).focus()
		$(field).val("")
		error = true
	}
	if (!isImage(user_input)){
		return_error(field, field_name + " must be a proper image URL ending in JPG, JPEG, PNG, or GIF")
		$(field).focus()
		error = true
	}
	return error
}

function valid_year(field, user_input, field_name){
	let error = false
	if (isNullOrWhitespace(user_input)){
		return_error(field,  field_name + " cannot be blank or only contain whitespace")
		$(field).focus()
		$(field).val("")
		error = true
	}
	if (!isNumber(user_input)){
		return_error(field,  field_name + " can only contain numbers")
		$(field).focus()
		error = true
	}
	if (user_input.length > 4){
		return_error(field,  field_name + " cannot exceed 4 numbers")
		$(field).focus()
		error = true
	}
	if (user_input.length != 4){
		return_error(field,  field_name + " must be a proper year in YYYY format")
		$(field).focus()
		error = true
	}
	let test_year = new Date().getFullYear()
	if (user_input > test_year){
		return_error(field,  field_name + " must not be in the future, are you time traveling?")
		$(field).focus()
		error = true
	}
	return error
}


function error_detection(){
	let error = false

	let first_name = $("#first-name-input").val()
	let last_name = $("#last-name-input").val()
	let image_url = $("#image-url-input").val()
	let year_born = $("#year-born-input").val()
	let year_drafted = $("#nba-draft-input").val()
	let college = $("#college-input").val()
	let position = $("#position-input").val()
	let teams = $("#teams-input").val()
	let summary = $("#bio-input").val()

	if (isNullOrWhitespace(summary)){
		return_error("#bio-input",  "Summary cannot be blank or only contain whitespace")
		$("#bio-input").focus()
		$("#bio-input").val("")
		error = true
	}

	if (teams.length == 0){
		return_error("#teams-input", "Player must belong to at least one NBA Team")
		error = true
	}

	if (position == null){
		return_error("#position-input", "Player must have a position")
		error = true
	}

	if (valid_college("#college-input", college, "College")){
		error = true
	}

	if (valid_year("#nba-draft-input", year_drafted, "NBA Draft Year")){
		error = true
	}

	if (valid_year("#year-born-input", year_born, "Year Born")){
		error = true
	}

	if (valid_image("#image-url-input", image_url, "Image URL")){
		error = true
	}

	if (valid_string("#last-name-input", last_name, "Last Name")){
		error = true
	}

	if (valid_string("#first-name-input", first_name, "First Name")){
		error = true
	}
	return error
}

$(document).ready(function() {

    display_player()

	$("#edit-submit-btn").click(function(){
		// Remove old error messages
		$(".form-control").removeClass("is-invalid")
		$(".invalid-feedback").remove()

		// Test for input errors
		let error = error_detection()

		if (error == false){
			let updates = {
                "id": $("#player-id").val(),
				"first_name": $("#first-name-input").val(),
				"last_name": $("#last-name-input").val(),
				"image": $("#image-url-input").val(),
				"year_born": $("#year-born-input").val(),
				"nba_draft": $("#nba-draft-input").val(),
				"position": $("#position-input").val(),
				"college": $("#college-input").val(),
				"team": $("#teams-input").val(),
				"nba_champion": $("#nba-champion-input").val(),
				"summary": $("#bio-input").val()
			}
			
			$.ajax({
				type: "POST",
				url: "/edit_player",                
				dataType : "json",
				contentType: "application/json; charset=utf-8",
				data : JSON.stringify(updates),
				success: function(result){
					window.location.href = "/view/" + $("#player-id").val()
				},
				error: function(request, status, error){
					console.log("Error");
					console.log(request)
					console.log(status)
					console.log(error)
				}
			});

		}
	})

    $("#edit-discard-btn").click(function(){
        let proceed = confirm("Are you sure you want to discard all edits?")
        if (proceed){
            window.location.href = "/view/" + $("#player-id").val()
        }
    })
})