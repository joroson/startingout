from pyramid.view import view_config


def get_test_packages():
    return {}


@view_config(route_name='home', renderer='startingout:templates/home/index.pt')
def home_index(_):
    return {}


@view_config(route_name='about', renderer='startingout:templates/home/about.pt')
def home_about(_):
    return {}


@view_config(route_name='bookmarks', renderer='startingout:templates/home/bookmarks.pt')
def home_bookmarks(_):
    return {}
