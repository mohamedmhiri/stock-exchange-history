import pandas as pd

from stockexchangehistory.models.cotation import Cotation, CotationSchema
class History:
    """
    Parse bvmt tunisian website 2015 history
    """
    def parse_2015():
        file = open("stockexchangehistory/utils/Cotation_site_2015.txt", 'r')
        cotations = []
        lines = file.readlines()
        for i in range(15000):
            if (i > 1):
                _cotations = lines[i].split()
                print(_cotations[0])
                if (len(_cotations) == 11):
                    print(i)
                    cotation = Cotation(
                        _cotations[0],
                        _cotations[1],
                        _cotations[2],
                        _cotations[3],
                        _cotations[4],
                        _cotations[5],
                        _cotations[6],
                        _cotations[7],
                        _cotations[8],
                        _cotations[9],
                        _cotations[10])
                    schema = CotationSchema()
                    cotations.append(schema.dump(cotation))
                elif (len(_cotations) > 11 ):
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
                    schema = CotationSchema()
                    cotations.append(schema.dump(cotation))
        return cotations

    """
    Parse bvmt tunisian website 2015 history
    """
    def parse_2016():
        cotation2016 = open("stockexchangehistory/utils/histo_cotation_2016.txt", 'r')
        cotations = []
        lines = file.readlines()
        for i in range(15000):
            if (i > 1):
                _cotations = lines[i].split()
                if (len(_cotations) == 11):
                    cotation = Cotation(
                        _cotations[0],
                        _cotations[1],
                        _cotations[2],
                        _cotations[3],
                        _cotations[4],
                        _cotations[5],
                        _cotations[6],
                        _cotations[7],
                        _cotations[8],
                        _cotations[9],
                        _cotations[10])
                    schema = CotationSchema()
                    cotations.append(schema.dump(cotation))
                elif (len(_cotations) > 11):
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
                    schema = CotationSchema()
                    cotations.append(schema.dump(cotation))
        return cotations