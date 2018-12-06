import requests

class NASA_API():

    def __init__():
        print("Successfully made an API object")

    def search(q, center=None, description=None, description_508=None,
                keywords=None, location=None, media_type=None, media_type='image',
                nasa_id = None, photographer=None, secondary_creator=None,
                title=None, year_start=1900, year_end=3000):

        http_endpoint = 'https://images-api.nasa.gov/search?'

        if q:
            if isinstance(q, list):
                q = '|'.join(q)
            http_endpoint += "&q={}".format(q)

        if center:
            if not isinstance(center, str):
                raise "Center is invalid data type"
            http_endpoint += '&q={}'.format(center)

        if description:
            http_endpoint += '&q={}'.format(description)
