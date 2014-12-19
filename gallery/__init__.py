import dbsettings


class GallerySettings(dbsettings.Group):
    gallery_in_nav = dbsettings.BooleanValue('Show Gallery in main nav menu', default=True)

gallery_settings = GallerySettings('Gallery Settings')