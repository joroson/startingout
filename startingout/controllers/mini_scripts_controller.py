from pyramid.view import view_config

from startingout.viewmodels.mini_scripts.mini_scripts_viewmodel import MiniScriptsViewModel


@view_config(route_name='mini-scripts', renderer='startingout:templates/mini-scripts/index.pt')
@view_config(route_name='mini-scripts/', renderer='startingout:templates/mini-scripts/index.pt')
def mini_scripts_index(_):
    return {}


@view_config(route_name='mini-scripts/weight-conversion', renderer='startingout:templates/mini-scripts/weight-conversion.pt', request_method='GET')
@view_config(route_name='mini-scripts/weight-conversion/', renderer='startingout:templates/mini-scripts/weight-conversion.pt', request_method='GET')
def weight_conversion_get(_):
    # vm = MiniScriptsViewModel(request)
    # return vm.to_dict()
    return {
        'weight': None,
        'output_lbs': None,
        'output_sto': None,
        'output_slb': None,
        'output_ozs': None,
        'output_kgs': None
    }


@view_config(route_name='mini-scripts/weight-conversion', renderer='startingout:templates/mini-scripts/weight-conversion.pt', request_method='POST')
@view_config(route_name='mini-scripts/weight-conversion/', renderer='startingout:templates/mini-scripts/weight-conversion.pt', request_method='POST')
def weight_conversion_post(request):
    vm = MiniScriptsViewModel(request)

    def convert_lbs(lbs):
        lbs_float = float(lbs)
        lbs_int = int(lbs_float)
        print(f"lbs expressed as an integer is {lbs_int} and as a float is {lbs_float}")
        con_lbs_st = lbs_int // 14
        con_lbs_lb = lbs_int % 14
        con_lbs_oz = (lbs_float % 14) - con_lbs_lb
        con_lbs_oz = int(round(con_lbs_oz, 2) // 0.0625)
        con_lbs_kg = round(lbs_float * 0.45359, 1)
        print(f"{lbs}lbs is equal to {con_lbs_st}st, {con_lbs_lb}lbs, {con_lbs_oz}ounces. Or, {con_lbs_kg}kgs")
        # return vm.to_dict()
        return {
            'output_sto': con_lbs_st,
            'output_slb': con_lbs_lb,
            'output_ozs': con_lbs_oz,
            'output_kgs': con_lbs_kg
        }

    def convert_sts(stones, pounds=0, ounces=0):
        stones = int(stones)
        pounds = int(pounds)
        ounces = int(ounces)
        con_sts_lb = (stones * 14) + pounds + (ounces * 0.0625)
        con_sts_kg = round(con_sts_lb * 0.45359, 3)
        print(f"{stones}st, {pounds}lbs {ounces}oz, is equal to {con_sts_lb}lbs or {con_sts_kg}kgs.")
        # return vm.to_dict()
        return {
            'output_lbs': con_sts_lb,
            'output_kgs': con_sts_kg
        }

    def convert_kgs(kgs):
        kgs_float = float(kgs)
        con_kgs_pd = kgs_float * 2.20462
        con_kgs_pd_int = int(con_kgs_pd)
        con_kgs_st = con_kgs_pd_int // 14
        con_kgs_lb = int(con_kgs_pd % 14)
        con_kgs_oz = con_kgs_pd - con_kgs_pd_int
        con_kgs_oz = int(round(con_kgs_oz, 2) // 0.0625)
        print(f"{kgs}kgs is equal to {round(con_kgs_pd, 2)}lbs or {con_kgs_st}st, {con_kgs_lb}lbs, {con_kgs_oz}oz.")
        # return vm.to_dict()
        return {
            'output_lbs': round(con_kgs_pd, 2),
            'output_sto': con_kgs_st,
            'output_slb': con_kgs_lb,
            'output_ozs': con_kgs_oz,
        }

    weight = request.POST.get('unit')
    print(f"The conversion unit is {weight}.")

    if request.POST.get('unit') == 'pounds':
        # pounds = request.POST.get('input-lb')
        # print(f"{pounds}lbs inputted.")
        pounds = convert_lbs(request.POST.get('input-lb'))
        # return vm.to_dict()
        return pounds

    if request.POST.get('unit') == 'st-lbs-oz':
        st_lb_ozs = convert_sts(request.POST.get('input-st-st'), request.POST.get('input-st-lb'),
                                request.POST.get('input-st-oz'))
        # return vm.to_dict()
        return st_lb_ozs

    if request.POST.get('unit') == 'kgs':
        kgs = convert_kgs(request.POST.get('input-kg'))
        # return vm.to_dict()
        return kgs

    print(vm.to_dict())
