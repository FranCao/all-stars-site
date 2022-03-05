$(document).ready(function() {
    
    let name = player['first_name'] + ' ' + player['last_name']

    $("#view-page-title").html(name)

    $("#edit-button").html('<button class="btn btn-outline-success edit-button-style" type="button" id="edit_button">Edit Player</button>')

    let image = $('<img src="' + player['image'] + '" alt="' + name + '" class="view-image-style">')
    $("#image").append(image)
    $("#summary").append(player['summary'])

    $("#year-born").append(player['year_born'])
    $("#nba-draft").append(player['nba_draft'])
    $("#position").html('<span class="view-box-label"> ' + player['position'] + ' </span>')

    if (player['college']){
        $("#college").append(player['college'])
    } else{
        $("#college").append("None")
    }

    $.each(player['team'], function(index, value){
        let list = $('<div class="view-box-label-small">' + value + '</div>')
        $("#team").append(list)
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

})