import random


def dinosaur(location=0):
    return {
        'name': ('Bob the Brontosaurus', 'Alice the Velociraptor', 'Charlie the T-Rex')[random.randint(0, 2)],
        'creature': {
            'alive': True,
            'age': 0.0,
            'health': 1.0
        },
        'location': location,
        'nearby_entities': []
    }
