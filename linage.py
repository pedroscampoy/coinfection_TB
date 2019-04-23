
def get_lineage_coll(dict_positions):
    list_positions = [615938,4404247,3021283,3216553,2622402,1491275,3479545,3470377,497491,1881090,2505085,797736,4248115,3836274,346693,3273107,1084911,3722702,1237818,2874344,931123,62657,514245,1850119,541048,4229087,891756,107794,2411730,783601,1487796,1455780,764995,615614,4316114,3388166,403364,3977226,4398141,1132368,1502120,4307886,4151558,355181,2694560,4246508,1719757,3466426,4260268,874787,1501468,4125058,3570528,2875883,4249732,3836739,1759252,1799921,1816587,1137518,2831482,1882180
    ]

    for position in list_positions:
        if position not in dict_positions:
            dict_positions[position] = "N"

    lineage  = 'unknown'
    if(dict_positions[931123] == "T"):                          # wt allel L4 Euro-American
        if(dict_positions[1759252] == "G"):                      # wt allel L4.9 Euro-American (H37Rv-like)
            lineage = '4.9'
        elif(dict_positions[1759252] == "T"):                   # L4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8
            if(dict_positions[62657] == "A"):                     # L4.1 Euro-American
                if(dict_positions[514245] == "T"):                 # L4.1.1 Euro-American (X-type)
                    if(dict_positions[1850119] == "T"):             # L4.1.1.1 Euro-American (X-type)
                        lineage = '4.1.1.1'
                    elif(dict_positions[541048] == "G"):           # L4.1.1.2 Euro-American (X-type)
                        lineage = '4.1.1.2'
                    elif(dict_positions[4229087] == "T"):          # L4.1.1.3 Euro-American (X-type)
                        lineage = '4.1.1.3'
                    else: 
                        lineage = '4.1.1'
                elif(dict_positions[891756] == "G"):              # L4.1.2 Euro-American
                    if(dict_positions[107794] == "T"):              # L4.1.2.1 Euro-American (Haarlem)
                        lineage = '4.1.2.1'
                    else: 
                        lineage = '4.1.2'
                else: 
                    lineage = '4.1'
            elif(dict_positions[2411730] == "C"):                # L4.2  Euro-American
                if(dict_positions[783601] == "C"):                 # L4.2.1 Euro-American (Ural)
                    lineage = '4.2.1'
                elif(dict_positions[1487796] == "A"):             # L4.2.2  Euro-American
                    if(dict_positions[1455780] == "C"):             # L4.2.2.1 Euro-American (TUR)
                        lineage = '4.2.2.1'
                    else: 
                        lineage = '4.2.2'
                else: 
                    lineage = '4.2'
            elif(dict_positions[764995] == "G"):                 # L4.3 Euro-American (LAM)
                if(dict_positions[615614] == "A"):                 # L4.3.1 Euro-American (LAM)
                    lineage = '4.3.1'
                elif(dict_positions[4316114] == "A"):             # L4.3.2 Euro-American (LAM)
                    if(dict_positions[3388166] == "G"):             # L4.3.2.1 Euro-American (LAM)
                        lineage = '4.3.2.1'
                    else: 
                        lineage = '4.3.2'
                elif(dict_positions[403364] == "A"):              # L4.3.3 Euro-American (LAM)
                    lineage = '4.3.3'
                elif(dict_positions[3977226] == "A"):             # L4.3.4 Euro-American (LAM)
                    if(dict_positions[4398141] == "A"):             # L4.3.4.1 Euro-American (LAM)
                        lineage = '4.3.4.1'
                    elif(dict_positions[1132368] == "T"):          # L4.3.4.2 Euro-American (LAM)
                        if(dict_positions[1502120] == "A"):          # L4.3.4.2.1 Euro-American (LAM)
                            lineage = '4.3.4.2.1'
                        else: 
                            lineage = '4.3.4.2'
                    else: 
                        lineage = '4.3.4'
                else: 
                    lineage = '4.3'
            elif(dict_positions[4307886] == "A"):                # L4.4 Euro-American
                if(dict_positions[4151558] == "A"):                # L4.4.1 Euro-American
                    if(dict_positions[355181] == "A"):              # L4.4.1.1 Euro-American (S-type)
                        lineage = '4.4.1.1'
                    elif(dict_positions[2694560] == "C"):          # L4.4.1.2 Euro-American
                        lineage = '4.4.1.2'
                    else: 
                        lineage = '4.4.1'
                elif(dict_positions[4246508] == "A"):             # L4.4.2 Euro-American
                    lineage = '4.4.2'
                else: 
                    lineage = '4.4'
            elif(dict_positions[1719757] == "T"):                # L4.5 Euro-American
                lineage = '4.5'
            elif(dict_positions[3466426] == "A"):                # L4.6 Euro-American
                if(dict_positions[4260268] == "C"):                # L4.6.1 Euro-American (Uganda)
                    if(dict_positions[874787] == "A"):              # L4.6.1.1 Euro-American (Uganda)
                        lineage = '4.6.1.1'
                    elif(dict_positions[1501468] == "C"):          # L4.6.1.2 Euro-American (Uganda)
                        lineage = '4.6.1.2'
                    else: 
                        lineage = '4.6.1'
                elif(dict_positions[4125058] == "C"):             # L4.6.2 Euro-American
                    if(dict_positions[3570528] == "G"):             # L4.6.2.1 Euro-American
                        lineage = '4.6.2.1'
                    elif(dict_positions[2875883] == "T"):          # L4.6.2.2 Euro-American (Cameroon)
                        lineage = '4.6.2.2'
                    else: 
                        lineage = '4.6.2'
                else: 
                    lineage = '4.6'
            elif(dict_positions[4249732] == "G"):                # L4.7 Euro-American (mainly T)
                lineage = '4.7'
            elif(dict_positions[3836739] == "A"):                # L4.8 Euro-American (mainly T)
                lineage = '4.8'
        else: 
            lineage = '4'
    else:                                                       # L1,2,3,5,6,7,BOV,BOV_AFRI
        if(dict_positions[615938] == "A"):                       # L1 Indo-Oceanic
            if(dict_positions[4404247] == "A"):                   # L1.1 Indo-Oceanic
                if(dict_positions[3021283] == "A"):                # L1.1.1 Indo-Oceanic
                    if(dict_positions[3216553] == "A"):             # L1.1.1.1 Indo-Oceanic
                        lineage = '1.1.1.1'
                    else: 
                        lineage = '1.1.1'
                elif(dict_positions[2622402] == "A"):             # L1.1.2 Indo-Oceanic
                    lineage = '1.1.2'
                elif(dict_positions[1491275] == "A"):             # L1.1.3 Indo-Oceanic
                    lineage = '1.1.3'
                else: 
                    lineage = '1.1'
            elif(dict_positions[3479545] == "A"):                # L1.2.1 Indo-Oceanic
                lineage = '1.2.1'
            elif(dict_positions[3470377] == "T"):                # L1.2.2 Indo-Oceanic
                lineage = '1.2.2'
            else: 
                lineage = '1'
        elif(dict_positions[497491] == "A"):                    # L2 East-Asian
            if(dict_positions[1881090] == "T"): 
                lineage = '2.1'                                  # L2.1 East-Asian (non-Beijing)
            elif(dict_positions[2505085] == "A"):                # L2.2 East-Asian (Beijing)
                if(dict_positions[797736] == "T"):                 # L2.2.1 East-Asian (Beijing)
                    if(dict_positions[4248115] == "T"):             # L2.2.1.1 East-Asian (Beijing)
                        lineage = '2.2.1.1'
                    elif(dict_positions[3836274] == "A"):          # L2.2.1.2 East-Asian (Beijing)
                        lineage = '2.2.1.2'
                    else: 
                        lineage = '2.2.1'
                elif(dict_positions[346693] == "T"):              # L2.2.2 East-Asian (Beijing)
                    lineage = '2.2.2'
                else: 
                    lineage = '2.2'
            else: 
                lineage = '2'
        elif(dict_positions[3273107] == "A"):                   # L3 East-African-Indian
            if(dict_positions[1084911] == "A"):                   # L3.1.1 East-African-Indian
                lineage = '3.1.1'
            elif(dict_positions[3722702] == "C"):                # L3.1.2 East-African-Indian
                if(dict_positions[1237818] == "G"):                # L3.1.2.1 East-African-Indian
                    lineage = '3.1.2.1'
                elif(dict_positions[2874344] == "A"):             # L3.1.2.2 East-African-Indian
                    lineage = '3.1.2.2'
                else: 
                    lineage = '3.1.2'
            else: 
                lineage = '3'
        elif(dict_positions[1799921] == "A"):                   # L5 West-Africa 1
            lineage = '5'
        elif(dict_positions[1816587] == "G"):                   # L6 West-Africa 2
            lineage = '6'
        elif(dict_positions[1137518] == "A"):                   # L7 Lineage 7
            lineage = '7'
        elif(dict_positions[2831482] == "G"):                   # LBOV M. bovis
            lineage = 'BOV'

    print("This samples belongs to linage " + lineage)
    return(lineage)


def get_lineage_homolka(dict_positions):
    species = 'unknown'
    lineage = 'unknown'
    if(dict_positions[648856] == 'C'):                          # not Euro American
        if(dict_positions[648756] == 'T'):                       # M. africanum 1a/1b
            if(dict_positions[2053726] == 'T'):                   # M. africanum 1b
                species    = 'M. africanum'
                lineage    = 'West African 1b'
            else:                                                 # M. africanum 1a ???
                species    = 'M. africanum'
                lineage    = 'West African 1a'                   # spoke with susanne, if 1b SNP is not there, it's 1a
        elif(dict_positions[649345] == 'T'):                    # EAI
            if(dict_positions[1128814] == 'A'):                   # EAI Manila
                species    = 'M. tuberculosis'
                lineage    = 'EAI Manila'
            else:                                                 # EAI
                species    = 'M. tuberculosis'
                lineage    = 'EAI'
        elif(dict_positions[649585] == 'A'):                    # M. caprae
            species       = 'M. caprae'
        elif(dict_positions[649601] == 'T'):                    # M. canettii
            species       = 'M. canettii'
        else:                                                    # Rv0557 is WT
            if(dict_positions[157129] == 'T'):                    # Delhi/CAS
                species    = 'M. tuberculosis'
                lineage    = 'Delhi-CAS'
            elif(dict_positions[1128825] == 'T'):                # M. microti or M. pinnipedii
                species    = 'M. microti or M. pinnipedii'
                if(dict_positions[1473079] == 'A'):                # M. microti (not SH)
                species = 'M. microti'
                elif((dict_positions[1674520] == 'T'): or (dict_positions[1473094] == 'C'):)     # M. pinnipedii (not SH)
                species = 'M. pinnipedii'
            elif(dict_positions[1129160] == 'T'):       # M. bovis
                species    = 'M. bovis'
            elif(dict_positions[2053762] == 'T'):       # M. africanum 2
                species    = 'M. africanum'
                lineage    = 'West African 2'
            elif(dict_positions[2955957] == 'C'):       # Beijing
                species    = 'M. tuberculosis'
                lineage    = 'Beijing'
        else:                                              # Euro American
            if(dict_positions[648990] == 'C'):              # Haarlem
                species       = 'M. tuberculosis'
                lineage       = 'Haarlem'
            elif(dict_positions[648992] == 'G'):           # S-type
                species       = 'M. tuberculosis'
                lineage       = 'S-type'
            elif(dict_positions[649067] == 'G'):           # Cameroon
                species       = 'M. tuberculosis'
                lineage       = 'Cameroon'
            else:                                           # Rv0557 is WT
                if(dict_positions[157292] == 'T'):           # LAM
                    species    = 'M. tuberculosis'
                    lineage    = 'LAM'
                elif(dict_positions[1129165] == 'A'):       # TUR
                    species    = 'M. tuberculosis'
                    lineage    = 'TUR'
                elif(dict_positions[2053454] == 'A'):       # Ural
                    species    = 'M. tuberculosis'
                    lineage    = 'Ural'
                elif(dict_positions[2956731] == 'T'):       # Ghana
                    species    = 'M. tuberculosis'
                    lineage    = 'Ghana'
                elif(dict_positions[7539] == 'G'):          # Uganda (not SH)
                    species    = 'M. tuberculosis'
                    lineage    = 'Uganda'
    if(species eq 'unknown'): 
        if(dict_positions[1816848] == 'T'): 
            species       = 'M. africanum or M. caprae or M. microti or M. pinipedii'
        elif(dict_positions[2955233] == 'T'): 
            species       = 'M. africanum or M.bovis or M. canetii or M. caprae or M. microti or M. pinipedii or M. tuberculosis EAI'
        elif(dict_positions[2955233] != 'T'):) 
            species       = 'M. tuberculosis'
            lineage       = 'Clade 1'
   
   return species,lineage

#get_lineage_coll(dict_pos)