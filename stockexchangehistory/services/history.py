import re
import json
import operator

from stockexchangehistory.models.cotation import Cotation, CotationSchema
class History:
    """
    Parse bvmt tunisian website history by year and month
    """
    def parse(self, year, month):
        if (year == '15'):
            PATH = 'stockexchangehistory/utils/Cotation_site_2015.txt'
        elif (year == '2016'):
            PATH = 'stockexchangehistory/utils/histo_cotation_2016.txt'
        print(PATH)
        file = open(PATH, 'r')
        cotations = []
        __cotations = []
        lines = file.readlines()
        for i in range(len(lines)):
            if (i > 1):
                _cotations = lines[i].split()
                _data = re.compile('.*/'+month+'/'+year)
                _nbr = re.compile('.*[0-9]+.*')
                #print(re.)
                if (_data.match(_cotations[0])):
                    if (_nbr.match(_cotations[-1])):
                        cotation = Cotation(
                            _cotations[0],
                            _cotations[1],
                            _cotations[2],
                            ' '.join(_cotations[3:-7]),
                            _cotations[-7],
                            _cotations[-6],
                            _cotations[-5],
                            _cotations[-4],
                            _cotations[-3],
                            _cotations[-2],
                            _cotations[-1])
                        cotations.append(cotation)
                    else:
                        cotation = Cotation(
                            _cotations[0],
                            _cotations[1],
                            _cotations[2],
                            ' '.join(_cotations[3:-8]),
                            _cotations[-8],
                            _cotations[-7],
                            _cotations[-6],
                            _cotations[-5],
                            _cotations[-4],
                            _cotations[-3],
                            _cotations[-2])
                        cotations.append(cotation)
        sorted__cotations = sorted(cotations, key=operator.attrgetter('qty'), reverse=True)[:7]
        #sorted__cotations = filter(lambda c, d: int(c.qty) > int(d.qty), cotations)
        for cot in sorted__cotations:
            schema = CotationSchema()
            __cotations.append(schema.dump(cot))

                # if (len(_cotations) == 11):
                #
                #     schema = CotationSchema()
                #     cotations.append(schema.dump(cotation))
                # elif (len(_cotations) > 11 ):
                #     cotation = Cotation(
                #         _cotations[0],
                #         _cotations[1],
                #         _cotations[2],
                #         ' '.join(_cotations[3:-7]),
                #         _cotations[-7],
                #         _cotations[-6],
                #         _cotations[-5],
                #         _cotations[-4],
                #         _cotations[-3],
                #         _cotations[-2],
                #         _cotations[-1])
                #     schema = CotationSchema()
                #     cotations.append(schema.dump(cotation))


        return __cotations#.sort(key=self.sort_by_field('qty'), reverse=True)

    # """
    # Parse bvmt tunisian website 2015 history
    # """
    # def parse_2016():
    #     cotation2016 = open("stockexchangehistory/utils/histo_cotation_2016.txt", 'r')
    #     cotations = []
    #     lines = file.readlines()
    #     for i in range(len(lines)):
    #         if (i > 1):
    #             _cotations = lines[i].split()
    #             if (len(_cotations) == 11):
    #                 cotation = Cotation(
    #                     _cotations[0],
    #                     _cotations[1],
    #                     _cotations[2],
    #                     _cotations[3],
    #                     _cotations[4],
    #                     _cotations[5],
    #                     _cotations[6],
    #                     _cotations[7],
    #                     _cotations[8],
    #                     _cotations[9],
    #                     _cotations[10])
    #                 schema = CotationSchema()
    #                 cotations.append(schema.dump(cotation))
    #             elif (len(_cotations) > 11):
    #                 cotation = Cotation(
    #                     _cotations[0],
    #                     _cotations[1],
    #                     _cotations[2],
    #                     ' '.join(_cotations[3:-7]),
    #                     _cotations[-7],
    #                     _cotations[-6],
    #                     _cotations[-5],
    #                     _cotations[-4],
    #                     _cotations[-3],
    #                     _cotations[-2],
    #                     _cotations[-1])
    #                 schema = CotationSchema()
    #                 cotations.append(schema.dump(cotation))
    #     return cotations
    """
    Sort Cotation list by field
    """
    def sort_by_field(self, field):
        try:
            return int(json[field])
        except KeyError:
            return 0