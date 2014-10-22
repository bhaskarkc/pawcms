import dbsettings


class CoreSettings(dbsettings.Group):
    site_name = dbsettings.StringValue()
    site_slogan = dbsettings.StringValue(required=False)
    address = dbsettings.TextValue(required=False)
    phone = dbsettings.StringValue(required=False)
    fax = dbsettings.StringValue(required=False)
    email = dbsettings.StringValue(required=False)
    location_name = dbsettings.StringValue(required=False)
    latitude = dbsettings.StringValue(required=False)
    longitude = dbsettings.StringValue(required=False)


settings = CoreSettings()