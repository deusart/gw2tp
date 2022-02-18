from gw2api import gw2api_urls as urls
from gw2api import gw2api_filesystem
from gw2api import gw2api_format
from gw2api import gw2api_requests
def upload_gw2api(id):
    url = urls.__get_item_url(id)
    print(url)
    item = gw2api_requests.__get_item(url)
    print(item)
    item_clean = gw2api_format.__get_format_item(item['data'])
    print(item_clean)
    gw2api_filesystem.__save_item_json(item_clean["id"],item_clean)