from subject_Weather import weather
from observer_currentCondition import currentCondition
from observer_forecastDisplay import forecastDisplay
from observer_statisticsDisplay import statisticsDisplay

if __name__== "__main__":

    weather = weather()

    current = currentCondition()
    weather.subscribeElem(current)

    forecast = forecastDisplay()
    weather.subscribeElem(forecast)

    stats = statisticsDisplay()
    weather.subscribeElem(stats)

    # I don't think this is right design. How can the weather object decides itself to notify. 
    # I think it should precursor an event that would lead to this notification.
    weather.notify()
