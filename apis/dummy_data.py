from faker import Faker
import django
import os
from users.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apis.settings')

django.setup()


obj = Faker()


def call(N=300):
    num = 1
    for i in range(N):
        name = obj.name()
        email = obj.email()
        phone = '+' + str(obj.random_number(digits=12))
        # spam_liklihood = obj.random_number(digits=2)
        password = obj.password()

        # basic_obj = UserContact.objects.get_or_create(
        #     name=name, email=email, phone=phone, spam_liklihood=spam_liklihood)[0]

        User.objects.get_or_create(
            name=name, password=password, phone=phone, email=email)[0]

        num += 1


if __name__ == '__main__':
    print("Filling random data")
    call(300)
    print("Filling done ")
