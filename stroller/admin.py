from django.contrib import admin

from .models import Stroller


@admin.register(Stroller)
class StrollerAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'updated_at']
    list_display_links = ['model_name']
    prepopulated_fields = {'slug': ('model_name',)}
    ordering = ['-updated_at', ]

    fieldsets = (
        ('Основне', {
            'fields': ('model_name', 'title_name', 'slug', 'description', 'features', 'title_image', 'is_featured',
                       'featured_photo', 'featured_description', 'price')
        }),
        ('Основні фото', {
            'fields': (
                'stroller_photo_1', 'stroller_photo_2', 'stroller_photo_3', 'stroller_photo_4',
                'stroller_photo_5', 'stroller_photo_6', 'stroller_photo_7', 'stroller_photo_8'
            ),
        }),
        ('Варіанти кольорів', {
            'fields': (
                'stroller_color_1', 'stroller_color_2', 'stroller_color_3', 'stroller_color_4',
                'stroller_color_5', 'stroller_color_6', 'stroller_color_7', 'stroller_color_8',
                'stroller_color_9', 'stroller_color_10', 'stroller_color_11', 'stroller_color_12',
                'stroller_color_13', 'stroller_color_14', 'stroller_color_15'
            ),
        }),
        ('Розміри і вага коляски', {
            'fields': ('weight_cradle', 'weight_walking_unit', 'weight_frame_with_wheels', 'width_frame',
                       'sized_stroller')
        }),
        ('Нижній Опис', {
            'fields': ('header_first', 'description_first', 'photo_first', 'header_second', 'description_second',
                       'photo_second', 'header_third', 'description_third', 'photo_third', 'header_fourth',
                       'description_fourth', 'photo_fourth')
        }),
        ('Галерея', {
            'fields': ('gallery_photo_1', 'gallery_photo_2', 'gallery_photo_3', 'gallery_photo_4', 'gallery_photo_5',
                       'gallery_photo_6', 'gallery_photo_7', 'gallery_photo_8')
        }),
    )
