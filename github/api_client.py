import requests


class GithubApiClient():
    """Client to interact with github's API"""
    BASE_URL = 'https://api.github.com/'
    PAGE_NUM = 1
    RESULTS_PER_PAGE = 30

    def make_request(self, path, request_params):
        default_params = {
            'page': self.PAGE_NUM,
            'per_page': self.RESULTS_PER_PAGE
        }
        params = {**request_params, **default_params}
        response_object = requests.get(self.BASE_URL + path, params=params)
        response = response_object.json()
        return response

    def get_repositories_by_organization(self, organization):
        """Returns the repositories of a organization"""
        return self.make_request('orgs/' + organization + '/repos', {})

    def get_repositories_by_stars(self, num_repos):
        """Returns the number of repositories by number of stars"""
        self.RESULTS_PER_PAGE = num_repos
        return self.make_request('search/repositories', {'q': 'stars:>0'})

    def set_page(self, page_num):
        self.PAGE_NUM = page_num