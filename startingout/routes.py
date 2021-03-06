import startingout.controllers.home_controller as regular


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('bookmarks', '/bookmarks')
    config.add_route('mini-scripts', '/mini-scripts')
