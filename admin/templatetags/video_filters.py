from django import template

register = template.Library()

@register.filter
def embed_url(url):
    # Convert YouTube watch URL to embed URL
    if 'watch?v=' in url:
        video_id = url.split('watch?v=')[1]
        return f'https://www.youtube.com/embed/{video_id}'
    return url