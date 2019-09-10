# ckanext-new-resource-order
Simple CKAN extension to move new resources to the first position

Based on this Gist: https://gist.github.com/salsa-nathan/3e38774f7f3e4d3582eec3774b055643

## Installation

1. Install this extension into your CKAN python virtual environment, e.g.

  pip install -e  git+https://github.com/salsa-nathan/ckanext-new-resource-order.git#egg=ckanext-new-resource-order

1. Enable the extension in your CKAN `.ini` file:

  ckan.plugins = ... new_resource_order 
