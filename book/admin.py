from django.contrib import admin
from book.models import BookSelf
# Register your models here.


# admin.site.register(BookSelf)
@admin.register(BookSelf)
class BookAdmin(admin.ModelAdmin):
    fields = ['title','description','price','publication_name','published_data_time','cover']
    list_display = ['title','publication_name']
    list_filter = ['published_data_time']
    list_per_page = 5
    search_fields = ['title','publication_name','price']