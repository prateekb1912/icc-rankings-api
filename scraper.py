from bs4 import BeautifulSoup
import requests



class TeamsRankingScraper():
    
    BASE_URL = 'https://www.icc-cricket.com/rankings/'
    MENS_URL = BASE_URL + 'mens/team-rankings'
    WOMENS_URL = BASE_URL + 'womens/team-rankings'

    def get_teams(self, format, gender):
        URL = self.WOMENS_URL if gender == 'womens' else self.MENS_URL

        URL += f'/{format}'

        resp = requests.get(URL)
        soup = BeautifulSoup(resp.content, 'lxml')

        table = soup.find('tbody')

        for row in table.find_all('tr'):
            data = row.find_all('td')

            pos, team, matches, points, rating = [d.text for d in data]
            
            pos = int(pos)
            team = ''.join(team.split("\n")[:-2])
            matches = int(matches)
            points = int(''.join(points.split(',')))
            rating = int(''.join(rating.split('\n')))

            print([pos, team, matches, points, rating])
