# field filters
game_kp_flds = ['id','date','home_team_score',
                   'visitor_team_score', 'home_team.full_name', 
                   'visitor_team.full_name'] 

game_cols = ['game.id', 'game.date', 
             'game.home_team_id', 'game.visitor_team_id', 
             'game.home_team_score', 'game.visitor_team_score']

# rename mappings for vertical stacking
home_rnm = {'game.home_team_id':'game.team_id',
            'game.home_team_score':'game.team_score',
            'game.home_team_win':'game.team_win'
            }
visitor_rnm = {'game.visitor_team_id':'game.team_id',
            'game.visitor_team_score':'game.team_score',
            'game.visitor_team_win':'game.team_win'
            }