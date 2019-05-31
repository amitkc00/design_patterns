from customer import customer

if __name__ == '__main__':
    coach = customer()
    coach.createVendor('EY') # We can move this to customer __init__ method as well
    coach.doTask()

    dupoint = customer()
    dupoint.createVendor('PWC') # This is something we can do as like dupoint.setNewVendor() to show loose coupling.
    dupoint.doTask()