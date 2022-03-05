function search_key(key, value){
    window.location.href="/search/" + key + "/" + value
}

$(document).ready(function() {
    
    let name = player['first_name'] + ' ' + player['last_name']

    $("#view-page-title").html(name)

    $("#edit-button").html('<button class="btn btn-outline-success edit-button-style" type="button" id="edit_button">Edit Player</button>')

    let image = $('<img src="' + player['image'] + '" alt="' + name + '" class="view-image-style">')
    $("#image").append(image)
    $("#summary").append(player['summary'])

    $("#year-born").append(player['year_born'])
    $("#nba-draft").append(player['nba_draft'])

    let position = '<button class="view-box-label" type="button" id="position_clickable">' + player['position'] + '</button>'
    $("#position").html(position)

    if (player['college']){
        $("#college").append(player['college'])
    } else{
        $("#college").append("None")
    }

    $.each(player['team'], function(index, value){
        let team = '<button class="view-box-label-small" type="button" id="team_clickable">' + value + '</button>'
        $("#team").append(team)
        // Clickable teams
        $("#team_clickable").click(function(){
            search_key("team", value)
        })
    })

    let champ_len = (player['nba_champion']).length
    $.each(player['nba_champion'], function(index, value){
        let content = $('<span>')
        if (index == champ_len - 1){
            content.append(value)
        } else{
            content.append(value + ', ')
        }
        $("#nba-champ").append(content)
    })

    // Edit reroutes to /edit endpoint
    $("#edit_button").click(function(){
        window.location.href="/edit/" + player['id']
	})

    // Clickable position
    $("#position_clickable").click(function(){
        let value = player['position']
        search_key("position", value)
    })

})