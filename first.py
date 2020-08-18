from faker import Faker
from morse3 import Morse as m

fake = Faker()

for x in range(5):
    print(m(fake.name()).stringToMorse())
