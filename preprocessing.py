import pandas as pd

# Load the data
with open(r'ipl_csv2\all_matches.csv') as f:
    ipl_data = pd.read_csv(f, low_memory=False)

# Select relevant columns
relevant_columns = [
    'match_id', 'season', 'start_date', 'venue', 'innings', 'ball', 
    'batting_team', 'bowling_team', 'striker', 'non_striker', 'bowler', 
    'runs_off_bat', 'extras', 'wides', 'noballs', 'byes', 'legbyes', 'penalty'
]
ipl_data = ipl_data[relevant_columns]

# Calculate total runs and drop unnecessary columns
ipl_data['total_runs'] = ipl_data['runs_off_bat'] + ipl_data['extras']
ipl_data = ipl_data.drop(columns=['runs_off_bat', 'extras'])

# Filter for balls up to the end of the 6th over and for the first two innings
ipl_data = ipl_data[ipl_data['ball'] <= 5.6]
ipl_data = ipl_data[ipl_data['innings'] <= 2]

# Group by necessary columns and sum the total runs1_
ipl_data = ipl_data.groupby(
    ['match_id', 'venue', 'innings', 'batting_team', 'bowling_team']
)['total_runs'].sum().reset_index()

# Drop the 'match_id' column
ipl_data = ipl_data.drop(columns=['match_id'])

# Normalize team names
team_name_replacements = {
    'Rising Pune Supergiants': 'Rising Pune Supergiant',
    'Delhi Daredevils': 'Delhi Capitals',
    'Kings XI Punjab': 'Punjab Kings'
}
ipl_data['batting_team'].replace(team_name_replacements, inplace=True)
ipl_data['bowling_team'].replace(team_name_replacements, inplace=True)

# Normalize venue names
venue_name_replacements = {
    'Wankhede Stadium, Mumbai': 'Wankhede Stadium',
    'M.Chinnaswamy Stadium': 'M Chinnaswamy Stadium',
    'MA Chidambaram Stadium, Chepauk': 'MA Chidambaram Stadium',
    'MA Chidambaram Stadium, Chepauk, Chennai': 'MA Chidambaram Stadium',
    'Rajiv Gandhi International Stadium': 'Rajiv Gandhi International Stadium, Uppal',
    'Punjab Cricket Association IS Bindra Stadium, Mohali': 'Punjab Cricket Association Stadium, Mohali',
    'Punjab Cricket Association IS Bindra Stadium': 'Punjab Cricket Association Stadium, Mohali',
    'Sardar Patel Stadium, Motera': 'Narendra Modi Stadium',
    '': 'Arun Jaitley Stadium'
}
ipl_data['venue'].replace(venue_name_replacements, inplace=True)

# Save the preprocessed data to a CSV file
ipl_data.to_csv('myPreprocessed.csv', index=False)
