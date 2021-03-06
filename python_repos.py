import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用，并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
try:
    r = requests.get(url)
    print("Status code:", r.status_code)
except Exception as e:
    print("网络异常")
else:
    # 将API响应存储在一个变量中
    response_dict = r.json()
    print("Total repositores:", response_dict['total_count'])
    # 探索有关仓库的信息
    repo_dicts = response_dict['items']
    print("Repositores returned:", len(repo_dicts))

    names, stars = [], []


    # 研究第一个仓库
    repo_dict = repo_dicts[0]
    # print("\nSelected information about first repository:")

    print("\nSelected information about each repository:")
    # for repo_dict in repo_dicts:
    #     names.append(repo_dict['name'])
    #     stars.append(repo_dict['stargazers_count'])
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
        }

        plot_dicts.append(plot_dict)
    # 可视化
    my_style = LS('#333366', base_style = LCS)

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    # 将较长的项目名缩短为15个字符
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style = my_style)

    # chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)
    chart.title = "GitHub 上点赞最多的仓库"
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('python_repos.svg')

    #     print('Name-项目名:', repo_dict['name'])
    #     print('Owner-作者:', repo_dict['owner']['login'])
    #     print('Stars-点赞数:', repo_dict['stargazers_count'])
    #     print('Repositores-项目地址:', repo_dict['html_url'])
    #     print('Create-创造时间:', repo_dict['created_at'])
    #     print('Updated-更新时间:', repo_dict['updated_at'])
    #     print('Description-描述:', repo_dict['description'])


    # print("\nKeys:", len(repo_dict))


    # 处理结果
    # print(response_dict.keys())
