from django.db import models
from django.core.validators import MinValueValidator

# Модель для товара
class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Назва товару'  # Переводим название поля на украинский язык
    )  # Название товара
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Опис товару'  # Переводим описание на украинский язык
    )  # Описание товара
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],  # Валидация цены (не может быть меньше 0)
        verbose_name='Ціна товару'  # Переводим на украинский
    )  # Цена товара
    store = models.ForeignKey(
        'Store',
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Магазин'  # Переводим на украинский
    )  # Связь с магазином
    category = models.ForeignKey(
        'Category',
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Категорія товару'  # Переводим на украинский
    )  # Связь с категорией
    stock_quantity = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],  # Валидация (не может быть меньше 0)
        verbose_name='Кількість на складі'  # Переводим на украинский
    )  # Количество товара в наличии
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення товару'  # Переводим на украинский
    )  # Дата добавления товара
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата останнього оновлення товару'  # Переводим на украинский
    )  # Дата последнего обновления товара

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


# Модель для категории товаров
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Назва категорії'  # Переводим на украинский
    )  # Название категории
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Опис категорії'  # Переводим на украинский
    )  # Описание категории
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення категорії'  # Переводим на украинский
    )  # Дата создания категории
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата останнього оновлення категорії'  # Переводим на украинский
    )  # Дата последнего обновления категории

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


# Модель для магазина
class Store(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Назва магазину'  # Переводим на украинский
    )  # Название магазина
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Опис магазину'  # Переводим на украинский
    )  # Описание магазина (необязательное)
    address = models.CharField(
        max_length=255,
        verbose_name='Адреса магазину'  # Переводим на украинский
    )  # Адрес магазина
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Номер телефону'  # Переводим на украинский
    )  # Номер телефона (необязательное)
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name='Електронна пошта'  # Переводим на украинский
    )  # Электронная почта (необязательное)
    website = models.URLField(
        blank=True,
        null=True,
        verbose_name='Веб-сайт'  # Переводим на украинский
    )  # Веб-сайт магазина (необязательное)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення магазину'  # Переводим на украинский
    )  # Дата создания записи
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата останнього оновлення магазину'  # Переводим на украинский
    )  # Дата последнего обновления записи

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазини'

class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name='Назва постачальника')
    contact_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Контактна особа')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')
    email = models.EmailField(blank=True, null=True, verbose_name='Електронна пошта')
    address = models.TextField(blank=True, null=True, verbose_name='Адреса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Постачальник'
        verbose_name_plural = 'Постачальники'


class Warehouse(models.Model):
    name = models.CharField(max_length=200, verbose_name='Назва складу')
    location = models.TextField(verbose_name='Розташування')
    manager = models.CharField(max_length=200, blank=True, null=True, verbose_name='Менеджер складу')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склади'
