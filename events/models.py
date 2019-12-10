from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField

#
# class Event(models.Model):
#     YEAR_CHOICES = []
#     for i in range(2019, timezone.now().year + 5):
#         YEAR_CHOICES.append((i, i))
#     name = models.CharField(max_length=50)
#     year = models.IntegerField(default=timezone.now().year, choices=YEAR_CHOICES,
#                                null=True, blank=True,
#                                help_text='year that event is being held')
#
#     def __str__(self):
#         return self.name


class Staff(models.Model):
    # event = models.ForeignKey(Event,
    #                           on_delete=models.CASCADE, )
    first_name = models.CharField(max_length=30, verbose_name='first name')
    last_name = models.CharField(max_length=30, verbose_name='last name')

    team_role_choices = [
        ('Curation', 'Curation'),
        ('Organizer', 'Organizer'),
        ('Co Organizer', 'Co Organizer'),
        ('Marketing', 'Marketing'),
        ('Documentation', 'Documentation'),
        ('Creativity', 'Creativity'),
        ('Frontend Developer', 'Frontend Developer'),
        ('Backend Developer', 'Backend Developer'),
        ('UI Designer', 'UI Designer'),
        ('Graphic Designer', 'Graphic Designer'),
    ]
    """
    Curation
    Organizer
    CoOrganizer
    Marketing
    Documentation
    Creativity
    FrontEnd Developer
    BackEnd Developer
    UI Designer
    """

    role = models.CharField(choices=team_role_choices, max_length=30,
                            help_text='team\'s way of association in team', default='others', null=True, blank=True)

    bio = models.TextField(blank=True, null=True, help_text='description about person e.g. role in team achievements')
    picture = models.ImageField(upload_to='pics/team/', help_text='team\'s picture')
    linkedin_account = models.CharField(max_length=100, null=True, blank=True,
                                        help_text='linkedin.com/in/[User_Account]')

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Speaker(models.Model):
    # event = models.ForeignKey(Event,
    #                           on_delete=models.CASCADE,
    #                           help_text='Choose Your Event:', null=True, blank=True)

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('deactive', 'Deactive'),
    ]

    first_name = models.CharField(max_length=30, verbose_name='first name')
    last_name = models.CharField(max_length=30, verbose_name='last name')
    picture = models.ImageField(upload_to='pics/speakers/',
                                default='default.jpg', null=True, blank=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=True, blank=True)
    bio = models.TextField(max_length=500)
    account_status = models.CharField(choices=STATUS_CHOICES,
                                      default='deactive', max_length=20)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Sponsor(models.Model):
    # event = models.ForeignKey(Event,
    #                           on_delete=models.CASCADE,
    #                           help_text='Choose Your Event:', )

    sponsor_type_choices = [('financial', 'Financial'),
                            ('spiritual', 'Spiritual'),
                            ('other', 'Other'), ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('deactive', 'Deactive'),
    ]

    sponsor_organization = models.CharField(max_length=50, help_text='sponsor company')
    name = models.CharField(max_length=50, help_text='sponsor person')
    sponsor_type = models.CharField(choices=sponsor_type_choices, default='other',
                                    help_text='type of support', max_length=30)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    about = models.TextField(max_length=1000, help_text='about sponsor')
    logo = models.ImageField(upload_to='pics/sponsors/', help_text='company\'s logo',
                             default='default.jpg')
    account_status = models.CharField(choices=STATUS_CHOICES,
                                      default='deactive', max_length=20)

    def __str__(self):
        return self.sponsor_organization


class Attendee(models.Model):
    full_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    career = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    start = models.SmallIntegerField()
    end = models.SmallIntegerField()
    before_tedxes = models.TextField(max_length=400)
    what_made_you = models.TextField(max_length=400)
    how_familiar = models.TextField(max_length=400)
    expects = models.TextField(max_length=400)
