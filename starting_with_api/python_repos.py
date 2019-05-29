import requests
import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

# make an API call and store the response to a variable
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# store API response in a variable
# .json() will return a dictionary which contains data in the API returned data
response_dict = r.json()

# process results
print(response_dict.keys())  # to find out the what keys are in the response package
print("Total repositories:", response_dict['total_count'])
print("Repositories returned:", len(response_dict['items']))
print("Incomplete results:", response_dict['incomplete_results'])

# store the items into a list, it is a list of dictionaries
repo_dicts = response_dict['items']

# collect selected information of each repository
repo_names, repo_stars, repo_urls, repo_descriptions = [], [], [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    repo_stars.append(int(repo_dict['stargazers_count']))
    repo_urls.append(repo_dict['html_url'])
    repo_descriptions.append(repo_dict['description'])

# visualize
my_style = LS('#333366', base_style=LCS)

# create a configuration object, which serves as "configuration" repository
my_config = pygal.Config()
my_config.x_label_rotation = -30  # change the x label rotation
my_config.show_legend = False  # the legend of the bar
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15  # truncate x labels to the number of chars
# my_config.show_y_guides = False
my_config.width = 1000


repo_hist = pygal.Bar(my_config, style=my_style)
repo_hist.title = 'Most-Starred Python Projects on Github'
repo_hist.x_labels = repo_names

# add data to the histogram
# create a list of dictionary first
repo_star_descriptions = []
for repo_description, repo_star, repo_url in zip(repo_descriptions, repo_stars, repo_urls):
    repo_star_descriptions.append(dict([('value', repo_star), ('label', str(repo_description)), ('xlink', str(repo_url))]))
    # str() is necessary because there might be some non-string in the list, which may cause trouble

print(repo_star_descriptions)
repo_hist.add('', repo_star_descriptions)

repo_hist.render_to_file('repo star.svg')
