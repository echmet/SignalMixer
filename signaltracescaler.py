from datapoint import Datapoint


class SignalTraceScaler:
    @staticmethod
    def scale(datapoints, scaleFrom, scaleTo):
        origin = datapoints[0].x
        shift = scaleFrom - datapoints[0].x
        stretchFactor = (scaleTo - scaleFrom) / (datapoints[-1].x - datapoints[0].x)
        scaled = []

        for pt in datapoints:
            distance = pt.x - datapoints[0].x
            newX = distance * stretchFactor + shift + origin
            scaled.append(Datapoint(newX, pt.y))

        return scaled
