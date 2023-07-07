# import os

# def makeCommits (days : int):
#     if days < 1:
#         os.system('git push')
#     else:
#         dates = f"{days} days ago"
#         with open('data.txt', 'a') as file:
#             file.write(f'{dates} <- this was the commit for the day!!\n')
        
#         # staging 
#         os.system('git add data.txt')

#         # commit 
#         os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')

#         return days * makeCommits(days - 1)

# makeCommits(1)


import os

def makeCommits(dates):
    for date in dates:
        with open('data.txt', 'a') as file:
            file.write(f'{date} <- this was the commit for the day!!\n')

        # staging
        os.system('git add data.txt')

        # commit
        os.system(f'git commit --date="{date}" -m "Commit for {date}"')

    # push the commits to the remote repository
    os.system('git push')

# Specify the desired commit dates in the format "YYYY-MM-DD"
commit_dates = ["2023-01-03", "2023-01-01", "2023-01-2"]

makeCommits(commit_dates)
