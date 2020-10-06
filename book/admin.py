from django.contrib import admin
from book.models import BookSelf, BookNumber, Character, Author
# Register your models here.


# admin.site.register(BookSelf)
@admin.register(BookSelf)
class BookAdmin(admin.ModelAdmin):
    fields = ['title','description','price','publication_name','published_data_time','number','cover']
    list_display = ['title','publication_name']
    list_filter = ['published_data_time']
    list_per_page = 5
    readonly_fields = ['published_data_time']
    search_fields = ['title','publication_name','price']


@admin.register(BookNumber)
class Number(admin.ModelAdmin):
    fields = ['isbn_10','isbn_13']
    list_display = [
        'isbn_10',
        'isbn_13'
    ]


admin.site.register(Character)
admin.site.register(Author)
