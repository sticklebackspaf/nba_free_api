#!user/bin/env python3
import pandas as pd
import numpy as np

from cfg.games import game_cols, home_rnm, visitor_rnm
from cfg.stats import team_cols


def summary(full_json):

    df = pd.json_normalize(full_json)

    game_df = df[game_cols].drop_duplicates()
    game_df['game.home_team_win'] = (game_df['game.home_team_score'] >
                                     game_df['game.visitor_team_score']
                                     ).map(int)
    game_df['game.visitor_team_win'] = (game_df['game.visitor_team_score'] >
                                        game_df['game.home_team_score']
                                        ).map(int)

    home = game_df[['game.id', 'game.date']+[x for x in game_df.columns if 'home' in x]
                   ].rename(columns=home_rnm)
    visitor = game_df[['game.id', 'game.date']+[x for x in game_df.columns if 'visitor' in x]
                      ].rename(columns=visitor_rnm)

    gm_df_stck = pd.concat([home, visitor])

    gm_summ = gm_df_stck.groupby(['game.team_id'],
                                 as_index=False).agg(median_score=('game.team_score',
                                                                   np.median),
                                                     perc_win=('game.team_win',
                                                               np.mean))

    hm_gm_summ = game_df.groupby(['game.home_team_id'],
                                 as_index=False
                                 )\
        .agg(home_median_score=('game.home_team_score',
                                np.median
                                ),
             home_perc_win=('game.home_team_win',
                            np.mean)
             )

    vs_gm_summ = game_df.groupby(['game.visitor_team_id'],
                                 as_index=False
                                 )\
        .agg(visitor_median_score=('game.visitor_team_score',
                                   np.median
                                   ),
             visitor_perc_win=('game.visitor_team_win',
                               np.mean
                               )
             )

    gm_summ['perc_win'] = gm_summ['perc_win']*100
    hm_gm_summ['home_perc_win'] = hm_gm_summ['home_perc_win']*100
    vs_gm_summ['visitor_perc_win'] = vs_gm_summ['visitor_perc_win']*100

    hm_gm_summ.rename(
        columns={'game.home_team_id': 'game.team_id'}, inplace=True)
    vs_gm_summ.rename(
        columns={'game.visitor_team_id': 'game.team_id'}, inplace=True)

    all_sum = gm_summ.merge(hm_gm_summ,
                            on='game.team_id',
                            how='left')\
        .merge(vs_gm_summ,
               on='game.team_id',
               how='left')
    
    team_df = df[team_cols].drop_duplicates()

    name_mapper = dict(zip(team_df['team.id'], team_df['team.full_name']))

    all_sum['team_name'] = all_sum['game.team_id'].map(name_mapper)

    return all_sum


def player_summary(json_data):

    df = pd.json_normalize(json_data)

    df1 = df[df['pts'] > 0][['player.first_name', 'player.last_name', 'pts']]

    df1['full_name'] = df1['player.first_name'] + " " + df1['player.last_name']

    df1.sort_values(by='pts', ascending=False, inplace=True)

    return dict(zip(df1['full_name'], df1['pts'].astype(int)))
