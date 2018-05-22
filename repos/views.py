from django.shortcuts import render
from github.api_client import GithubApiClient


def organization_repos(request):
    """Shows the repositories of a organization"""
    if 'organization' in request.POST:
        organization = request.POST['organization']
        api_client = GithubApiClient()
        repositories = api_client.get_repositories_by_organization(organization)
        context = {'organization': organization, 'repositories': repositories}
    else:
        context = {'organization': None}

    return render(request, 'repos/organization_repos.html', context)


def stars_repos(request):
    """Shows the selected amount of repositories with more stars in github"""
    number_of_repos = ''
    if 'number_of_repos' in request.POST:
        number_of_repos = request.POST['number_of_repos']
    if number_of_repos == '':
        number_of_repos = 10
    api_client = GithubApiClient()
    repositories = api_client.get_repositories_by_stars(number_of_repos)
    context = {
        'number_of_repos': number_of_repos,
        'repositories': repositories
    }
    return render(request, 'repos/stars_repos.html', context)
