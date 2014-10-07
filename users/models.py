from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, full_name=''):
        # import pdb
        # pdb.set_trace()
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=username,
            email=UserManager.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, full_name=''):
        """
        Creates and saves a superuser with the given email, full name and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
            full_name=full_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def by_group(self, group_name):
        try:
            group = Group.objects.get(name=group_name)
            return self.filter(groups=group)
        except Group.DoesNotExist:
            return False


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=245)
    email = models.EmailField(
        verbose_name='email address',
        max_length=254,
        unique=True,
        db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='users', blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'email']

    def __unicode__(self):
        return self.username

    def get_short_name(self):
        # The user is identified by username
        return self.username

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def email_user(self, subject, message, from_email):
        pass

    def is_admin(self):
        return self.is_superuser

    def in_group(self, group_name):
        try:
            group = Group.objects.get(name=group_name)
            return group in self.groups.all()
        except Group.DoesNotExist:
            return False

    def add_to_group(self, group_name):
        try:
            group = Group.objects.get(name=group_name)
            self.groups.add(group)
            return True
        except Group.DoesNotExist:
            return False

    objects = UserManager()


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(u):
        if u.is_authenticated():
            # if bool(u.groups.filter(name__in=group_names)) | u.is_superuser():
            #    return True
            if bool(u.groups.filter(name__in=group_names)):
                return True
        return False

    return user_passes_test(in_groups)


class GroupProxy(Group):
    class Meta:
        proxy = True
        verbose_name = _('Group')
        # verbose_name_plural = _('Groups')
