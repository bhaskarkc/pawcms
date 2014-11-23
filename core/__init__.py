import dbsettings
import os
from django.conf import settings


def get_themes():
    all_themes = []
    for template_dir in settings.TEMPLATE_DIRS:
        themes_dir = os.path.join(template_dir, 'themes')
        for theme_dir in os.listdir(themes_dir):
            all_themes += ((theme_dir, theme_dir),)
    return all_themes


themes = get_themes()


class SiteSettings(dbsettings.Group):
    site_name = dbsettings.StringValue()
    site_slogan = dbsettings.StringValue(required=False)
    theme = dbsettings.MultipleChoiceValue(choices=themes, help_text='Change with caution')


site_settings = SiteSettings(' Site Settings')


class ContactSettings(dbsettings.Group):
    address = dbsettings.TextValue(required=False)
    phone = dbsettings.StringValue(required=False)
    fax = dbsettings.StringValue(required=False)
    email = dbsettings.StringValue(required=False)
    location_name = dbsettings.StringValue(required=False)
    latitude = dbsettings.StringValue(required=False)
    longitude = dbsettings.StringValue(required=False)


contact_settings = ContactSettings('Contact Settings')