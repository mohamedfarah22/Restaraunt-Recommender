suburbs = """3000,Melbourne,0.66
3002,East Melbourne,1.74
3003,West Melbourne,1.25
3005,World Trade Centre,1.58
3006,South Wharf,1.57
3006,Southbank,1.03
3008,Docklands,1.33
3050,Royal Melbourne Hospital,1.72
3053,Carlton,1.21
3053,Carlton South,1.21
3065,Fitzroy,1.82
3205,South Melbourne,1.99
3205,South Melbourne Dc,1.99
8012,Docklands,1.33
3010,University Of Melbourne,2.01
3051,Hotham Hill,2.29
3051,North Melbourne,2.29
3066,Collingwood,2.33
3066,Collingwood North,2.33
3004,Melbourne,3.39
3004,St Kilda Road Central,3.39
3052,Melbourne University,3.07
3052,Parkville,3.07
3054,Carlton North,3.05
3054,Princes Hill,3.05
3067,Abbotsford,3.30
3068,Clifton Hill,3.28
3068,Fitzroy North,3.28
3121,Burnley,3.54
3121,Cremorne,3.54
3121,Richmond,3.54
3121,Richmond East,3.54
3121,Richmond North,3.54
3121,Richmond South,3.54
3121,Victoria Gardens,3.54
3141,Chapel Street North,3.84
3141,Domain Road Po,3.84
3141,South Yarra,3.84
3206,Albert Park,3.75
3206,Middle Park,3.75
8008,St Kilda Road Central,3.39
3011,Footscray,4.91
3011,Seddon,4.91
3011,Seddon West,4.91
3031,Flemington,4.33
3031,Kensington,4.33
3057,Sumner,4.91
3121,Burnley North,4.11
3207,Garden City,4.44
3207,Port Melbourne,4.44
3055,Brunswick South,5.92
3055,Brunswick West,5.92
3055,Moonee Vale,5.92
3055,Moreland West,5.92
3056,Brunswick,5.34
3056,Brunswick Lower,5.34
3056,Brunswick North,5.34
3057,Brunswick East,5.07
3057,Lygon Street North,5.07
3070,Northcote,5.50
3070,Northcote South,5.50
3142,Hawksburn,5.83
3142,Toorak,5.83
3181,Prahran,5.32
3181,Prahran East,5.32
3181,Windsor,5.32
3182,St Kilda,5.86
3182,St Kilda South,5.86
3182,St Kilda West,5.86
3013,Yarraville,6.54
3013,Yarraville West,6.54
3039,Moonee Ponds,6.40
3078,Alphington,6.80
3078,Fairfield,6.80
3101,Cotham,6.49
3101,Kew,6.49
3122,Auburn South,6.00
3122,Glenferrie South,6.00
3122,Hawthorn,6.00
3122,Hawthorn North,6.00
3122,Hawthorn West,6.00
3183,Balaclava,6.86
3183,St Kilda East,6.86
3015,Newport,7.73
3015,South Kingsville,7.73
3015,Spotswood,7.73
3032,Ascot Vale,7.29
3032,Highpoint City,7.29
3032,Maribyrnong,7.29
3032,Travancore,7.29
3071,Thornbury,7.21
3123,Auburn,7.77
3123,Hawthorn East,7.77
3143,Armadale,7.01
3143,Armadale North,7.01
3144,Kooyong,7.87
3144,Malvern,7.87
3144,Malvern North,7.87
3184,Brighton Road,7.69
3184,Elwood,7.69
3012,Brooklyn,8.99
3012,Kingsville,8.99
3012,Kingsville West,8.99
3012,Maidstone,8.99
3012,Tottenham,8.99
3012,West Footscray,8.99
3016,Williamstown,8.56
3016,Williamstown North,8.56
3040,Aberfeldie,8.74
3040,Essendon,8.74
3040,Essendon West,8.74
3058,Batman,8.26
3058,Coburg,8.26
3058,Coburg North,8.26
3058,Merlynston,8.26
3058,Moreland,8.26
3072,Gilberton,8.81
3072,Northland Centre,8.81
3072,Preston,8.81
3072,Preston Lower,8.81
3072,Preston South,8.81
3072,Preston West,8.81
3072,Regent West,8.81
3072,Sylvester,8.81
3079,Ivanhoe,8.81
3079,Ivanhoe East,8.81
3079,Ivanhoe North,8.81
3102,Kew East,8.14
3161,Caulfield Junction,8.28
3161,Caulfield North,8.28
3044,Pascoe Vale,9.53
3044,Pascoe Vale South,9.53
3103,Balwyn,9.75
3103,Balwyn East,9.75
3103,Deepdene,9.03
3103,Deepdene Dc,9.75
3124,Camberwell,9.69
3124,Camberwell North,9.69
3124,Camberwell South,9.69
3124,Camberwell West,9.69
3124,Hartwell,9.69
3124,Middle Camberwell,9.69
3126,Camberwell East,9.99
3126,Canterbury,9.99
3146,Glen Iris,9.58
3185,Elsternwick,9.30
3185,Gardenvale,9.30,
3185,Ripponlea,9.30"""
suburbs_list = suburbs.split("\n")
print(suburbs_list)
new_suburbs_list = []
for suburb in suburbs_list:
   new_suburbs_list.append(suburb.split(","))
print(new_suburbs_list)
print(len(suburbs_list))