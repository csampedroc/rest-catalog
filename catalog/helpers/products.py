from django.core.mail import send_mail


def send_data_update_notification(sku, product_name):

    send_mail(
        f"Update product data {sku} - {product_name}",
        f"This is a notification because, there is a update in product {sku} - {product_name}",
        "app_catalog@gmail.com",
        ["app_catalog@gmail.com"],
        fail_silently=False,
    )
