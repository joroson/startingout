from pyramid.request import Request
from pyramid.view import view_config


@view_config(route_name='mini-scripts', renderer='startingout:templates/mini-scripts/index.pt')
@view_config(route_name='mini-scripts/', renderer='startingout:templates/mini-scripts/index.pt')
def mini_scripts_index(_):
    return {}


@view_config(route_name='mini-scripts/weight-conversion',
             renderer='startingout:templates/mini-scripts/weight-conversion.pt', request_method='GET')
@view_config(route_name='mini-scripts/weight-conversion/',
             renderer='startingout:templates/mini-scripts/weight-conversion.pt', request_method='GET')
def weight_conversion_get(_):
    # vm = MiniScriptsViewModel(request)
    # return vm.to_dict()

    return {
        'weight': None,
        'output_lbs': None,
        'output_sto': None,
        'output_slb': None,
        'output_ozs': None,
        'output_kgs': None,
        'input_pou': None,
        'input_sto': None,
        'input_slb': None,
        'input_ozs': None,
        'input_kgs': None
    }

    # return {}


@view_config(route_name='mini-scripts/weight-conversion',
             renderer='startingout:templates/mini-scripts/weight-conversion.pt', request_method='POST')
@view_config(route_name='mini-scripts/weight-conversion/',
             renderer='startingout:templates/mini-scripts/weight-conversion.pt', request_method='POST')
def weight_conversion_post(request: Request):
    def info():
        print("request.POST: ", request.POST)
        print("request.GET: ", request.GET)
        print("request.matchdict: ", request.matchdict)

    if request.POST.get('unit') == 'pounds':
        lbs = request.POST.get('input-lb')
        lbs_float = float(lbs)
        lbs_int = int(lbs_float)
        con_lbs_st = lbs_int // 14
        con_lbs_lb = lbs_int % 14
        con_lbs_oz = (lbs_float % 14) - con_lbs_lb
        con_lbs_oz = int(round(con_lbs_oz // 0.0625, 2))
        con_lbs_kg = round(lbs_float * 0.45359, 1)

        info()

        print(f"output_sto = {con_lbs_st}\noutput_slb = {con_lbs_lb}\noutput_ozs = {con_lbs_oz}\noutput_kgs = {con_lbs_kg}\ninput_pou = {lbs_float}")

        return {
            'output_lbs': None,
            'output_sto': con_lbs_st,
            'output_slb': con_lbs_lb,
            'output_ozs': con_lbs_oz,
            'output_kgs': con_lbs_kg,
            'input_pou': lbs_float,
            'input_sto': None,
            'input_slb': None,
            'input_ozs': None,
            'input_kgs': None
        }

    elif request.POST.get('unit') == 'st-lbs-oz':
        stones = int(request.POST.get('input-st-st'))
        pounds = int(request.POST.get('input-st-lb'))
        ounces = int(request.POST.get('input-st-oz'))
        con_sts_lb = (stones * 14) + pounds + (ounces * 0.0625)
        con_sts_kg = round(con_sts_lb * 0.45359, 2)

        info()

        return {
            'output_lbs': con_sts_lb,
            'output_sto': None,
            'output_slb': None,
            'output_ozs': None,
            'output_kgs': con_sts_kg,
            'input_pou': None,
            'input_sto': stones,
            'input_slb': pounds,
            'input_ozs': ounces,
            'input_kgs': None
        }

    elif request.POST.get('unit') == 'kgs':
        kgs = request.POST.get('input-kg')
        kgs_float = float(kgs)
        con_kgs_pd = kgs_float * 2.20462
        con_kgs_pd_int = int(con_kgs_pd)
        con_kgs_st = con_kgs_pd_int // 14
        con_kgs_lb = int(con_kgs_pd % 14)
        con_kgs_oz = con_kgs_pd - con_kgs_pd_int
        con_kgs_oz = int(round(con_kgs_oz // 0.0625, 2))

        info()

        return {
            'output_lbs': round(con_kgs_pd, 2),
            'output_sto': con_kgs_st,
            'output_slb': con_kgs_lb,
            'output_ozs': con_kgs_oz,
            'output_kgs': None,
            'input_pou': None,
            'input_sto': None,
            'input_slb': None,
            'input_ozs': None,
            'input_kgs': kgs_float
        }

    else:
        info()
        return {}

