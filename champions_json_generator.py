PATCH = 10.15

# List by hardest to easiest champion skill cap
s_tier = (
    'Aurelion Sol', 'Kalista', 'Draven', 'Gangplank', 'Tresh', 'Zed', 'Yasuo', 'Lee Sin', 'Azir', 'Nidalee', 
    'Riven', 'LeBlanc', 'Akali', 'Bard'
)

a_tier = (
    'Rengar', 'Katarina', 'Cassiopeia', 'Elise', 'Twisted Fate', 'Shaco', 'Ivern', 'Pyke', 'Zoe', 'Vayne',
    'Qiyana', 'Lucian', 'Rakan', 'Tahm Kench', 'Jayce', 'Irelia', 'Fiora', 'Syndra', 'Kai\'Sa', 'Aatrox',
    'Rek\'Sai'
)

b_tier = (
    'Singed', 'Xerath', 'Anivia', 'Kha\'Zix', 'Ryze', 'Kled', 'Kindred', 'Orianna', 'Evelynn', 'Rumble',
    'Ekko', 'Taliyah', 'Vladimir', 'Karthus', 'Janna', 'Xayah', 'Ezreal', 'Camille', 'Gnar', 'Kayn',
    'Kog\'Maw', 'Alisar', 'Gragas', 'Sylas', 'Talon', 'Viktor', 'Aphelios'
)

c_tier = (
    'Fizz', 'Renekton', 'Heimerdinger', 'Ahri', 'Vel\'Koz', 'Jax', 'Twitch', 'Illaoi', 'Urgot', 'Jhin',
    'Yorik', 'Graves', 'Nunu & Willump', 'Kassadin', 'Shen', 'Ornn', 'Kennen', 'Sion', 'Quinn', 'Varus',
    'Senna', 'Fiddlesticks', 'Lissandra', 'Caitlyn', 'Lulu', 'Nami', 'Corki', 'Galio', 'Taric'
)

d_tier = (
    'Darius', 'Tryndamere', 'Mordekaiser', 'Master Yi', 'Neeko', 'Swain', 'Teemo', 'Zyra', 'Kayle', 'Olaf',
    'Udyr', 'Tristana', 'Nocturne', 'Nasus', 'Shyvana', 'Poppy', 'Volibear', 'Zac', 'Sejuani', 'Hecarim',
    'Skarner', 'Diana', 'Cho\'Gath', 'Jarvan IV', 'Blitzcrank', 'Nautilus', 'Wukong', 'Trundle', 'Morgana',
    'Zilean', 'Karma', 'Braum', 'Leona', 'Sivir', 'Maokai', 'Sett'
)

e_tier = (
    'Brand', 'Jinx', 'Vi', 'Veigar', 'Ziggs', 'Lux', 'Pantheon', 'Malzahar', 'Soraka', 'Miss Fortune', 
    'Ashe', 'Mundo', 'Yuumi', 'Xin Zao', 'Garen', 'Amumu', 'Rammus', 'Warwick', 'Malhpite', 'Sona', 'Annie'
)

unkown_tier = (
    'Lillia', 'Yone'
)

abilities = {
    'Aatrox': (
        'DEATHBRINGER STANCE', 'Periodically, Aatrox\'s next basic attack deals bonus physical damage and heals him, based on the target\'s max health.',
        'THE DARIN BLADE', 'Aatrox slams his greatsword down, dealing physical damage. He can swing three times, each with a different area of effect.',
        'INFERNAL CHAINS', 'Aatrox smashes the ground, dealing damage to the first enemy hit. Champions and large monsters have to leave the impact area quickly or they will be dragged to the center and take the damage again.',
        'UMBRAL DASH', 'Passively, Aatrox heals when damaging enemy champions. On activation, he dashes in a direction.',
        'WORLD ENDER', 'Aatrox unleashes his demonic form, fearing nearby enemy minions and gaining attack damage, increased healing, and movement speed. If he gets a takedown, this effect is extended.'
    ),
    'Ahri': (
        'VASTAYAN GRACE', 'Whenever Ahri\'s spells hit a champion 2 times within a short period, she briefly gains movement speed.',
        'ORB OF DECEPTION', 'Ahri sends out and pulls back her orb, dealing magic damage on the way out and true damage on the way back. After earning several spells hits, Ahri\'s next orb hits will restore her health.',
        'FOX-FIRE', 'Ahri releases three fox-fires, that lock onto and attack nearby enemies',
        'CHARM', 'Ahri blows a kiss that damages and charms an enemy it encounters, instantly stopping movement abilities and causing them to walk harmlessly towards her. The target temporarily takes increased damage from Ahri.',
        'SPIRIT RUSH', 'Ahri dashes forward and fires essence bolts, damaging nearby enemies. Spirit Rush can be cast up to three times before going on cooldown'
    )
}

# List strongest to weakest champions (meta)
tier_op = (
    'Maokai', 'Karthus', 'Volibear', 'Nunu & Willump', 'Galio', 'Talon', 'Caitlyn', 'Ashe', 'Bard'
)

tier_1 = (
    'Darius', 'Camille', 'Renekton', 'Garen', 'Elise', 'Zed', 'Kassadin', 'Fizz', 'Lulu', 'Blitzcrank'
)

tier_2 = (
    'Wukong', 'Quinn', 'Jax', 'Fiora', 'Ekko', 'Graves', 'Rek\'Sai', 'Kha\'Zix', 'Zac', 'Kayn',
    'Cassiopeia', 'Pantheon', 'Yasuo', 'Katarina', 'Nocturne', 'Ezreal', 'Vayne', 'Senna', 'Yasuo', 'Swain',
    'Leona', 'Morgana', 'Thresh', 'Karma', 'Zilean', 'Sona'
)

# Regroup and sort every champion in a single list
champions = sorted(s_tier + a_tier + b_tier + c_tier + d_tier + e_tier + unkown_tier)

word = '{\n"champions":\n['
for index, champ in enumerate(champions):
    # Don't put a ',' if first element when opening champion part
    if index == 0: word += '{\n'
    else: word += ',\n{\n'

    # Add champion name and (maybe) display name
    if "'" in champ or ' ' in champ:
        word += '"name": "%s"\n' % (champ.replace("'", '').replace(' ', ''))
        word += ',"displayName": "%s"\n' % (champ)
    else:
        word += '"name": "%s"\n' % (champ)

    # Add champion skill caps rank
    word += ',"difficulty_rank": '
    if champ in s_tier: word += '%i' %(s_tier.index(champ) + 1)
    elif champ in a_tier: word += '%i' %(a_tier.index(champ) + len(a_tier) + 1)
    elif champ in b_tier: word += '%i' %(b_tier.index(champ) + len(s_tier + a_tier) + 1)
    elif champ in c_tier: word += '%i' %(c_tier.index(champ) + len(s_tier + a_tier + b_tier) + 1)
    elif champ in d_tier: word += '%i' %(d_tier.index(champ) + len(s_tier + a_tier + b_tier + c_tier) + 1)
    elif champ in e_tier: word += '%i' %(e_tier.index(champ) + len(s_tier + a_tier + b_tier + c_tier + d_tier) + 1)
    else: word += '"?"'
    word += '\n'

    # Add champion meta rank
    word += ',"meta_tier": '
    if champ in tier_op: word += '"OP"'
    elif champ in tier_1: word += '1'
    elif champ in tier_2: word += '2'
    else: word += '": weak"'
    word += '\n'

    # Add abilities
    if champ in abilities and len(abilities[champ]) == 10:
        word += ',"passive_name": "%s"\n' % (abilities[champ][0].replace("'", "\\\\'"))
        word += ',"passive_description": "%s"\n' % (abilities[champ][1].replace("'", "\\\\'"))
        word += ',"q_name": "%s"\n' % (abilities[champ][2].replace("'", "\\\\'"))
        word += ',"q_description": "%s"\n' % (abilities[champ][3].replace("'", "\\\\'"))
        word += ',"w_name": "%s"\n' % (abilities[champ][4].replace("'", "\\\\'"))
        word += ',"w_description": "%s"\n' % (abilities[champ][5].replace("'", "\\\\'"))
        word += ',"e_name": "%s"\n' %(abilities[champ][6].replace("'", "\\\\'"))
        word += ',"e_description": "%s"\n' %(abilities[champ][7].replace("'", "\\\\'"))
        word += ',"r_name": "%s"\n' %(abilities[champ][8].replace("'", "\\\\'"))
        word += ',"r_description": "%s"\n' %(abilities[champ][9].replace("'", "\\\\'"))

    # Close champion part
    word += '}'

word += '\n]\n}'
with open('champs_temp.json', 'w') as f:
    f.write(word)