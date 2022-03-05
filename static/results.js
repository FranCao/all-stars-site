function display_results(results){
	$.each(results, function(index, value){
		let cont = $('<div class="col-md-4 player-cont-style">')
		let player_cont = $('<div class="player-cont-style-2">')

		let image_url = value['image']
		let name = value['first_name'] + ' ' + value['last_name']
		let position = value['position']
		let year_drafted = value['nba_draft']
		let team = value['team'].slice(-1)

		let image_cont = $('<a href="/view/' + value["id"] + '"></a>')
		let image = $('<img src="' + image_url + '" alt="' + name + '" class="player-display-image-style img-fluid">')
		image_cont.html(image)
		player_cont.append(image_cont)

		let name_cont = $('<div class="player-name-style">')
		name_cont.html(name)
		player_cont.append(name_cont)

		let position_cont = $('<div class="player-position-style">')
		position_cont.html(position)
		player_cont.append(position_cont)

		let team_cont = $('<div class="player-team-style">')
		team_cont.html('<span class="player-detail-style">Currently with </span> ' + team)
		player_cont.append(team_cont)

		let year_cont = $('<div class="player-year-style">')
		year_cont.html('Drafted by NBA in ' + year_drafted)
		player_cont.append(year_cont)

		cont.append(player_cont)
		$("#results").append(cont)
	})
}

$(document).ready(function() {
	$("#results").empty()

	let result_len = results.length

	$("#page-title").html('Search results for "' + search_term + '": ' + result_len + ' results found')
	if (result_len == 0){
		$("#results").append("No matches were found, please try your search again")
	}else{
		display_results(results)
	}
})