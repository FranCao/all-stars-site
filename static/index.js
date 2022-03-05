function display_player(player){

	let cont = $('<div class="col-md-4 player-cont-style">')
	let player_cont = $('<div class="player-cont-style-2">')

	let image_url = player['image']
	let name = player['first_name'] + ' ' + player['last_name']
	let position = player['position']
	let year_drafted = player['nba_draft']
	let team = player['team'].slice(-1)

	let image_cont = $('<a href="/view/' + player["id"] + '"></a>')
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
	return cont
}

$(document).ready(function() {
    $("#players").empty()
	$.each(players, function(index, value){
		let player = display_player(value)
		$("#players").append(player)
	})

})