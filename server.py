from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import random
from datetime import datetime
app = Flask(__name__)

data = [
    {
        'id': 1,
        'first_name': 'Stephen',
        'last_name': 'Curry',
        'image': 'https://www.vbetnews.com/wp-content/uploads/2020/08/Curry-1280x720-1.jpg',
        'year_born': 1988,
        'nba_draft': 2009,
        'position': 'Point Guard',
        'college': 'Davidson',
        'team': ['Golden State Warriors'],
        'nba_champion': [2015, 2017, 2018],
        'summary': 'Wardell Stephen Curry is an American professional basketball player for the Golden State Warriors of the National Basketball Association (NBA). Widely regarded as one of the greatest point guards of all time and as the greatest shooter in NBA history, Curry is credited with revolutionizing basketball by inspiring teams and players to routinely utilize the three-point shot. Curry is the son of former NBA player Dell Curry and the older brother of current NBA player Seth Curry. He played college basketball for the Davidson Wildcats, where he set the all-time scoring record for Davidson and the Southern Conference, was twice named conference player of the year, and set the single-season NCAA record during his sophomore year for most three-pointers made. Curry was selected by the Warriors with the seventh overall pick in the 2009 NBA Draft.'
    },
    {
        'id': 2,
        'first_name': 'Michael',
        'last_name': 'Jordan',
        'image': 'https://i.pinimg.com/originals/78/11/01/781101fc32db74499d4ef3b059956f0b.jpg',
        'year_born': 1963,
        'nba_draft': 1984,
        'position': 'Shooting Guard',
        'college': 'North Carolina',
        'team': ['Chicago Bulls', 'Washington Wizards'],
        'nba_champion': [1991, 1992, 1993, 1996, 1997, 1998],
        'summary': 'Michael Jeffrey Jordan (born February 17, 1963), also known by his initials MJ, is an American businessman and former professional basketball player. His biography on the official National Basketball Association (NBA) website states: "By acclamation, Michael Jordan is the greatest basketball player of all time." He was integral in popularizing the NBA around the world in the 1980s and 1990s, becoming a global cultural icon in the process. Jordan played 15 seasons in the NBA, winning six championships with the Chicago Bulls. He is the principal owner and chairman of the Charlotte Hornets of the NBA and of 23XI Racing in the NASCAR Cup Series.' 
    },
    {
        'id': 3,
        'first_name': 'Kobe',
        'last_name': 'Bryant',
        'image': 'https://wallpaperaccess.com/full/2027512.jpg',
        'year_born': 1978,
        'nba_draft': 1996,
        'position': 'Shooting Guard',
        'college': None,
        'team': ['Los Angeles Lakers'],
        'nba_champion': [2000, 2001, 2002, 2009, 2010],
        'summary': 'Kobe Bean Bryant was an American professional basketball player. A shooting guard, he spent his entire 20-year career with the Los Angeles Lakers in the National Basketball Association (NBA). Widely regarded as one of the greatest basketball players of all time, Bryant won five NBA championships, was an 18-time All-Star, a 15-time member of the All-NBA Team, a 12-time member of the All-Defensive Team, the 2008 NBA Most Valuable Player (MVP), and a two-time NBA Finals MVP. Bryant also led the NBA in scoring twice, and ranks fourth in league all-time regular season and postseason scoring. He was posthumously voted into the Naismith Memorial Basketball Hall of Fame in 2020.'
    },
    {
        'id': 4,
        'first_name': 'Lebron',
        'last_name': 'James',
        'image': 'https://library.sportingnews.com/styles/amp_lead_image_16_9/s3/2022-01/lebron-james-los-angeles-lakers_r9yimc7tlgoc1tn547hmfoh54.png?itok=UmDjMqNx',
        'year_born': 1984,
        'nba_draft': 2003,
        'position': 'Small Forward',
        'college': None,
        'team': ['Cleveland Cavaliers', 'Miami Heat', 'Los Angeles Lakers'],
        'nba_champion': [2012, 2013, 2016, 2020],
        'summary': 'LeBron Raymone James Sr. is an American professional basketball player for the Los Angeles Lakers of the National Basketball Association (NBA). Nicknamed "King James", he is widely considered one of the greatest players in NBA history and is frequently compared to Michael Jordan in debates over the greatest basketball player ever. James is the only player to have won the NBA Finals MVP with three different franchises. James has competed in ten NBA Finals, eight of them consecutively with the Heat and the Cavaliers from 2011 to 2018. His accomplishments include four NBA championships, four NBA MVP awards, four NBA Finals MVP awards, and two Olympic gold medals.'
    },
    {
        'id': 5,
        'first_name': 'Kevin',
        'last_name': 'Durant',
        'image': 'https://images.complex.com/complex/image/upload/c_fill,dpr_auto,f_auto,fl_lossy,g_face,q_auto,w_1280/uykqqdm348n5mlrlt3vh.jpg',
        'year_born': 1988,
        'nba_draft': 2007,
        'position': 'Small Forward',
        'college': 'Texas',
        'team': ['Oklahoma City Thunders', 'Golden State Warriors', 'Brooklyn Nets'],
        'nba_champion': [2017, 2018],
        'summary': 'Kevin Wayne Durant is an American professional basketball player for the Brooklyn Nets of the National Basketball Association (NBA). He played one season of college basketball for the Texas Longhorns, and was selected as the second overall pick by the Seattle SuperSonics in the 2007 NBA draft. He played nine seasons with the franchise, which became the Oklahoma City Thunder in 2008, before signing with the Golden State Warriors in 2016, winning consecutive NBA championships in 2017 and 2018. After sustaining an Achilles injury in the 2019 finals, he joined the Nets as a free agent that summer. Durant has often been called the best player in the NBA and is widely regarded as one of the greatest players of all time.'
    },
    {
        'id': 6,
        'first_name': 'Yao',
        'last_name': 'Ming',
        'image': 'https://library.sportingnews.com/styles/amp_lead_image_16_9/s3/2021-08/yao-ming-getty-072219-ftrjpg_l5bodbvf6b4w1m0mw096d3hc0.jpg?itok=RS9g4K6D',
        'year_born': 1980,
        'nba_draft': 2002,
        'position': 'Center',
        'college': None,
        'team': ['Houston Rockets'],
        'nba_champion': [],
        'summary': 'Yao Ming is a Chinese basketball executive and former professional player. He played for the Shanghai Sharks of the Chinese Basketball Association (CBA) and the Houston Rockets of the National Basketball Association (NBA). Yao was selected to start for the Western Conference in the NBA All-Star Game eight times, and was named to the All-NBA Team five times. During his final season, he was the tallest active player in the NBA, at 2.29 m (7 ft 6 in).'
    },
    {
        'id': 7,
        'first_name': 'Klay',
        'last_name': 'Thompson',
        'image': 'https://www.sportsnet.ca/wp-content/uploads/2019/01/Klay-Thompson.jpg',
        'year_born': 1990,
        'nba_draft': 2011,
        'position': 'Shooting Guard',
        'college': 'Washington State',
        'team': ['Golden State Warriors'],
        'nba_champion': [2015, 2017, 2018],
        'summary': 'Klay Alexander Thompson is an American professional basketball player for the Golden State Warriors of the National Basketball Association (NBA). He is credited as one of the greatest shooters in NBA history. A three-time NBA champion with the Warriors, he is a five-time NBA All-Star and a two-time All-NBA Third Team honoree. He has also been named to the NBA All-Defensive Second Team.'
    },
    {
        'id': 8,
        'first_name': 'Draymond',
        'last_name': 'Green',
        'image': 'https://basketballforever.com/wp-content/uploads/2020/08/green-1.jpg',
        'year_born': 1990,
        'nba_draft': 2012,
        'position': 'Power Forward',
        'college': 'Michigan State',
        'team': ['Golden State Warriors'],
        'nba_champion': [2015, 2017, 2018],
        'summary': 'Draymond Jamal Green Sr. is an American professional basketball player for the Golden State Warriors of the National Basketball Association (NBA). Green, who plays primarily at the power forward position, is a three-time NBA champion, a four-time NBA All-Star, a two-time member of the All-NBA Team, a six-time member of the All-Defensive Team and a two-time Olympic gold medalist. In 2017, he won the NBA Defensive Player of the Year and led the league in steals.'
    },
    {
        'id': 9,
        'first_name': 'Kawhi',
        'last_name': 'Leonard',
        'image': 'https://sport.one/content/images/2020/07/22-26.jpg',
        'year_born': 1991,
        'nba_draft': 2011,
        'position': 'Small Forward',
        'college': 'San Diego State',
        'team': ['San Antonio Spurs', 'Toronto Raptors', 'Los Angeles Clippers'],
        'nba_champion': [2014, 2019],
        'summary': 'Kawhi Anthony Leonard is an American professional basketball player for the Los Angeles Clippers of the National Basketball Association (NBA). He played two seasons of college basketball for the San Diego State Aztecs and was named a consensus second-team All-American as a sophomore. Leonard opted to forgo his final two seasons at San Diego State to enter the 2011 NBA draft. He was selected by the Indiana Pacers with the 15th overall pick before being traded to the San Antonio Spurs on draft night.'
    },
    {
        'id': 10,
        'first_name': 'Giannis',
        'last_name': 'Antetokounmpo',
        'image': 'https://ewscripps.brightspotcdn.com/dims4/default/910739f/2147483647/strip/true/crop/2661x1497+0+139/resize/1280x720!/quality/90/?url=http%3A%2F%2Fewscripps-brightspot.s3.amazonaws.com%2F1c%2F9a%2Fe69d4a0649ffb6115ea68e1699bd%2Fgettyimages-1133943635.jpg',
        'year_born': 1994,
        'nba_draft': 2013,
        'position': 'Power Forward',
        'college': None,
        'team': ['Milwaukee Bucks'],
        'nba_champion': [2021],
        'summary': 'Giannis Sina Ugo Antetokounmpo is a Greek professional basketball player for the Milwaukee Bucks of the National Basketball Association (NBA). Antetokounmpo\'s nationality, in addition to his size, speed and ball-handling skills have earned him the nickname "Greek Freak". Born and raised in Athens to Nigerian immigrants, Antetokounmpo began playing basketball for the youth teams of Filathlitikos in Athens. In 2011, he began playing for the club\'s senior team before entering the 2013 NBA draft, where he was selected 15th overall by the Bucks.'
    }
]

current_id = len(data) + 1

years = []
for i in range(datetime.now().year, 1945, -1):
    years.append(i)

names = []
for player in data:
      names.append(player['first_name'] + ' ' + player['last_name'])

teams = [
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizard"
]


@app.route('/')
def index():
   # Get 3 random items from data
   rand = random.sample(range(len(data)),6)

   players = []
   for i in rand:
      players.append(data[i])
   return render_template('index.html', players=players, names=names)


@app.route('/search_results/<search_term>', methods=['GET', 'POST'])
def search(search_term):
    global data
    results = []

    for player in data:
        full_name = player['first_name'] + ' ' + player['last_name']
        position = player['position'].lower()
        last_team = player['team'][-1]

        if search_term.lower() in last_team.lower() and player not in results:
            results.append(player)
        
        if search_term.lower() in position and player not in results:
            results.append(player)

        if search_term.lower() in full_name.lower() and player not in results:
            results.append(player)

    return render_template('results.html', results=results, names=names, search_term=search_term, key=None)


# Clickable Search based on key
@app.route('/search/<key>/<search_term>', methods=['GET', 'POST'])
def clickable_search(key, search_term):
    global data
    results = []

    for player in data:
        value = player[key]
        try:
            if search_term.lower() == value.lower():
                results.append(player)
        except: 
            if search_term in value:
                results.append(player)

    return render_template('results.html', results=results, names=names, search_term=search_term, key=key)


@app.route('/view/<id>', methods=['GET'])
def view(id):
   global data
   for player in data:
      if int(id) == player['id']:
         return render_template('view.html', player=player, names=names)


@app.route('/add', methods=['GET'])
def add():
    return render_template('add.html', names=names, years=years, teams=teams)


@app.route('/add_player', methods=['GET', 'POST'])
def add_player():
    global data
    global current_id
    global years
    
    new_player = request.get_json()
    new_player['id'] = current_id
    data.append(new_player)

    current_id += 1

    url = 'view/' + str(new_player['id'])

    return jsonify(url=url)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    global data
    for player in data:
        if int(id) == player['id']:
            return render_template('edit.html', player=player, names=names, teams=teams, years=years)


@app.route('/edit_player', methods=['GET', 'POST'])
def edit_player():
    global data
    updates = request.get_json()
    id = int(updates['id'])

    for player in data:
        if id == player['id']:
            player['first_name'] = updates['first_name']
            player['last_name'] = updates['last_name']
            player['image'] = updates['image']
            player['year_born'] = updates['year_born']
            player['nba_draft'] = updates['nba_draft']
            player['position'] = updates['position']
            player['college'] = updates['college']
            player['team'] = updates['team']
            player['nba_champion'] = updates['nba_champion']
            player['summary'] = updates['summary']

    return jsonify(updates=updates)


if __name__ == '__main__':
   app.run(debug = True)