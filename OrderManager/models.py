from django.db import models
from django.contrib.auth.models import User
from StoreManager.models import Product

# Статусы заказов
class OrderStatus(models.TextChoices):
    PENDING = 'Pending', 'В ожидании'
    PROCESSING = 'Processing', 'В процессе'
    SHIPPED = 'Shipped', 'Отправлено'
    DELIVERED = 'Delivered', 'Доставлено'
    CANCELED = 'Canceled', 'Отменено'


from django.db import models


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name='Код купону')
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE, verbose_name='Знижка')
    valid_from = models.DateTimeField(verbose_name='Дійсний з')
    valid_to = models.DateTimeField(verbose_name='Дійсний до')
    active = models.BooleanField(default=True, verbose_name='Активний')
    usage_limit = models.PositiveIntegerField(null=True, blank=True, verbose_name='Ліміт використань')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купони'

class Discount(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва знижки')
    discount_type = models.CharField(
        max_length=50,
        choices=[('percentage', 'Відсоток'), ('fixed', 'Фіксована сума')],
        verbose_name='Тип знижки'
    )
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Значення знижки')
    start_date = models.DateTimeField(verbose_name='Початок дії')
    end_date = models.DateTimeField(verbose_name='Кінець дії', blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return f"{self.name} ({self.discount_type} - {self.value})"

    class Meta:
        verbose_name = 'Знижка'
        verbose_name_plural = 'Знижки'



class DeliveryMethod(models.Model):
    name = models.CharField(max_length=100, verbose_name='Метод доставки')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вартість доставки')
    estimated_time = models.CharField(max_length=50, verbose_name='Орієнтовний час доставки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Метод доставки'
        verbose_name_plural = 'Методи доставки'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders', verbose_name='Пользователь')
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
        verbose_name='Статус заказа'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Итоговая сумма')
    shipping_address = models.CharField(max_length=255, verbose_name='Адрес доставки')
    payment_method = models.CharField(max_length=50, verbose_name='Метод оплаты')
    note = models.TextField(blank=True, null=True, verbose_name='Примечания')
    delivery_method = models.ForeignKey(
        'DeliveryMethod',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Метод доставки'
    )
    coupon = models.ForeignKey(
        'Coupon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Купон'
    )

    def __str__(self):
        return f"Заказ {self.id} от {self.user.username}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')

    discount = models.ForeignKey(
        'Discount',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Знижка'
    )

    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказах'


class Payment(models.Model):
    order = models.OneToOneField('Order', on_delete=models.CASCADE, verbose_name='Замовлення')
    payment_method = models.CharField(max_length=50, verbose_name='Метод оплати')
    payment_status = models.CharField(
        max_length=20,
        choices=[('pending', 'Очікується'), ('completed', 'Завершено'), ('failed', 'Не вдалося')],
        default='pending',
        verbose_name='Статус оплати'
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплати')
    transaction_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='ID транзакції')

    def __str__(self):
        return f"Оплата для замовлення {self.order.id}"

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплати'


