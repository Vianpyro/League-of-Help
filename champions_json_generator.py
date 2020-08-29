# -*- coding: utf-8 -*-
from lxml import html
import requests


class GetLeagueStatsBot:
    def __init__(self):
        base_url = 'https://na.leagueoflegends.com/en-us/news/tags/patch-notes'
        try:
            page = requests.get(f'{base_url}')
            tree = html.fromstring(page.content)
        except: pass

        try: self.PATCH = tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/div[1]/div/ol/li[1]/a/article/div[2]/div/h2/text()')[0][6:-6]
        except: self.PATCH = '"?"'
        print('PATCH: ' + self.PATCH)

    def get_champ_meta_tier(self, champion):
        base_url = 'https://na.op.gg/champion'
        try:
            champ_url = champion.replace('-', '').lower()
            page = requests.get(f'{base_url}/{champ_url}/statistics')
            tree = html.fromstring(page.content)
        except: pass

        try: return tree.xpath('//*[@class="champion-stats-header-info__tier"]/b/text()')[0][-1]
        except: pass

        
    def get_champ_abilities(self, champion):
        base_url = 'https://na.leagueoflegends.com/en-us/champions'
        page = requests.get(f'{base_url}/{champion.lower()}/')
        tree = html.fromstring(page.content)

        recent_abilities = {
            'Lillia': (
                'Dream-Laden Bough', "Lillia's abilities apply Dream Dust, dealing a portion of the target's maximum health as magic damage over a duration.",
                'Blooming Blows', "Lillia swings her branch in the air and deals magic damage to nearby enemies, dealing true damage to those at the outer edge of the circle, Lillia gains stacking movement speed whenever she hits a target with a skill.",
                'Watch Out! Eep!', 'Lillia winds up for a huge strike with her branch, dealing magic damage to enemies. Enemies at the center of the impact recieve more damage.',
                'Swirlseed', "Lillia lobs a Swirlseed overhead, dealing magic damage to enemies and slowing them for a duration. If Lillia's Swirlseed misses, it's continue to roll until it hits and enemy or collides with terrain.",
                'Lilting Lullaby', 'Lillia casts a lullaby over her enemies and those affected by her Dream Dust become increasingly slowed before falling asleep for a duration. When awakened by damage, enemies will take additional magic damage.'
            ),
            'Yone': (
                'Way of the Hunter', 'Yone uses two blades, causing every second attack to deal more magic damage. His critical strike chance is also doubled but his critical strikes deal reduced damage.',
                'Mortal Steel', 'Yone thrusts forward, dealing physical damage to opponents, On hit, he gains a stack of Gathering Storm. At two stacks, Yone can dash forward with a wave that makes enemies airborn.'
                'Spirit Cleave', "Yone cleaves forward in a massive arc, dealing a portion of the target's max health. After successfully hitting an enemy, Yone also gains a temporary shield. The shield's power increases per champion struck.",
                'Soul Unbound', "Yone can enter his Spirit Form, gaingin movement speed and leaving his body behing. When Yone's Spirit Form expires, he'll snap back into his body and deal a pecentage of all the damage he dealt while in Spirit Form.",
                'Fate Sealed', 'Yone strikes all enemies in his path, blinking behind the last enemy hit and knocking everyone airborn towards him.'
            ),
            'Samira': (
                'Daredevil Impulse', "Samira builds a combo by hitting attacks or abilities from the previous hit. Each one increases her Style, from 'E' to 'S' grade. Samira gains movement speed according to her grade. Samira's attacks in melee range deal additional magic damage, increased with the target missing health. Samira's attacks against enemies affected by Immobilizing effects Knock Up for 0.5 seconds and deal damage over 6 separate attacks. Samira dashes into range against targets slightly outside of her attack range.",
                'Flair', f'Samira fires a shot, dealing physical damage to the first enemy hit. If this ability is cast towards an enemy in melee range, Samira will instead slash with her sword, dealing physical damage. Either hit can critically strike for 25% bonus damage. If cast during Wild Rush, Samira will strike all enemies in her path upon completion.',
                'Blade Whirl', 'Samira slashes around her for 1 second, damaging enemies twice dealing physical damage each and destroying any enemy missiles that enter the area.',
                'Wild Rush', "Samira dashes through an enemy or ally, slashing enemies she passes through and gaining Attack Speed. Killing an enemy champion refreshes this ability's cooldown.",
                'Inferno Trigger', "Samira can only use this ability if her current Style rating is 'S'. Samira unleashes a torrent of shots from her weapons, wildly shooting all enemies surrounding her 10 times over 2 seconds, each shot dealing physical damage and applying lifesteal. Each shot can also critically strike."
            )
        }

        try:
            return (
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[1]/h5/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[1]/p/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[2]/h5/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[2]/p/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[3]/h5/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[3]/p/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[4]/h5/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[4]/p/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[5]/h5/text()')[0].replace("\n", " "),
                tree.xpath('//*[@id="gatsby-focus-wrapper"]/div/section[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/ol/li[5]/p/text()')[0].replace("\n", " ")
            )
        except:
            try: return recent_abilities[champion]
            except: pass


if __name__ == '__main__':
    champ_stats = GetLeagueStatsBot()

new_champs, new_winrate = [], []

tier_op, tier_1, tier_2, tier_3, tier_4, tier_5 = [], [], [], [], [], []
for j in range (len(new_champs)):
    if new_winrate[j] > 53.0: tier_op.append(new_champs[j])
    elif 53.0 > new_winrate[j] > 51.0: tier_1.append(new_champs[j])
    elif 51.0 > new_winrate[j] > 50.0: tier_2.append(new_champs[j])
    elif 50.0 > new_winrate[j] > 49.0: tier_3.append(new_champs[j])
    elif 49.0 > new_winrate[j] > 48.0: tier_4.append(new_champs[j])
    else: tier_5.append(new_champs[j])

# List by hardest to easiest champion skill cap
champions_list = (
    'Aurelion Sol', 'Kalista', 'Draven', 'Gangplank', 'Thresh', 'Zed', 'Yasuo', 'Lee Sin', 'Azir', 'Nidalee',
    'Riven', 'Yone', 'Leblanc', 'Akali', 'Bard', 'Rengar', 'Katarina', 'Cassiopeia', 'Elise', 'Twisted Fate',
    'Shaco', 'Ivern', 'Pyke', 'Zoe', 'Vayne', 'Qiyana', 'Lucian', 'Rakan', 'Tahm Kench', 'Jayce', 'Irelia', 
    'Fiora', 'Syndra', 'Kai\'Sa', 'Aatrox', 'Rek\'Sai', 'Singed', 'Xerath', 'Anivia', 'Kha\'Zix', 'Ryze', 
    'Kled', 'Kindred', 'Orianna', 'Evelynn', 'Rumble', 'Ekko', 'Taliyah', 'Vladimir', 'Karthus', 'Janna', 
    'Xayah', 'Ezreal', 'Camille', 'Gnar', 'Kayn', 'Kog\'Maw', 'Alistar', 'Gragas', 'Sylas', 'Talon', 'Viktor',
    'Aphelios', 'Fizz', 'Renekton', 'Heimerdinger', 'Ahri', 'Vel\'Koz', 'Jax', 'Twitch', 'Illaoi', 'Urgot',
    'Jhin',  'Yorick', 'Graves', 'Nunu & Willump', 'Kassadin', 'Shen', 'Ornn', 'Kennen', 'Sion', 'Quinn', 
    'Varus', 'Senna', 'Fiddlesticks', 'Lissandra', 'Caitlyn', 'Lulu', 'Nami', 'Corki', 'Galio', 'Taric', 
    'Darius', 'Tryndamere', 'Mordekaiser', 'Master Yi', 'Neeko', 'Lillia', 'Swain', 'Teemo', 'Zyra', 'Kayle',
    'Olaf', 'Udyr', 'Tristana', 'Nocturne', 'Nasus', 'Shyvana', 'Poppy', 'Volibear', 'Zac', 'Sejuani',
    'Hecarim', 'Skarner', 'Diana', 'Cho\'Gath', 'Jarvan IV', 'Blitzcrank', 'Nautilus', 'Wukong', 'Trundle',
    'Morgana', 'Zilean', 'Karma', 'Braum', 'Leona', 'Sivir', 'Maokai', 'Sett', 'Brand', 'Jinx', 'Vi', 'Veigar',
    'Ziggs', 'Lux', 'Pantheon', 'Malzahar', 'Soraka', 'Miss Fortune', 'Ashe', 'Dr. Mundo', 'Yuumi', 'Xin Zhao',
    'Garen', 'Amumu', 'Rammus', 'Warwick', 'Malphite', 'Sona', 'Annie', 'Samira', 'Seraphine', 'Ultra-Heavy Tank Support'
)

no_data_champions = ('Samira', 'Seraphine', 'Ultra-Heavy Tank Support')

word = '{\n"patch": %s,\n"champions":\n[' % (champ_stats.PATCH)
total_champions = len(champions_list)
for index, champ in enumerate(sorted(champions_list)):
    # Don't put a ',' if first element when opening champion part
    if index == 0: word += '{\n'
    else: word += ',\n{\n'

    # Add champion name and (maybe) display name
    LoL_names = {
        'Aurelion Sol': 'Aurelion-Sol',
        "Cho'Gath": 'Cho-Gath',
        'Dr. Mundo': 'Dr-Mundo',
        'Jarvan IV': 'Jarvan-IV',
        "Kai'Sa": 'Kai-Sa',
        "Kha'Zix": 'Kha-Zix',
        "Kog'Maw": 'Kog-Maw',
        'Lee Sin': 'Lee-Sin',
        'Master Yi': 'Master-Yi',
        'Miss Fortune': 'Miss-Fortune',
        'Nunu & Willump': 'Nunu', 
        "Rek'Sai": 'Rek-Sai',
        'Tahm Kench': 'Tahm-Kench',
        'Twisted Fate': 'Twisted-Fate',
        "Vel'Koz": 'Vel-Koz',
        'Xin Zhao': 'Xin-Zhao'
    }

    if champ in LoL_names:
        word += f'"name": "{LoL_names[champ]}",\n'
        word += f'"displayName": "{champ}",\n'
        champions_abilities = champ_stats.get_champ_abilities(LoL_names[champ])
        champ_meta_tier = champ_stats.get_champ_meta_tier(LoL_names[champ].lower())
    else:
        champions_abilities = champ_stats.get_champ_abilities(champ)
        word += f'"name": "{champ}",\n'
        champ_meta_tier = champ_stats.get_champ_meta_tier(champ.lower())

    # Add abilities
    if champions_abilities != None:
        abilities = ['p', 'q', 'w', 'e', 'r']
        for j in range (len(abilities)):
            word += f'"{abilities[j]}_name": "{champions_abilities[j * 2]}",\n'
            word += f'"{abilities[j]}_description": "{champions_abilities[(j * 2) + 1]}",\n'

    # Add champion skill caps rank
    if champ in no_data_champions: word += '"difficulty_rank": "?",\n'
    else: word += f'"difficulty_rank": {champions_list.index(champ) + 1},\n'

    # Add champion meta rank
    word += '"meta_tier": '
    if champ_meta_tier != None: word += f'{champ_meta_tier}'
    else: word += '"?"'
    word += '\n'

    # Close champion part
    word += '}'

    # Print the amount of champions left
    print(total_champions - index)

word += ']}'
with open('src/json/champions.json', 'w') as f:
    f.write(word)

input('JSON file generated successfuly, press enter to close this dialog...')
