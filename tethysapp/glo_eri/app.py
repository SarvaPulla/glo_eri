from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting, PersistentStoreConnectionSetting


class GloEri(TethysAppBase):
    """
    Tethys app class for Emergency Response Infrastructure.
    """

    name = 'Emergency Response Infrastructure'
    index = 'glo_eri:home'
    icon = 'glo_eri/images/logo.jpg'
    package = 'glo_eri'
    root_url = 'glo-eri'
    color = '#16a085'
    description = 'Emergency Response Infrastructure'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='glo-eri',
                controller='glo_eri.controllers.home'
            ),
            UrlMap(
                name='popup-info',
                url='glo-eri/popup-info',
                controller='glo_eri.controllers_ajax.get_popup_info'
            ),
            UrlMap(
                name='get-meta-file',
                url='glo-eri/get-meta-file',
                controller='glo_eri.controllers_ajax.get_meta_file'
            ),
            UrlMap(
                name='add-point',
                url='glo-eri/add-point',
                controller='glo_eri.controllers.add_point'
            ),
            UrlMap(
                name='delete-layer',
                url='glo-eri/delete-layer',
                controller='glo_eri.controllers.delete_layer'
            ),
            UrlMap(
                name='submit-delete-layer',
                url='glo-eri/delete-layer/submit',
                controller='glo_eri.controllers_ajax.layer_delete'
            ),
            UrlMap(
                name='add-point-ajax',
                url='glo-eri/add-point/submit',
                controller='glo_eri.controllers_ajax.point_add'
            ),
            UrlMap(
                name='approve-points',
                url='glo-eri/approve-points',
                controller='glo_eri.controllers.approve_points'
            ),
            UrlMap(
                name='approve-points_tabulator',
                url='glo-eri/approve-points/tabulator',
                controller='glo_eri.controllers_ajax.points_tabulator'
            ),
            UrlMap(
                name='update-points-ajax',
                url='glo-eri/approve-points/submit',
                controller='glo_eri.controllers_ajax.point_update'
            ),
            UrlMap(
                name='delete-points-ajax',
                url='glo-eri/approve-points/delete',
                controller='glo_eri.controllers_ajax.point_delete'
            ),
            UrlMap(
                name='add-polygon',
                url='glo-eri/add-polygon',
                controller='glo_eri.controllers.add_polygon'
            ),
            UrlMap(
                name='add-polygon-ajax',
                url='glo-eri/add-polygon/submit',
                controller='glo_eri.controllers_ajax.polygon_add'
            ),
            UrlMap(
                name='approve-polygons',
                url='glo-eri/approve-polygons',
                controller='glo_eri.controllers.approve_polygons'
            ),
            UrlMap(
                name='approve-polygons-tabulator',
                url='glo-eri/approve-polygons/tabulator',
                controller='glo_eri.controllers_ajax.polygons_tabulator'
            ),
            UrlMap(
                name='update-polygons-ajax',
                url='glo-eri/approve-polygons/submit',
                controller='glo_eri.controllers_ajax.polygon_update'
            ),
            UrlMap(
                name='delete-polygons-ajax',
                url='glo-eri/approve-polygons/delete',
                controller='glo_eri.controllers_ajax.polygon_delete'
            ),
            UrlMap(
                name='add-new-layer',
                url='glo-eri/add-new-layer',
                controller='glo_eri.controllers.add_new_layer'
            ),
            UrlMap(
                name='get-new-layer-attributes',
                url='glo-eri/add-new-layer/get-attributes',
                controller='glo_eri.controllers_ajax.get_shp_attributes'
            ),
            UrlMap(
                name='add-new-layer-ajax',
                url='glo-eri/add-new-layer/submit',
                controller='glo_eri.controllers_ajax.new_layer_add'
            ),
            UrlMap(
                name='set-layer-style',
                url='glo-eri/set-layer-style',
                controller='glo_eri.controllers.set_layer_style'
            ),
            UrlMap(
                name='set-layer-style-ajax',
                url='glo-eri/set-layer-style/submit',
                controller='glo_eri.controllers_ajax.layer_style_set'
            ),
            UrlMap(
                name='add-endpoint',
                url='glo-eri/add-endpoint',
                controller='glo_eri.controllers.add_endpoint'
            ),
            UrlMap(
                name='add-endpoint-submit',
                url='glo-eri/add-endpoint/submit',
                controller='glo_eri.controllers_ajax.endpoint_add'
            ),
            UrlMap(
                name='delete-endpoint',
                url='glo-eri/delete-endpoint',
                controller='glo_eri.controllers.delete_endpoint'
            ),
            UrlMap(
                name='delete-endpoint-submit',
                url='glo-eri/delete-endpoint/submit',
                controller='glo_eri.controllers_ajax.endpoint_delete'
            ),
            UrlMap(
                name='get-layers-info',
                url='glo-eri/api/get-layers-info',
                controller='glo_eri.api.get_layers_info'
            ),
            UrlMap(
                name='get-layers-by-county',
                url='glo-eri/api/get-layers-by-county',
                controller='glo_eri.api.get_layers_by_county'
            ),
            UrlMap(
                name='get-points-by-county',
                url='glo-eri/api/get-points-by-county',
                controller='glo_eri.api.get_points_by_county'
            ),
            UrlMap(
                name='get-polygons-by-county',
                url='glo-eri/api/get-polygons-by-county',
                controller='glo_eri.api.get_polygons_by_county'
            ),
            UrlMap(
                name='get-points-by-layer',
                url='glo-eri/api/get-points-by-layer',
                controller='glo_eri.api.get_points_by_layer'
            ),
            UrlMap(
                name='get-polygons-by-layer',
                url='glo-eri/api/get-polygons-by-layer',
                controller='glo_eri.api.get_polygons_by_layer'
            ),
            UrlMap(
                name='get-points-by-geometry',
                url='glo-eri/api/get-points-by-geometry',
                controller='glo_eri.api.get_points_by_geom'
            ),
            UrlMap(
                name='get-polygons-by-geometry',
                url='glo-eri/api/get-polygons-by-geometry',
                controller='glo_eri.api.get_polygons_by_geom'
            ),
            UrlMap(
                name='dowloand-layers',
                url='glo-eri/download-layers',
                controller='glo_eri.controllers_ajax.download_layers'
            ),
            UrlMap(
                name='download-interaction',
                url='glo-eri/download-interaction',
                controller='glo_eri.controllers_ajax.download_interaction'
            ),
            UrlMap(
                name='download-points-csv',
                url='glo-eri/api/download-points-csv',
                controller='glo_eri.api.download_points_csv'
            ),
            UrlMap(
                name='download-polygons-csv',
                url='glo-eri/api/download-polygons-csv',
                controller='glo_eri.api.download_polygons_csv'
            ),
            UrlMap(
                name='download-layer-csv',
                url='glo-eri/api/download-layer-csv',
                controller='glo_eri.api.download_layer_csv'
            ),
        )

        return url_maps

    def persistent_store_settings(self):
        """
        Define Persistent Store Settings.
        """
        ps_settings = (
            PersistentStoreDatabaseSetting(
                name='layers',
                description='layers database',
                initializer='glo_eri.model.init_layer_db',
                required=True,
                spatial=True
            ),
        )

        return ps_settings
