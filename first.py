from faker import Faker
fake = Faker()

for x in range(5):
    print(fake.name())
