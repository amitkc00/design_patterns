from context import context
from strategy_bicycle import bicycle_map
from strategy_car import car_map
from strategy_publicTransport import publicTransport_map

if __name__ == '__main__':

    # Get the basic context object as client.
    client = context()

    #Instantiate all the strategy here or later when you need it.
    bicycle_strategy = bicycle_map('home', 'costco')
    car_strategy = car_map('home', 'marlborough')
    public_strategy = publicTransport_map('home', 'south station')

    #Car Strategy 
    client.setStrategy(car_strategy)
    client.executeStrategy()

    # Dynamically setting Bicycle Strategy
    client.setStrategy(bicycle_strategy)
    client.executeStrategy()

    # Got bored of Bicycle, moving on to public transport
    # The ability to extend this code without changing the context, is great.
    client.setStrategy(public_strategy)
    client.executeStrategy()

    # I really like it. I think learning and implementing it in Python is great way to make sure I really get the concepts.
