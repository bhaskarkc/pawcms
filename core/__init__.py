import dbsettings


class CoreSettings(dbsettings.Group):
    site_name = dbsettings.StringValue()
    site_slogan = dbsettings.StringValue()

settings = CoreSettings()