import pandas as pd 

with open('all_matches.csv') as f:
    ipl_data = pd.read_csv(f, low_memory=False)
relevantColumns = ['match_id','season','start_date','venue','innings','ball','batting_team','bowling_team','striker','non_striker','bowler','runs_off_bat','extras','wides','noballs','byes','legbyes','penalty']
ipl_data = ipl_data[relevantColumns]
ipl_data['total_runs'] = ipl_data['runs_off_bat'] + ipl_data['extras']
ipl_data=ipl_data.drop(columns=['runs_off_bat','extras'])
ipl_data=ipl_data[ipl_data['ball']<=5.6]
ipl_data=ipl_data[ipl_data['innings']<=2]
ipl_data = ipl_data.groupby(['match_id','venue','innings','batting_team','bowling_team']).total_runs.sum()
ipl_data = ipl_data.reset_index()
ipl_data = ipl_data.drop(columns=['match_id'])
ipl_data['batting_team'].replace(['Rising Pune Supergiants','Delhi Daredevils','Kings XI Punjab'],['Rising Pune Supergiant','Delhi Capitals','Punjab Kings'],inplace=True)
ipl_data['bowling_team'].replace(['Rising Pune Supergiants','Delhi Daredevils','Kings XI Punjab'],['Rising Pune Supergiant','Delhi Capitals','Punjab Kings'],inplace=True)
ipl_data['venue'].replace(['Wankhede Stadium, Mumbai','M.Chinnaswamy Stadium','MA Chidambaram Stadium, Chepauk','MA Chidambaram Stadium, Chepauk, Chennai','Rajiv Gandhi International Stadium','Punjab Cricket Association IS Bindra Stadium, Mohali','Punjab Cricket Association IS Bindra Stadium','Sardar Patel Stadium, Motera',''],['Wankhede Stadium','M Chinnaswamy Stadium','MA Chidambaram Stadium','MA Chidambaram Stadium','Rajiv Gandhi International Stadium, Uppal','Punjab Cricket Association Stadium, Mohali','Punjab Cricket Association Stadium, Mohali','Narendra Modi Stadium','Arun Jaitley Stadium'],inplace=True)
ipl_data.to_csv('myPreprocessed.csv',index=False)