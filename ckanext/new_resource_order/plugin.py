import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging

log = logging.getLogger(__name__)


class NewResourceOrderPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IResourceController, inherit=True)

    def after_create(self, context, data_dict):
        # Set the resource position order for this (latest) resource to first
        resource_id = data_dict.get('id', None)
        package_id = data_dict.get('package_id', None)
        if resource_id and package_id:
            try:
                toolkit.get_action('package_resource_reorder')(context, {'id': package_id, 'order': [resource_id]})
            except Exception, e:
                log.error(str(e))
        return data_dict
