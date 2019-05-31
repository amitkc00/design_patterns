from beverage import beverage
from addon_hazzlenut import hazzlenut
from addon_vanilla import vanilla
import pdb

if __name__ == '__main__':
    #pdb.set_trace()
    regular = beverage()
    regular.printCost()
    regular.printDescription()

    regHazz = hazzlenut(regular)
    regHazz.printCost()
    regHazz.printDescription()

    regHazzVan = vanilla(regHazz)
    regHazzVan.printCost()
    regHazzVan.printDescription()