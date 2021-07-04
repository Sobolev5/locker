from settings import SITE_URL


def common(request):
    return {
        "SITE_URL": SITE_URL,
    }
