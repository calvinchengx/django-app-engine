from django.conf import settings

def site_attributes(request):
    """
    This keeps all the site wide attributes like site name, tag line \n
    etc in one dictionary which is sent to the Template using the \n
    context processor
    """
    try:
        host = request.get_host()
        settings.SITE_ATTRIBUTES['hostname'] = 'http://%s' % host
        settings.SITE_ATTRIBUTES['hostname_ssl'] = 'https://%s' % host
    except Exception, e:
        #dbg(e)
        print e
    return {'site_attributes': settings.SITE_ATTRIBUTES}
