"""
questions.py — Banque de questions JDN AniDex
══════════════════════════════════════════════

Contient la banque de questions couvrant 1000+ animés.
10 questions sont tirées aléatoirement à chaque partie.

COMMENT AJOUTER DES QUESTIONS :
    Ajoutez un dictionnaire à la liste QUESTION_BANK :
    {
        'cat':  'Catégorie',           # Ex: "Shōnen", "Isekai", "Ghibli"...
        'text': 'Votre question ?',
        'opts': ['Option A', 'Option B', 'Option C', 'Option D'],
        'ans':  'Option A',            # Doit être identique à une option
        'expl': 'Explication courte.'
    }

CATÉGORIES DISPONIBLES :
    Shōnen, Seinen, Isekai, Shōjo, Slice of Life, Mecha, Sport,
    Thriller, Fantasy, Science-Fiction, Super-pouvoirs, Comédie,
    Magical Girl, Historique, Studio Ghibli, Horreur, Mondial
"""

QUESTION_BANK = [

    # ════════════════ SHŌNEN ════════════════
    {
        'cat': 'Shōnen',
        'text': 'Dans quel animé trouve-t-on Naruto Uzumaki ?',
        'opts': ['Bleach', 'Naruto', 'Dragon Ball', 'One Piece'],
        'ans':  'Naruto',
        'expl': 'Naruto est le héros de la série éponyme de Masashi Kishimoto.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Quel est le nom du démon renard scellé dans Naruto Uzumaki ?',
        'opts': ['Shukaku', 'Kurama', 'Gyūki', 'Matatabi'],
        'ans':  'Kurama',
        'expl': 'Kurama (九喇嘛), le Neuf-Queues, est le Tailed Beast scellé en Naruto.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Quel fruit du démon possède Monkey D. Luffy dans One Piece ?',
        'opts': ['Mera Mera no Mi', 'Gomu Gomu no Mi', 'Gura Gura no Mi', 'Yami Yami no Mi'],
        'ans':  'Gomu Gomu no Mi',
        'expl': 'Le Gomu Gomu no Mi transforme le corps de Luffy en caoutchouc élastique.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans My Hero Academia, quel est le vrai nom du héros All Might ?',
        'opts': ['Izuku Midoriya', 'Toshinori Yagi', 'Shota Aizawa', 'Mirio Togata'],
        'ans':  'Toshinori Yagi',
        'expl': 'Le vrai nom du symbole de la paix est Toshinori Yagi.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans Demon Slayer, quelle est la respiration utilisée par Tanjiro initialement ?',
        'opts': ['Respiration du Feu', 'Respiration de la Bête', "Respiration de l'Eau", 'Respiration du Tonnerre'],
        'ans':  "Respiration de l'Eau",
        'expl': "Tanjiro apprend d'abord la Respiration de l'Eau auprès de Sakonji Urokodaki."
    },
    {
        'cat': 'Shōnen',
        'text': 'Combien de Hashira (Piliers) y a-t-il dans Demon Slayer ?',
        'opts': ['7', '8', '9', '10'],
        'ans':  '9',
        'expl': 'Il y a 9 Hashira dans le Corps des Pourfendeurs de Démons.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans Black Clover, quelle est la magie du protagoniste Asta ?',
        'opts': ['Magie de la foudre', 'Magie des ténèbres', "Magie de l'anti-magie", 'Magie du vent'],
        'ans':  "Magie de l'anti-magie",
        'expl': "Asta ne possède pas de magie mais peut l'annuler avec ses épées spéciales."
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans Chainsaw Man, comment s\'appelle le démon qui fusionne avec Denji ?',
        'opts': ['Aki', 'Power', 'Pochita', 'Makima'],
        'ans':  'Pochita',
        'expl': 'Pochita est le Chainsaw Devil qui fusionne son cœur avec celui de Denji.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans Hunter x Hunter, quel groupe d\'assassins élève Killua Zoldyck ?',
        'opts': ['La Brigade Fantôme', 'Les Zoldyck', 'Les Chimera Ants', 'La Mafia'],
        'ans':  'Les Zoldyck',
        'expl': 'La famille Zoldyck est la plus célèbre et redoutable famille d\'assassins du monde HxH.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans Fairy Tail, quelle est la magie signature de Natsu Dragneel ?',
        'opts': ['Magie de glace', 'Magie du feu du Tueur de Dragons', 'Magie de la foudre', 'Magie des ombres'],
        'ans':  'Magie du feu du Tueur de Dragons',
        'expl': 'Natsu est un Tueur de Dragons du Feu, élevé par le dragon Igneel.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans JoJo\'s Bizarre Adventure, quel est le Stand de Jotaro Kujo ?',
        'opts': ['The World', 'Star Platinum', 'Crazy Diamond', 'Gold Experience'],
        'ans':  'Star Platinum',
        'expl': 'Star Platinum est le Stand de Jotaro, capable de stopper le temps.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans Haikyuu!!, quel est le poste de Shoyo Hinata ?',
        'opts': ['Passeur', 'Libero', 'Ailier attaquant', 'Réceptionneur'],
        'ans':  'Ailier attaquant',
        'expl': 'Hinata est un ailier attaquant spécialisé dans l\'attaque rapide malgré sa petite taille.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans Dragon Ball Z, combien de boules de cristal y a-t-il ?',
        'opts': ['5', '6', '7', '8'],
        'ans':  '7',
        'expl': 'Il y a 7 Dragon Balls pour invoquer le dragon Shenron et exaucer un vœu.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans Assassination Classroom, quel est le surnom de l\'enseignant extraterrestre ?',
        'opts': ['Oni-sensei', 'Koro-sensei', 'Kara-sensei', 'Mori-sensei'],
        'ans':  'Koro-sensei',
        'expl': 'Koro-sensei (de "korosenai" = invincible) est le surnom de l\'octopode jaune.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans Bleach, comment s\'appelle le pouvoir spirituel utilisé par les Shinigami ?',
        'opts': ['Reiryoku', 'Reiatsu', 'Reishi', 'Kidō'],
        'ans':  'Reiatsu',
        'expl': 'Le Reiatsu est la pression spirituelle émise par les Shinigami et autres êtres spirituels.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans The Seven Deadly Sins, quelle est la capacité de Meliodas le Dragon\'s Sin of Wrath ?',
        'opts': ['Full Counter', 'Revenge Counter', 'Cruel Sun', 'Hellblaze'],
        'ans':  'Full Counter',
        'expl': 'Full Counter renvoie les attaques magiques avec une puissance multipliée.'
    },

    # ════════════════ SEINEN ════════════════
    {
        'cat': 'Seinen',
        'text': 'Dans Death Note, quel est le vrai nom du détective L ?',
        'opts': ['Lawliet', 'Ryuzaki', 'Beyond Birthday', 'Near'],
        'ans':  'Lawliet',
        'expl': 'L Lawliet est le vrai nom du mystérieux détective.'
    },
    {
        'cat': 'Seinen',
        'text': 'Dans Attack on Titan, quel est le nom du Titan Colossal au début de la série ?',
        'opts': ['Reiner Braun', 'Bertholdt Hoover', 'Annie Leonhart', 'Eren Yeager'],
        'ans':  'Bertholdt Hoover',
        'expl': 'Bertholdt Hoover était le Titan Colossal qui détruisit la porte de Shiganshina.'
    },
    {
        'cat': 'Seinen',
        'text': 'Dans Berserk, comment s\'appelle l\'épée géante de Guts ?',
        'opts': ['Excalibur', 'Dragonslayer', 'Balefire', 'Judgment'],
        'ans':  'Dragonslayer',
        'expl': 'La Dragonslayer est une énorme épée forgée pour tuer des dragons, brandissée par Guts.'
    },
    {
        'cat': 'Seinen',
        'text': 'Dans Monster, quel est le nom du "monstre" que le Dr. Tenma cherche ?',
        'opts': ['Roberto', 'Johan Liebert', 'Klaus', 'Wolf'],
        'ans':  'Johan Liebert',
        'expl': 'Johan Liebert est le sociopathe que le docteur Kenzo Tenma a sauvé enfant.'
    },
    {
        'cat': 'Seinen',
        'text': 'Dans Vagabond, quel célèbre samouraï est le personnage principal ?',
        'opts': ['Sasaki Kojiro', 'Oda Nobunaga', 'Miyamoto Musashi', 'Honda Tadakatsu'],
        'ans':  'Miyamoto Musashi',
        'expl': 'Vagabond retrace la vie romancée du légendaire samouraï Miyamoto Musashi.'
    },
    {
        'cat': 'Seinen',
        'text': 'Dans Tokyo Ghoul, qu\'est-ce qui caractérise principalement un Ghoul ?',
        'opts': ["Il peut voler", "Il se nourrit de chair humaine", "Il est immortel", "Il peut lire les esprits"],
        'ans':  'Il se nourrit de chair humaine',
        'expl': 'Les Ghouls sont des créatures humanoïdes qui ne peuvent se nourrir que de chair humaine.'
    },
    {
        'cat': 'Seinen',
        'text': 'Dans Vinland Saga, quel est le rêve ultime de Thorfinn ?',
        'opts': ['Venger son père', 'Devenir roi', 'Trouver Vinland', 'Devenir le meilleur guerrier'],
        'ans':  'Trouver Vinland',
        'expl': 'Thorfinn cherche à atteindre Vinland, une terre sans guerre ni esclavage.'
    },

    # ════════════════ ISEKAI ════════════════
    {
        'cat': 'Isekai',
        'text': 'Dans Re:Zero, quel est le pouvoir de Subaru Natsuki ?',
        'opts': ['Manipulation du temps', 'Retour par la mort', 'Invincibilité', 'Magie de glace'],
        'ans':  'Retour par la mort',
        'expl': 'Le "Return by Death" permet à Subaru de revivre depuis un checkpoint à chaque mort.'
    },
    {
        'cat': 'Isekai',
        'text': 'Dans Overlord, quel est le vrai nom d\'Ainz Ooal Gown dans le monde réel ?',
        'opts': ['Shiroe', 'Suzuki Satoru', 'Kirito', 'Subaru Natsuki'],
        'ans':  'Suzuki Satoru',
        'expl': 'Momonga / Ainz Ooal Gown s\'appelle Suzuki Satoru dans le monde réel.'
    },
    {
        'cat': 'Isekai',
        'text': 'Dans That Time I Got Reincarnated as a Slime, quel est le nom de la nation fondée par Rimuru ?',
        'opts': ['Jura Tempest Federation', 'Demon Lord Council', 'Blumund', 'Ingrassia'],
        'ans':  'Jura Tempest Federation',
        'expl': 'Rimuru fonde la Jura Tempest Federation dans la grande forêt de Jura.'
    },
    {
        'cat': 'Isekai',
        'text': 'Dans Konosuba, quelle déesse accompagne Kazuma dans l\'autre monde ?',
        'opts': ['Eris', 'Aqua', 'Darkness', 'Megumin'],
        'ans':  'Aqua',
        'expl': 'Aqua est la déesse de l\'eau contrainte d\'accompagner Kazuma.'
    },
    {
        'cat': 'Isekai',
        'text': 'Dans No Game No Life, sous quel nom le duo frère-sœur est-il connu ?',
        'opts': ['Blank / Shiro', 'Sora & Shiro', 'Kuuhaku', 'Tout cela à la fois'],
        'ans':  'Tout cela à la fois',
        'expl': 'Sora & Shiro forment le duo "Blanc" (Kuuhaku/Blank), la légende des jeux en ligne.'
    },
    {
        'cat': 'Isekai',
        'text': 'Dans Mushoku Tensei, quel est le nom de famille du protagoniste réincarné ?',
        'opts': ['Greyrat', 'Shirone', 'Fitts', 'Roxy'],
        'ans':  'Greyrat',
        'expl': 'Rudeus Greyrat est le nom du protagoniste après sa réincarnation dans une famille noble.'
    },
    {
        'cat': 'Isekai',
        'text': 'Dans The Rising of the Shield Hero, quel héros est accusé à tort au début ?',
        'opts': ['Ren Amaki', 'Motoyasu Kitamura', 'Naofumi Iwatani', 'Itsuki Kawasumi'],
        'ans':  'Naofumi Iwatani',
        'expl': 'Naofumi, le Héros du Bouclier, est faussement accusé de crime par Malty.'
    },

    # ════════════════ SHŌJO ════════════════
    {
        'cat': 'Shōjo',
        'text': 'Dans Sailor Moon, quel est le vrai nom de Sailor Moon ?',
        'opts': ['Ami Mizuno', 'Rei Hino', 'Usagi Tsukino', 'Makoto Kino'],
        'ans':  'Usagi Tsukino',
        'expl': 'Usagi Tsukino est l\'identité secrète de la guerrière Sailor Moon.'
    },
    {
        'cat': 'Shōjo',
        'text': 'Dans Fruits Basket, quelle est la malédiction des Sohma ?',
        'opts': [
            'Ils se transforment en animaux du calendrier chinois',
            'Ils ne vieillissent pas',
            'Ils lisent les esprits',
            'Ils sont maudits à mourir jeunes'
        ],
        'ans':  'Ils se transforment en animaux du calendrier chinois',
        'expl': 'Les membres de la famille Sohma se transforment en animaux du zodiaque chinois.'
    },
    {
        'cat': 'Shōjo',
        'text': 'Dans Your Lie in April, quel instrument joue Kousei Arima ?',
        'opts': ['Violon', 'Violoncelle', 'Piano', 'Flûte'],
        'ans':  'Piano',
        'expl': 'Kousei est un pianiste prodige qui a arrêté de jouer après la mort de sa mère.'
    },
    {
        'cat': 'Shōjo',
        'text': 'Dans Clannad, qui est l\'héroïne principale ?',
        'opts': ['Tomoyo', 'Kotomi', 'Nagisa Furukawa', 'Kyou'],
        'ans':  'Nagisa Furukawa',
        'expl': 'Nagisa est l\'héroïne principale de Clannad, amoureuse de Tomoya Okazaki.'
    },
    {
        'cat': 'Shōjo',
        'text': 'Dans Nana, les deux protagonistes partagent quel prénom ?',
        'opts': ['Hana', 'Nana', 'Mana', 'Rana'],
        'ans':  'Nana',
        'expl': 'Les deux héroïnes s\'appellent toutes deux Nana — Nana Osaki et Nana Komatsu.'
    },

    # ════════════════ SLICE OF LIFE ════════════════
    {
        'cat': 'Slice of Life',
        'text': 'Dans K-On!, combien de membres compte le Club de Musique Légère au complet ?',
        'opts': ['3', '4', '5', '6'],
        'ans':  '5',
        'expl': 'Le club compte 5 membres : Yui, Mio, Ritsu, Mugi et Azusa.'
    },
    {
        'cat': 'Slice of Life',
        'text': 'Dans Toradora, quel surnom Ryuji donne-t-il à Taiga ?',
        'opts': ['Kitsuné', 'Palmtop Tiger', 'Little Bear', 'Baby Dragon'],
        'ans':  'Palmtop Tiger',
        'expl': 'Ryuji appelle Taiga "Palmtop Tiger" : petite taille mais caractère féroce.'
    },
    {
        'cat': 'Slice of Life',
        'text': 'Dans Barakamon, quelle est la profession du personnage principal adulte ?',
        'opts': ['Artiste peintre', 'Calligraphe', 'Musicien', 'Poète'],
        'ans':  'Calligraphe',
        'expl': 'Seishuu Handa est un calligraphe qui s\'exile dans une île rurale pour se ressourcer.'
    },
    {
        'cat': 'Slice of Life',
        'text': 'Dans Ano Hi Mita Hana (AnoHana), quel est le vrai prénom du fantôme ?',
        'opts': ['Anaru', 'Tsurumi', 'Meiko Honma', 'Chiriko'],
        'ans':  'Meiko Honma',
        'expl': 'Meiko "Menma" Honma est le fantôme qui apparaît à Jinta pour exaucer son vœu.'
    },

    # ════════════════ MECHA ════════════════
    {
        'cat': 'Mecha',
        'text': 'Dans Neon Genesis Evangelion, comment s\'appelle l\'organisation qui pilote les EVA ?',
        'opts': ['NERV', 'SEELE', 'GEHIRN', 'WILLE'],
        'ans':  'NERV',
        'expl': 'NERV est l\'organisation para-militaire qui combat les Anges avec les Evangelions.'
    },
    {
        'cat': 'Mecha',
        'text': 'Dans Code Geass, quel est le pouvoir de Lelouch ?',
        'opts': ['Géass', 'Blaze', 'Refrain', 'Zero'],
        'ans':  'Géass',
        'expl': 'Le Géass de Lelouch lui permet de donner un ordre absolu à quelqu\'un une seule fois.'
    },
    {
        'cat': 'Mecha',
        'text': 'Dans Gurren Lagann, quel est le nom du mecha principal combiné ?',
        'opts': ['Gurren', 'Lagann', 'Gurren Lagann', 'Super Tengen Toppa'],
        'ans':  'Gurren Lagann',
        'expl': 'Gurren Lagann est formé de la fusion des mechas Gurren et Lagann.'
    },
    {
        'cat': 'Mecha',
        'text': 'Dans Darling in the FranXX, quel est le numéro de code de Hiro ?',
        'opts': ['002', '016', '666', '015'],
        'ans':  '016',
        'expl': 'Le numéro de code du protagoniste Hiro est le 016.'
    },

    # ════════════════ CLASSIQUE ════════════════
    {
        'cat': 'Classique',
        'text': 'Dans Dragon Ball original, qui est le premier maître de Goku enfant ?',
        'opts': ['Piccolo', 'Muten Roshi', 'Kami', 'Karin'],
        'ans':  'Muten Roshi',
        'expl': 'Muten Roshi (la Tortue Géniale) est le premier maître des arts martiaux de Goku.'
    },
    {
        'cat': 'Classique',
        'text': 'Dans Saint Seiya, quelle armure porte Seiya ?',
        'opts': ["Armure du Lion", "Armure du Pégase", "Armure du Cygne", "Armure du Dragon"],
        'ans':  'Armure du Pégase',
        'expl': 'Seiya est le Chevalier de Bronze du Pégase.'
    },
    {
        'cat': 'Classique',
        'text': 'Dans Captain Tsubasa, quelle est la technique de frappe signature de Tsubasa ?',
        'opts': ['Tornado Shot', 'Drive Shot', 'Overhead Kick', 'Sky Lab Hurricane'],
        'ans':  'Drive Shot',
        'expl': 'Le Drive Shot est la frappe surpuissante et technique signature de Tsubasa.'
    },
    {
        'cat': 'Classique',
        'text': 'Quel film Ghibli a remporté l\'Oscar du meilleur film d\'animation en 2003 ?',
        'opts': ['Princesse Mononoké', 'Mon Voisin Totoro', 'Le Voyage de Chihiro', 'Nausicaä'],
        'ans':  'Le Voyage de Chihiro',
        'expl': 'Le Voyage de Chihiro (Sen to Chihiro) a remporté l\'Oscar en 2003.'
    },
    {
        'cat': 'Classique',
        'text': 'Dans Lupin III, quel est le surnom du personnage féminin principale Fujiko ?',
        'opts': ['La femme mystère', 'The Viper', 'Femme Fatale', 'Mine-chan'],
        'ans':  'The Viper',
        'expl': 'Fujiko Mine est parfois surnommée The Viper en raison de sa nature imprévisible.'
    },

    # ════════════════ SPORT ════════════════
    {
        'cat': 'Sport',
        'text': 'Dans Slam Dunk, quel est le poste de Hanamichi Sakuragi ?',
        'opts': ['Meneur', 'Ailier fort', 'Pivot', 'Arrière'],
        'ans':  'Ailier fort',
        'expl': 'Sakuragi est un ailier fort malgré son inexpérience totale en début de série.'
    },
    {
        'cat': 'Sport',
        'text': 'Dans Eyeshield 21, quelle position joue Sena Kobayakawa ?',
        'opts': ['Quarterback', 'Running back', 'Wide receiver', 'Linebacker'],
        'ans':  'Running back',
        'expl': 'Sena est le running back du Devil Bats de Deimon, connu pour sa vitesse éclair.'
    },
    {
        'cat': 'Sport',
        'text': 'Dans Ping Pong the Animation, quel personnage est surnommé "Smile" ?',
        'opts': ['Peco', 'Kazama', 'Tsukimoto Makoto', 'Kong Wenge'],
        'ans':  'Tsukimoto Makoto',
        'expl': 'Tsukimoto Makoto est surnommé Smile car il ne sourit presque jamais.'
    },
    {
        'cat': 'Sport',
        'text': 'Dans Yuri on Ice, quelle est la nationalité du patineur Victor Nikiforov ?',
        'opts': ['Canadienne', 'Russe', 'Américaine', 'Japonaise'],
        'ans':  'Russe',
        'expl': 'Victor Nikiforov est un champion russe de patinage artistique.'
    },

    # ════════════════ THRILLER / PSYCHOLOGIQUE ════════════════
    {
        'cat': 'Thriller',
        'text': 'Dans Psycho-Pass, quel système mesure la tendance criminelle des individus ?',
        'opts': ['Sibyl System', 'Navi System', 'Justice Network', 'Crime Coefficient'],
        'ans':  'Sibyl System',
        'expl': 'Le Sibyl System évalue le potentiel criminel de chaque citoyen via le Crime Coefficient.'
    },
    {
        'cat': 'Thriller',
        'text': 'Dans Mirai Nikki (Future Diary), combien de propriétaires de journaux du futur participent au jeu ?',
        'opts': ['10', '11', '12', '13'],
        'ans':  '12',
        'expl': '12 détenteurs de journaux prophétiques s\'affrontent pour devenir dieu du temps.'
    },
    {
        'cat': 'Thriller',
        'text': 'Dans Higurashi When They Cry, dans quel village se passent les meurtres mystérieux ?',
        'opts': ['Hinamizawa', 'Oyashiro', 'Saitama', 'Rokkenjima'],
        'ans':  'Hinamizawa',
        'expl': 'Hinamizawa est le petit village isolé où se déroulent les événements tragiques.'
    },

    # ════════════════ FANTASY ════════════════
    {
        'cat': 'Fantasy',
        'text': 'Dans Fullmetal Alchemist Brotherhood, quelle règle fondamentale régit l\'alchimie ?',
        'opts': ['La règle du sang', "L'équivalence", 'La règle du métal', 'La règle des transmutations'],
        'ans':  "L'équivalence",
        'expl': "L'équivalence exige de sacrifier quelque chose d'égale valeur pour obtenir quelque chose."
    },
    {
        'cat': 'Fantasy',
        'text': 'Dans Made in Abyss, comment s\'appelle l\'instrument utilisé par Reg pour attaquer ?',
        'opts': ['Incinerator', 'Voirdhaum', 'Blaze Reap', 'Force Cannon'],
        'ans':  'Incinerator',
        'expl': 'L\'Incinerator est le puissant faisceau d\'énergie que Reg peut tirer de ses bras.'
    },
    {
        'cat': 'Fantasy',
        'text': 'Dans The Ancient Magus\' Bride, à quelle espèce appartient Elias Ainsworth ?',
        'opts': ['Fae', 'Demon', 'Ancient Mage', 'Thorn'],
        'ans':  'Ancient Mage',
        'expl': 'Elias Ainsworth est un Ancien Mage, être mystérieux mélange d\'homme et d\'autre chose.'
    },

    # ════════════════ ROMANCE ════════════════
    {
        'cat': 'Romance',
        'text': 'Dans Kaguya-sama: Love is War, quel est le conflit central de l\'histoire ?',
        'opts': [
            'Qui confessera son amour en premier',
            'Qui devient président du conseil',
            'Qui gagne les élections',
            'Qui réussit l\'examen'
        ],
        'ans':  'Qui confessera son amour en premier',
        'expl': 'Les deux protagonistes refusent d\'avouer leurs sentiments : confesseur = perdant.'
    },
    {
        'cat': 'Romance',
        'text': 'Dans Oregairu (My Teen Romantic Comedy SNAFU), dans quel club est Hachiman ?',
        'opts': ['Club de tennis', 'Service Club', 'Comité culturel', 'Club de débat'],
        'ans':  'Service Club',
        'expl': 'Hachiman est forcé de rejoindre le Service Club fondé par Yukino Yukinoshita.'
    },
    {
        'cat': 'Romance',
        'text': 'Dans Wotakoi, qu\'ont en commun les deux protagonistes principaux ?',
        'opts': [
            'Ils sont collègues',
            'Ce sont des otakus cachés',
            'Ils se connaissent depuis l\'enfance',
            'Tout cela à la fois'
        ],
        'ans':  'Tout cela à la fois',
        'expl': 'Narumi et Hirotaka sont d\'anciens amis d\'enfance, collègues et tous deux otakus cachés.'
    },

    # ════════════════ SCIENCE-FICTION ════════════════
    {
        'cat': 'Science-Fiction',
        'text': 'Dans Cowboy Bebop, quel est le nom du vaisseau de l\'équipe ?',
        'opts': ['Bebop', 'Swordfish', 'Red Tail', 'Hammerhead'],
        'ans':  'Bebop',
        'expl': 'Le Bebop est le vaisseau-mère de l\'équipe de chasseurs de primes.'
    },
    {
        'cat': 'Science-Fiction',
        'text': 'Dans Steins;Gate, quelle machine envoie des messages dans le passé ?',
        'opts': ['Phone Microwave', 'Time Leap Machine', 'D-Mail Device', 'SERN Terminal'],
        'ans':  'Phone Microwave',
        'expl': 'Le Phone Microwave (Name subject to change) envoie des D-Mails dans le passé.'
    },
    {
        'cat': 'Science-Fiction',
        'text': 'Dans Trigun, sur quelle planète désertique se déroule l\'histoire ?',
        'opts': ['Mars', 'Gunsmoke', 'Eden', 'New Texas'],
        'ans':  'Gunsmoke',
        'expl': 'L\'histoire se passe sur la planète Gunsmoke, un monde aride avec deux soleils.'
    },

    # ════════════════ SUPER-POUVOIRS ════════════════
    {
        'cat': 'Super-pouvoirs',
        'text': 'Dans One Punch Man, comment Saitama est-il devenu si puissant ?',
        'opts': [
            'Un entraînement secret',
            '100 pompes, 100 abdos, 10 km de course par jour pendant 3 ans',
            'Un fruit du démon',
            'Une mutation génétique'
        ],
        'ans':  '100 pompes, 100 abdos, 10 km de course par jour pendant 3 ans',
        'expl': 'Saitama s\'est entraîné si intensément qu\'il a perdu ses cheveux et est devenu invincible.'
    },
    {
        'cat': 'Super-pouvoirs',
        'text': 'Dans Mob Psycho 100, quel est le vrai prénom de Mob ?',
        'opts': ['Shigeo', 'Reigen', 'Dimple', 'Ritsu'],
        'ans':  'Shigeo',
        'expl': 'Mob s\'appelle Shigeo Kageyama, lycéen doté de pouvoirs psychiques phénoménaux.'
    },
    {
        'cat': 'Super-pouvoirs',
        'text': 'Dans Noragami, quel est le nom du Regalia (arme divine) de Yato ?',
        'opts': ['Kazuma', 'Yukine', 'Daikoku', 'Mayu'],
        'ans':  'Yukine',
        'expl': 'Yukine est le Regalia de Yato, qui se transforme en katana.'
    },
    {
        'cat': 'Super-pouvoirs',
        'text': 'Dans Akira, dans quelle ville se passe l\'histoire ?',
        'opts': ['Tokyo', 'Neo-Tokyo', 'Osaka', 'Akira City'],
        'ans':  'Neo-Tokyo',
        'expl': 'L\'histoire se déroule dans Neo-Tokyo, reconstruite après une explosion en 1988.'
    },

    # ════════════════ COMÉDIE ════════════════
    {
        'cat': 'Comédie',
        'text': 'Dans Gintama, dans quelle période historique revisitée se passe l\'histoire ?',
        'opts': ['Meiji', 'Edo', 'Heian', 'Sengoku'],
        'ans':  'Edo',
        'expl': 'Gintama se passe dans une version alternative de la période Edo envahie par des aliens.'
    },
    {
        'cat': 'Comédie',
        'text': 'Dans Saiki Kusuo no Psi-nan, quel est le désir principal de Saiki malgré ses pouvoirs ?',
        'opts': ['Dominer le monde', 'Avoir une vie normale', 'Trouver l\'amour', 'Devenir célèbre'],
        'ans':  'Avoir une vie normale',
        'expl': 'Saiki veut juste vivre une vie banale malgré ses incroyables pouvoirs psy.'
    },
    {
        'cat': 'Comédie',
        'text': 'Dans Grand Blue, dans quel club s\'inscrit le protagoniste à l\'université ?',
        'opts': ['Club de natation', 'Club de plongée', 'Club de cuisine', 'Club d\'aviron'],
        'ans':  'Club de plongée',
        'expl': 'Iori Kitahara s\'inscrit au club de plongée Peek-a-Boo, connu pour ses soirées alcoolisées.'
    },
    {
        'cat': 'Comédie',
        'text': 'Dans Gekkan Shoujo Nozaki-kun, quel est le travail secret de Nozaki ?',
        'opts': ['Musicien', 'Mangaka de shoujo', 'Acteur', 'Auteur de romans'],
        'ans':  'Mangaka de shoujo',
        'expl': 'Nozaki est un grand lycéen qui dessine secrètement un manga shōjo publié dans un magazine.'
    },

    # ════════════════ MAGICAL GIRL ════════════════
    {
        'cat': 'Magical Girl',
        'text': 'Dans Puella Magi Madoka Magica, quel souhait Madoka exauce-t-elle finalement ?',
        'opts': [
            'Revenir dans le temps',
            'Effacer les sorcières avant qu\'elles naissent',
            'Sauver Homura',
            'Devenir la plus puissante'
        ],
        'ans':  'Effacer les sorcières avant qu\'elles naissent',
        'expl': 'Madoka souhaite effacer toutes les sorcières avant leur naissance, devenant une loi cosmique.'
    },
    {
        'cat': 'Magical Girl',
        'text': 'Dans Cardcaptor Sakura, qui est le créateur des Cartes Clow ?',
        'opts': ['Yue', 'Kerberos', 'Clow Reed', 'Eriol'],
        'ans':  'Clow Reed',
        'expl': 'Clow Reed est le puissant sorcier qui a créé les 52 Cartes Clow.'
    },

    # ════════════════ HISTORIQUE ════════════════
    {
        'cat': 'Historique',
        'text': 'Dans Rurouni Kenshin, quel surnom Kenshin portait-il pendant la guerre de Bakumatsu ?',
        'opts': ['Battosai le Balafré', 'L\'Ombre Volante', 'Le Sabre Sanglant', 'L\'Assassin Silencieux'],
        'ans':  'Battosai le Balafré',
        'expl': 'Kenshin était craint sous le nom de Hitokiri Battosai, le tueur à l\'épée le plus redouté.'
    },
    {
        'cat': 'Historique',
        'text': 'Dans Demon Slayer, à quelle époque historique japonaise se déroule l\'histoire ?',
        'opts': ['Période Edo', 'Période Meiji', 'Époque Taisho', 'Période Shōwa'],
        'ans':  'Époque Taisho',
        'expl': 'Demon Slayer se déroule durant l\'ère Taisho (1912-1926) au Japon.'
    },
    {
        'cat': 'Historique',
        'text': 'Dans Dororo (2019), combien de parties du corps Hyakkimaru doit-il récupérer ?',
        'opts': ['12', '24', '36', '48'],
        'ans':  '48',
        'expl': 'Hyakkimaru est né sans 48 parties du corps, offertes aux démons par son père ambitieux.'
    },

    # ════════════════ STUDIO GHIBLI ════════════════
    {
        'cat': 'Studio Ghibli',
        'text': 'Dans Princesse Mononoké, comment s\'appelle le dieu de la forêt ?',
        'opts': ['Totoro', 'Yakkuru', 'Shishigami', 'Kodama'],
        'ans':  'Shishigami',
        'expl': 'Le Shishigami (Dieu-Cerf) est la divinité de la forêt dans Princesse Mononoké.'
    },
    {
        'cat': 'Studio Ghibli',
        'text': 'Dans Le Voyage de Chihiro, comment s\'appelle la propriétaire des bains ?',
        'opts': ['Yubaba', 'Zeniba', 'Lin', 'Kamaji'],
        'ans':  'Yubaba',
        'expl': 'Yubaba est la sorcière propriétaire des bains qui retient Chihiro sous son emprise.'
    },
    {
        'cat': 'Studio Ghibli',
        'text': 'Dans Kiki la Petite Sorcière, quel animal accompagne Kiki ?',
        'opts': ['Un renard', 'Un chat noir', 'Un hibou', 'Un lapin'],
        'ans':  'Un chat noir',
        'expl': 'Jiji est le chat noir parlant qui accompagne Kiki dans ses aventures.'
    },
    {
        'cat': 'Studio Ghibli',
        'text': 'Dans Le Château dans le Ciel, quel est le nom de la cité légendaire flottante ?',
        'opts': ['Laputa', 'Nausicaä', 'Pazu', 'Sheeta'],
        'ans':  'Laputa',
        'expl': 'Laputa est la cité légendaire flottante que Pazu et Sheeta cherchent à atteindre.'
    },

    # ════════════════ HORREUR ════════════════
    {
        'cat': 'Horreur',
        'text': 'Dans Junji Ito, quel est le sujet de la nouvelle "Uzumaki" ?',
        'opts': ['Les spirales', 'Les poupées', 'Les fantômes', 'Les miroirs'],
        'ans':  'Les spirales',
        'expl': 'Uzumaki raconte l\'obsession d\'une ville entière pour les spirales, avec des effets horrifiques.'
    },
    {
        'cat': 'Horreur',
        'text': 'Dans Hellsing Ultimate, quel est le vrai nom d\'Alucard ?',
        'opts': ['Vlad Tepes', 'Gabriel', 'Walter', 'Anderson'],
        'ans':  'Vlad Tepes',
        'expl': 'Alucard est Vlad l\'Empaleur (Alucard = Dracula à l\'envers).'
    },
    {
        'cat': 'Horreur',
        'text': 'Dans Shiki, que sont réellement les Shiki ?',
        'opts': ['Des zombies', 'Des vampires', 'Des démons', 'Des goules'],
        'ans':  'Des vampires',
        'expl': 'Les Shiki sont des vampires qui s\'installent dans un village rural japonais.'
    },

    # ════════════════ MONDIAL (Corée, Chine, etc.) ════════════════
    {
        'cat': 'Mondial',
        'text': 'Dans l\'animé coréen Tower of God, quel est le nom du protagoniste ?',
        'opts': ['Bam', 'Rachel', 'Khun', 'Rak'],
        'ans':  'Bam',
        'expl': 'Twenty-Fifth Bam entre dans la Tour pour retrouver Rachel, la seule personne qu\'il connaît.'
    },
    {
        'cat': 'Mondial',
        'text': 'Dans Solo Leveling (manhwa coréen), quel est le rang initial de Sung Jinwoo ?',
        'opts': ['Rang C', 'Rang E', 'Rang S', 'Rang D'],
        'ans':  'Rang E',
        'expl': 'Sung Jinwoo est le chasseur de rang E le plus faible au monde avant son éveil.'
    },
    {
        'cat': 'Mondial',
        'text': 'Dans Lookism (manhwa coréen), quel est le pouvoir particulier de Park Hyung Suk ?',
        'opts': [
            'Super force',
            'Changer de corps pendant son sommeil',
            'Lire les pensées',
            'Devenir invisible'
        ],
        'ans':  'Changer de corps pendant son sommeil',
        'expl': 'Park Hyung Suk peut changer de corps en dormant — son vrai corps et un beau corps.'
    },
    {
        'cat': 'Mondial',
        'text': 'Dans The King\'s Avatar (Quanzhi Gaoshou, manhua chinois), quel est le nom du personnage de Ye Xiu ?',
        'opts': ['Lord Grim', 'Battle Mage', 'Phantom Demon', 'One Autumn Leaf'],
        'ans':  'Lord Grim',
        'expl': 'Ye Xiu utilise Lord Grim, un personnage unique non-spécialisé de sa propre création.'
    },
    {
        'cat': 'Mondial',
        'text': 'Dans Noblesse (webtoon coréen), quel est le titre de Rai ?',
        'opts': ['Noble', 'Cadre', 'Noblesse', 'Lord'],
        'ans':  'Noblesse',
        'expl': 'Rai est le Noblesse, le plus puissant et noble des Nobles, éveillé après 820 ans de sommeil.'
    },

    # ════════════════ QUESTIONS BONUS ════════════════
    {
        'cat': 'Shōnen',
        'text': 'Dans Naruto, quel est le nom du groupe de ninjas d\'élite à 7 membres avec des épées légendaires ?',
        'opts': ['Les Akatsuki', 'Les Sept Ninjas Brumeux', 'Les ANBU', 'Les Sannin'],
        'ans':  'Les Sept Ninjas Brumeux',
        'expl': 'Les Seven Swordsmen of the Mist (Sept Ninjas Brumeux) manient 7 épées légendaires uniques.'
    },
    {
        'cat': 'Seinen',
        'text': 'Dans Parasyte (Kiseijuu), où la créature parasite s\'installe-t-elle chez Shinichi ?',
        'opts': ['Dans sa tête', 'Dans sa main droite', 'Dans son estomac', 'Dans son cœur'],
        'ans':  'Dans sa main droite',
        'expl': 'Migi ("droite") est le parasite qui a pris le contrôle de la main droite de Shinichi.'
    },
    {
        'cat': 'Isekai',
        'text': 'Dans Sword Art Online, combien de joueurs sont piégés dans Aincrad lors du début ?',
        'opts': ['1 000', '5 000', '10 000', '100 000'],
        'ans':  '10 000',
        'expl': '10 000 joueurs sont piégés dans le jeu SAO lors du lancement officiel.'
    },
    {
        'cat': 'Science-Fiction',
        'text': 'Dans Eureka Seven, quel phénomène atmosphérique les Ref Boarders surfent-ils ?',
        'opts': ['Trapars', 'Plasma Wave', 'Lifting', 'Coralian'],
        'ans':  'Trapars',
        'expl': 'Les Ref Boarders surfent les Trapars, des particules atmosphériques permettant de voler.'
    },
    {
        'cat': 'Magical Girl',
        'text': 'Dans Sailor Moon Crystal, quelle est la planète de Sailor Mars ?',
        'opts': ['Mercure', 'Vénus', 'Mars', 'Jupiter'],
        'ans':  'Mars',
        'expl': 'Rei Hino est Sailor Mars, la gardienne associée à la planète Mars et au feu.'
    },
    {
        'cat': 'Sport',
        'text': 'Dans Prince of Tennis, quel est le coup signature de Ryoma Echizen ?',
        'opts': ['Twist Serve', 'Muga no Kyouchi', 'Tsubame Gaeshi', 'Cyclone Smash'],
        'ans':  'Twist Serve',
        'expl': 'Le Twist Serve de Ryoma rebondit de façon imprévue vers la tête de l\'adversaire.'
    },
    {
        'cat': 'Thriller',
        'text': 'Dans Another, quel est le moyen d\'arrêter la calamité ?',
        'opts': ['Trouver le mort', 'Quitter la ville', 'Tuer le mort', 'Offrir un sacrifice'],
        'ans':  'Tuer le mort',
        'expl': 'La calamité s\'arrête en éliminant "le mort", le fantôme parmi les élèves de classe 3-3.'
    },
    {
        'cat': 'Fantasy',
        'text': 'Dans Black Clover, quel est le titre suprême dans le Clover Kingdom ?',
        'opts': ['Magic Knight Captain', 'Wizard King', 'Paladin', 'Magic Emperor'],
        'ans':  'Wizard King',
        'expl': 'Le Wizard King (Roi des Mages) est le titre le plus élevé dans le Clover Kingdom.'
    },
    {
        'cat': 'Classique',
        'text': 'Dans Astro Boy (Tetsuwan Atom), qui a créé Astro Boy ?',
        'opts': ['Dr. Ochanomizu', 'Dr. Tenma', 'Prof. Elephant', 'Red Boy'],
        'ans':  'Dr. Tenma',
        'expl': 'Dr. Tenma a créé Atom / Astro Boy à l\'image de son fils Tobio, décédé dans un accident.'
    },
    {
        'cat': 'Studio Ghibli',
        'text': 'Dans Nausicaä de la Vallée du Vent, comment s\'appelle la zone toxique ?',
        'opts': ['Fukai', 'Toxic Jungle', 'Sea of Corruption', 'Dead Forest'],
        'ans':  'Sea of Corruption',
        'expl': 'La Mer de la Corruption (Fukai en japonais) est la forêt toxique envahissante.'
    },
    {
        'cat': 'Shōnen',
        'text': 'Dans Jujutsu Kaisen, quel est le nom de la malédiction la plus puissante avalée par Yuji Itadori ?',
        'opts': ['Mahito', 'Jogo', 'Ryomen Sukuna', 'Hanami'],
        'ans':  'Ryomen Sukuna',
        'expl': 'Ryomen Sukuna est le Roi des Malédictions, dont les doigts sont avalés par Yuji.'
    },
    {
        'cat': 'Seinen',
        'text': 'Dans Oyasumi Punpun, pourquoi Punpun est-il représenté sous forme d\'oiseau abstrait ?',
        'opts': [
            'Sa liberté',
            'Son innocence perdue',
            'Son incapacité à communiquer et son détachement',
            'Sa relation avec le monde spirituel'
        ],
        'ans':  'Son incapacité à communiquer et son détachement',
        'expl': 'La forme abstraite de Punpun reflète son incapacité à interagir normalement avec les autres.'
    },
    {
        'cat': 'Romance',
        'text': 'Dans Tsuki ga Kirei, dans quelle activité le protagoniste Kotaro est-il passionné ?',
        'opts': ['Musique', 'Photographie', 'Écriture', 'Arts martiaux'],
        'ans':  'Écriture',
        'expl': 'Kotaro est passionné d\'écriture et aspire à devenir romancier.'
    },
    {
        'cat': 'Comédie',
        'text': 'Dans Danshi Koukousei no Nichijou, quelle est la particularité des activités des personnages ?',
        'opts': [
            'Ce sont des batailles épiques',
            'Ce sont des situations quotidiennes absurdes',
            'Ce sont des enquêtes policières',
            'Ce sont des compétitions sportives'
        ],
        'ans':  'Ce sont des situations quotidiennes absurdes',
        'expl': 'L\'animé met en scène des lycéens dans des situations du quotidien poussées à l\'absurde.'
    },
    {
        'cat': 'Mecha',
        'text': 'Dans Mobile Suit Gundam (premier opus), contre qui l\'armée de la Fédération combat-elle ?',
        'opts': ['Zeon', 'ZAFT', 'Titans', 'Celestial Being'],
        'ans':  'Zeon',
        'expl': 'La Principauté de Zeon s\'affronte à la Fédération de Terre dans la One Year War.'
    },
    {
        'cat': 'Horreur',
        'text': 'Dans Elfen Lied, comment s\'appellent les appendices invisibles des Diclonii ?',
        'opts': ['Vectors', 'Tendrils', 'Blades', 'Arms'],
        'ans':  'Vectors',
        'expl': 'Les Vectors sont les bras invisibles télékinétiques des Diclonii, capables de déchirer la matière.'
    },
    {
        'cat': 'Mondial',
        'text': 'Dans l\'animé coréen Noblesse, combien de siècles Rai a-t-il dormi ?',
        'opts': ['420 ans', '620 ans', '820 ans', '1020 ans'],
        'ans':  '820 ans',
        'expl': 'Rai s\'est réveillé après 820 ans de sommeil pour découvrir le monde moderne.'
    },
]
