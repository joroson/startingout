from pyramid.request import Request

from startingout.viewmodels.shared.viewmodel_base import ViewModelBase


class MiniScriptsViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.weight = self.request_dict.get('weight')
        self.output_lbs = self.request_dict.get('output_lbs')
        self.output_sto = self.request_dict.get('output_sto')
        self.output_slb = self.request_dict.get('output_slb')
        self.output_ozs = self.request_dict.get('output_ozs')
        self.output_kgs = self.request_dict.get('output_kgs')
