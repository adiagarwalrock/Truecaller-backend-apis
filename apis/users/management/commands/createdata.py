from django.core.management.base import BaseCommand

from users.models import User, UserContact

from faker import Faker

# python manage.py createdata


class Command(BaseCommand):
    help = "Command informaation"

    def handle(self, *args, **kwargs):

        fake = Faker()

        for _ in range(100):
            name = fake.name()
            phone = fake.random_number(digits=11)
            password = fake.password()
            email = fake.email()

            print(_, name, phone, password, email)

            user_obj = User.objects.create(name=name, email=email,
                                           password=password, phone=phone)

            for i in range(15):
                cname = fake.name()
                cphone = fake.random_number(digits=11)
                cemail = fake.email()
                cspam_liklihood = fake.random_number(digits=2)

                print('\t', _, '.', i, '|', cname,
                      cphone, cspam_liklihood, cemail)

                UserContact.objects.create(
                    name=cname, phone=cphone, spam_liklihood=cspam_liklihood, email=cemail, imported_from=user_obj)
