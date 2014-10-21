import dbsettings


class CoreSettings(dbsettings.Group):
    site_name = dbsettings.StringValue()
    site_slogan = dbsettings.StringValue()
    address = dbsettings.TextValue()
    phone = dbsettings.StringValue()
    fax = dbsettings.StringValue(required=False)
    email = dbsettings.StringValue()


settings = CoreSettings()