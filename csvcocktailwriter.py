import abstractcocktailwriter


class CSVCocktailWriter(abstractcocktailwriter.AbstractCocktailWriter):
    def write(self, header, cocktail, target):
        try:
            f = open(target, 'bw')

            s = ''
            for col in header:
                s += '{};'.format(col)
            s += '\n'

            for pt in cocktail:
                s += str(pt.x)
                for y in pt.yValues:
                    if y is None:
                        s+= ';'
                    else:
                        s += ';{}'.format(y)
                s += '\n'

            f.write(s.encode('UTF-8'))
        except OSError as ex:
            raise abstractcocktailwriter.CocktailWriterError(str(ex))
