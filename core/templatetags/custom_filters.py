from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def to_uppercase(value):
    """
    Converte o valor para maiúsculas.
    """
    if isinstance(value, str):
        return value.upper()
    return value


@register.filter
def remove_extension(filename):
    """
    Retira a extensão do nome do arquivo, tratando casos com múltiplos pontos.
    """
    return filename.rsplit('.', 1)[0]  # Divide no último ponto


@register.inclusion_tag('components/../templates/index/carrossel_servicos.html')
def render_carousel(carousel_id, carousel_internet, carousel_int_is_active, img_base_path):
    return {
        'carousel_id': carousel_id,
        'carousel_internet': carousel_internet,
        'carousel_int_is_active': carousel_int_is_active,
        'img_base_path': img_base_path,
    }