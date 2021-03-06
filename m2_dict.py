# Mappers for requests
mappers = {
    # Expenditures' mappers
    '2.3.0.1.0.0': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*4} dimension properties [RZPR].[Tab1],[Tab2],[Tab3] ON ROWS FROM [EXYR03.DB] WHERE ([BGLevels].[09-1],[Years].[*3],[Marks].[03-4])',
    '2.2.0.1.1.0': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*4} dimension properties [RZPR].[Tab1],[Tab2],[Tab3] ON ROWS FROM [EXYR03.DB] WHERE ([BGLevels].[09-1],[Years].[*3],[Marks].[03-3])',
    '2.3.0.1.1.0': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*4} dimension properties [RZPR].[Tab1],[Tab2],[Tab3] ON ROWS FROM [EXYR03.DB] WHERE ([BGLevels].[09-1],[Years].[*3],[MARKS].[03-4])',
    '2.5.0.0.1.0': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*4} dimension properties [RZPR].[Tab1],[Tab2],[Tab3] ON ROWS FROM [EXDO01.DB] WHERE ([BGLevels].[09-1],[Marks].[03-3])',
    '2.4.0.0.1.0': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*4} dimension properties [RZPR].[Tab1],[Tab2],[Tab3] ON ROWS FROM [EXDO01.DB] WHERE ([BGLevels].[09-1],[Marks].[03-4])',

    '2.3.0.1.0.1': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*4} dimension properties [RZPR].[Tab1],[Tab2],[Tab3] ON ROWS FROM [EXYR03.DB] WHERE ([BGLevels].[09-3],[Years].[*3],[Territories].[*5],[Marks].[03-4])',
    '2.2.0.1.1.1': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*4} dimension properties [RZPR].[Tab1],[Tab2],[Tab3] ON ROWS FROM [EXYR03.DB] WHERE ([BGLevels].[09-3],[Years].[*3],[Territories].[*5],[Marks].[03-3])',
    '2.3.0.1.1.1': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*4} dimension properties [RZPR].[Tab1],[Tab2],[Tab3] ON ROWS FROM [EXYR03.DB] WHERE ([BGLevels].[09-3],[Years].[*3],[Territories].[*5],[Marks].[03-4])',
    '2.5.0.0.1.1': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*4} dimension properties [RZPR].[Tab1],[Tab2],[Tab3] ON ROWS FROM [EXDO01.DB] WHERE ([BGLevels].[09-3],[Territories].[*5],[Marks].[03-3])',
    '2.4.0.0.1.1': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*4} dimension properties [RZPR].[Tab1],[Tab2],[Tab3] ON ROWS FROM [EXDO01.DB] WHERE ([BGLevels].[09-3],[Territories].[*5],[Marks].[03-4])',

    # Profits' mappers
    '3.0.0.1.0.0': 'SELECT {[Measures].[VALUE]} ON COLUMNS FROM [INYR03.DB] WHERE ([BGLevels].[09-1],[Years].[*3],[Marks].[03-2])',
    '3.2.0.1.0.0': 'SELECT {[Measures].[VALUE]} ON COLUMNS FROM [INYR03.DB] WHERE ([BGLevels].[09-1],[Years].[*3],[Marks].[03-1])',
    '3.0.1.1.0.0': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*2} dimension properties [KDGROUPS].[Tab1],[Tab2],[Tab3] ON ROWS FROM [INYR03.DB] WHERE ([BGLevels].[09-1],[Years].[*3],[Marks].[03-2])',
    '3.2.1.1.0.0': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*2} dimension properties [KDGROUPS].[Tab1],[Tab2],[Tab3] ON ROWS FROM [INYR03.DB] WHERE ([BGLevels].[09-1],[Years].[*3],[Marks].[03-1])',
    '3.2.0.0.0.0': 'SELECT {[Measures].[PLANONYEAR]} ON COLUMNS, {[BIFB].[25-1],[BIFB].[25-4],[BIFB].[25-5],[BIFB].[25-6],[BIFB].[25-7]} ON ROWS FROM [CLDO01.DB]',
    '3.2.1.0.0.0': 'SELECT {[Measures].[PLANONYEAR]} ON COLUMNS FROM [CLDO01.DB] WHERE ([BIFB].[*2])',
    '3.4.0.0.0.0': 'SELECT {[Measures].[FACTBGYEAR]} ON COLUMNS, {[BIFB].[25-1],[BIFB].[25-4],[BIFB].[25-5],[BIFB].[25-6],[BIFB].[25-7]} ON ROWS FROM [CLDO01.DB]',
    '3.4.1.0.0.0': 'SELECT {[Measures].[FACTBGYEAR]} ON COLUMNS FROM [CLDO01.DB] WHERE ([BIFB].[*2])',
    '3.0.0.1.0.1': 'SELECT {[Measures].[VALUE]} ON COLUMNS FROM [INYR03.DB] WHERE ([BGLevels].[09-3],[Years].[*3],[Marks].[03-2],[Territories].[*5])',
    '3.2.0.1.0.1': 'SELECT {[Measures].[VALUE]} ON COLUMNS FROM [INYR03.DB] WHERE ([BGLevels].[09-3],[Years].[*3],[Marks].[03-1],[Territories].[*5])',
    '3.2.0.0.0.1': 'SELECT {[Measures].[VALUE]} ON COLUMNS FROM [INDO01.DB] WHERE ([BGLevels].[09-3],[Marks].[03-1],[Territories].[*5])',
    '3.2.1.0.0.1': 'SELECT {[Measures].[VALUE]}  ON COLUMNS, {*2} dimension properties [KDGROUPS].[Tab1],[Tab2],[Tab3] ON ROWS FROM [INDO01.DB] WHERE ([BGLevels].[09-3],[Marks].[03-1],[Territories].[*5])',
    '3.4.0.0.0.1': 'SELECT {[Measures].[VALUE]} ON COLUMNS FROM [INDO01.DB] WHERE ([BGLevels].[09-3],[Marks].[03-2],[Territories].[*5])',
    '3.4.1.0.0.1': 'SELECT {[Measures].[VALUE]} ON COLUMNS, {*2} dimension properties [KDGROUPS].[Tab1],[Tab2],[Tab3] ON ROWS FROM [INDO01.DB] WHERE ([BGLevels].[09-3],[Marks].[03-2],[Territories].[*5])',

    # Deficit/surplus's mappers
    '4.4.0.0.0.0': 'SELECT {[Measures].[PLANONYEAR]} ON COLUMNS FROM [CLDO01.DB] WHERE ([BIFB].[25-20])',
    '4.2.0.0.0.0': 'SELECT {[Measures].[FACTBGYEAR]} ON COLUMNS FROM [CLDO01.DB] WHERE ([BIFB].[25-20])',
    '4.0.0.1.0.0': 'SELECT {[Measures].[VALUE]} ON COLUMNS FROM [FSYR01.DB] WHERE ([BGLevels].[09-1], [Marks].[03-6],[Years].[*3])',
    '4.0.0.1.0.1': 'SELECT {[Measures].[VALUE]} ON COLUMNS FROM [FSYR01.DB] WHERE ([BGLevels].[09-3],[Years].[*3],[Territories].[*5],[Marks].[03-6])',
    '4.2.0.0.0.1': 'SELECT {[Measures].[PLAN_ONYEAR]} ON COLUMNS FROM [CLDO02.DB] WHERE ([BGLevels].[09-3],[Marks].[03-6],[Territories].[*5])',
    '4.4.0.0.0.1': 'SELECT {[Measures].[FACT_BGYEAR]} ON COLUMNS FROM [CLDO02.DB] WHERE ([BGLevels].[09-3],[Marks].[03-6],[Territories].[*5])'
}

# Outer codes for substitution in MDX-query
param2 = {

    'налоговый': ('[KDGROUPS].[05-12], [KDGROUPS].[05-19], [KDGROUPS].[05-23], [KDGROUPS].[05-20], '
                  '[KDGROUPS].[05-21], [KDGROUPS].[05-22], [KDGROUPS].[05-33], [KDGROUPS].[05-34], '
                  '[KDGROUPS].[05-35], [KDGROUPS].[05-36]', '25-6'),
    'неналоговый': ('[KDGROUPS].[05-13], [KDGROUPS].[05-25], [KDGROUPS].[05-26], [KDGROUPS].[05-27], '
                    '[KDGROUPS].[05-28], [KDGROUPS].[05-29], [KDGROUPS].[05-30], [KDGROUPS].[05-31], '
                    '[KDGROUPS].[05-32], [KDGROUPS].[05-37]', '25-7')
}

sphere = {
    'null': '[RZPR], [RZPR].[14-848223],[RZPR].[14-413284],[RZPR].[14-850484],[RZPR].[14-848398],'
            '[RZPR].[14-848260],[RZPR].[14-1203414],[RZPR].[14-848266],[RZPR].[14-848294],'
            '[RZPR].[14-848302],[RZPR].[14-848345],[RZPR].[14-1203401],[RZPR].[14-413259],'
            '[RZPR].[14-413264],[RZPR].[14-413267],[RZPR].[14-1203208],[RZPR].[14-1203195]',

    # общегосударственные вопросы
    '2': '[RZPR].[14-848223],[RZPR].[14-413272],[RZPR].[14-342647],'
         '[RZPR].[14-413273],[RZPR].[14-413274],[RZPR].[14-413275],'
         '[RZPR].[14-413276],[RZPR].[14-413277],[RZPR].[14-413278],'
         '[RZPR].[14-413279],[RZPR].[14-848224],[RZPR].[14-413281],'
         '[RZPR].[14-413282],[RZPR].[14-848249]',

    # национальная оборона
    '3': '[RZPR].[14-413284],[RZPR].[14-413285],[RZPR].[14-413286],[RZPR].[14-413287],'
         '[RZPR].[14-413288],[RZPR].[14-413289],[RZPR].[14-413290],[RZPR].[14-413291]',

    # национальная безопасность и правоохранительная деятельность
    '4': '[RZPR].[14-850484],[RZPR].[14-413293],[RZPR].[14-413294],[RZPR].[14-853732],'
         '[RZPR].[14-413296],[RZPR].[14-855436],[RZPR].[14-854333],[RZPR].[14-854342],'
         '[RZPR].[14-854482],[RZPR].[14-108129],[RZPR].[14-852920],[RZPR].[14-850760],'
         '[RZPR].[14-1203368],[RZPR].[14-853005],[RZPR].[14-850485]',

    # национальная экономика
    '5': '[RZPR].[14-848398],[RZPR].[14-848399],[RZPR].[14-1203160],'
         '[RZPR].[14-850771],[RZPR].[14-857652],[RZPR].[14-850172],'
         '[RZPR].[14-849065],[RZPR].[14-849070],[RZPR].[14-851151],'
         '[RZPR].[14-1203167],[RZPR].[14-1203168],[RZPR].[14-1203169],'
         '[RZPR].[14-848501]',

    # жилищно-коммунальное хозяйство
    '6': '[RZPR].[14-848260],[RZPR].[14-848261],[RZPR].[14-850428],'
         '[RZPR].[14-1203187],[RZPR].[14-881303],[RZPR].[14-849768]',

    # охрана окружающей среды
    '7': '[RZPR].[14-1203414],[RZPR].[14-1203191],[RZPR].[14-872910],'
         '[RZPR].[14-872714],[RZPR].[14-848836]',

    # образование
    '8': '[RZPR].[14-848266],[RZPR].[14-848267],[RZPR].[14-849320],'
         '[RZPR].[14-343261],[RZPR].[14-848274],[RZPR].[14-849333],'
         '[RZPR].[14-873227],[RZPR].[14-850050],[RZPR].[14-849520],'
         '[RZPR].[14-849303]',

    # культура, кинематография
    '9': '[RZPR].[14-848294],[RZPR].[14-848295],[RZPR].[14-873473],'
         '[RZPR].[14-873499],[RZPR].[14-873512]',

    # здравоохранение
    '10': '[RZPR].[14-848302],[RZPR].[14-872659],[RZPR].[14-848317],'
          '[RZPR].[14-343881],[RZPR].[14-108717],[RZPR].[14-349151],'
          '[RZPR].[14-349155],[RZPR].[14-349159],[RZPR].[14-849621],'
          '[RZPR].[14-349163]',

    # социальная политика
    '11': '[RZPR].[14-848345],[RZPR].[14-349188],[RZPR].[14-349196],'
          '[RZPR].[14-848346],[RZPR].[14-874840],[RZPR].[14-851908],'
          '[RZPR].[14-849729]',

    # физическая культура и спорт
    '12': '[RZPR].[14-1203401],[RZPR].[14-850455],[RZPR].[14-866083],'
          '[RZPR].[14-850952],[RZPR].[14-413257],[RZPR].[14-413258],'
          '[RZPR].[14-413259],[RZPR].[14-413260],[RZPR].[14-851607],'
          '[RZPR].[14-413262],[RZPR].[14-413263],[RZPR].[14-413264],'
          '[RZPR].[14-413265],[RZPR].[14-413266],[RZPR].[14-413267],'
          '[RZPR].[14-413268],[RZPR].[14-413269],[RZPR].[14-413270]'
}

places = {
    'адыгея': '67646',
    'алания': '67652',
    'алтай': '67684',
    'алтайский': '67688',
    'амурская': '67708',
    'архангельская': '67678',
    'астраханская': '67645',
    'байконур': '93015',
    'башкортостан': '67655',
    'белгородская': '67721',
    'брянская': '67719',
    'бурятия': '67691',
    'владимирская': '67716',
    'волгоградская': '67647',
    'вологодская': '67674',
    'воронежская': '67723',
    'дагестан': '67643',
    'дальневосточный': '17698',
    'еврейская': '67705',
    'забайкальский': '67729',
    'ивановская': '67722',
    'ингушетия': '67649',
    'иркутская': '67682',
    'кабардино-балкарская': '67651',
    'калининградская': '67670',
    'калмыкия': '67648',
    'калужская': '67712',
    'камчатский': '67728',
    'карачаево-черкесская': '67638',
    'карелия': '67677',
    'кемеровская': '67689',
    'кировская': '67663',
    'коми': '67673',
    'костромская': '67714',
    'краснодарский': '67644',
    'красноярский': '67694',
    'крым': '93010',
    'крымский': '91128',
    'курганская': '67699',
    'курская': '67710',
    'ленинградская': '67676',
    'липецкая': '67711',
    'магаданская': '67703',
    'марий эл': '67666',
    'мордовия': '67662',
    'москва': '67724',
    'московская': '67709',
    'мурманская': '67669',
    'ненецкий': '67672',
    'нижегородская': '67656',
    'новгородская': '67675',
    'новосибирская': '67690',
    'омская': '67687',
    'оренбургская': '67659',
    'орловская': '67726',
    'осетия': '67652',
    'пензенская': '67667',
    'пермский': '67727',
    'приволжский': '3417',
    'приморский': '67706',
    'псковская': '67671',
    'российская федерация': '2',
    'россия': '2',
    'ростовская': '67653',
    'рф': '2',
    'рязанская': '67720',
    'самарская': '67658',
    'санкт-петербург': '67639',
    'саратовская': '67665',
    'саха': '67642',
    'сахалинская': '67704',
    'свердловская': '67698',
    'севастополь': '93011',
    'северо-западный': '10249',
    'северо-кавказский': '24604',
    'сибирский': '12097',
    'смоленская': '67718',
    'ставропольский': '67654',
    'тамбовская': '67725',
    'татарстан': '67661',
    'тверская': '67717',
    'томская': '67692',
    'тульская': '67715',
    'тыва': '67683',
    'тюменская': '67697',
    'удмуртская': '67668',
    'ульяновская': '67660',
    'уральский': '16333',
    'хабаровский': '67707',
    'хакасия': '67681',
    'ханты-мансийский': '67695',
    'центральный': '19099',
    'челябинская': '67700',
    'чеченская': '67650',
    'чувашия': '67664',
    'чувашская': '67664',
    'чукотский': '67640',
    'югра': '67695',
    'южный': '3',
    'якутия': '67642',
    'ямало-ненецкий': '67696',
    'ярославская': '67713'
}

places_cld = {
    'адыгея': '1451',
    'алания': '2507',
    'алтай': '12792',
    'алтайский': '13781',
    'амурская': '18776',
    'архангельская': '11867',
    'астраханская': '1176',
    'байконур': '93015',
    'башкортостан': '3418',
    'белгородская': '22729',
    'брянская': '22143',
    'бурятия': '15295',
    'владимирская': '21258',
    'волгоградская': '1512',
    'вологодская': '10809',
    'воронежская': '23249',
    'дагестан': '4',
    'дальневосточный': '17698',
    'еврейская': '18317',
    'забайкальский': '24584',
    'ивановская': '23067',
    'ингушетия': '2135',
    'иркутская': '12232',
    'кабардино-балкарская': '2374',
    'калининградская': '10293',
    'калмыкия': '2006',
    'калужская': '20350',
    'камчатский': '24543',
    'карачаево-черкесская': '1354',
    'карелия': '11627',
    'кемеровская': '14580',
    'кировская': '7726',
    'коми': '10597',
    'костромская': '20774',
    'краснодарский': '749',
    'красноярский': '15777',
    'крым': '91129',
    'крымский': ' 91128',
    'курганская': '16921',
    'курская': '19479',
    'ленинградская': '11404',
    'липецкая': '20018',
    'магаданская': '18239',
    'марий эл': '9301',
    'мордовия': '7265',
    'москва': '23783',
    'московская': '19100',
    'мурманская': '10250',
    'ненецкий': '10575',
    'нижегородская': '4439',
    'новгородская': '11182',
    'новосибирская': '14804',
    'омская': '13356',
    'оренбургская': '5483',
    'орловская': '24262',
    'осетия': '2507',
    'пензенская': '9475',
    'пермский': '24541',
    'приволжский': '3417',
    'приморский': '18354',
    'псковская': '10330',
    'российская федерация': '2',
    'россия': '2',
    'рф': '2',
    'ростовская': '2622',
    'рязанская': '22433',
    'самарская': '5140',
    'санкт-петербург': '11755',
    'саратовская': '8860',
    'саха': '17699',
    'сахалинская': '18294',
    'свердловская': '16827',
    'севастополь': '91139',
    'северо-западный': '10249',
    'северо-кавказский': '24604',
    'сибирский': '12097',
    'смоленская': '21792',
    'ставропольский': '3086',
    'тамбовская': '23909',
    'татарстан': '6265',
    'тверская': '21386',
    'томская': '15593',
    'тульская': '21078',
    'тыва': '12649',
    'тюменская': '16507',
    'удмуртская': '9907',
    'ульяновская': '6097',
    'уральский': '16333',
    'хабаровский': '18540',
    'хакасия': '12130',
    'ханты-мансийский': '16334',
    'центральный': '19099',
    'челябинская': '17380',
    'чеченская': '2136',
    'чувашская': '8208',
    'чувашия': '8208',
    'чукотский': '18184',
    'югра': '16334',
    'южный': '3',
    'якутия': '17699',
    'ямало-ненецкий': '16448',
    'ярославская': '20670'
}

