states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'Califonia': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "FLorida's abbreviation is: ", states['Florida']

print '-' * 10
for a, b in states.items():
    print "%s state is abbreviated %s and has city %s" %(a, b, cities[b])

state = states.get('Texas')

print state
print not state
if not state:
    print 111
