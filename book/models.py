from django.db import models

# Create your models here.
# we have to pay attention to the order during making models
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True,null=True)
    isbn_13 = models.CharField(max_length=13, blank=True,null=True)



class BookSelf(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, default='')
    description = models.TextField(max_length=500, blank=True, null=True, default='')
    price = models.DecimalField(default=0,decimal_places=2,max_digits=10) #price will always be DecimalField or FloatField
    # published = models.DateTimeField() #we can do this separetely for date and time field with DateField and TimeField
    publication_name = models.CharField(max_length=120, blank=True, null=True, default='')
    published_data_time = models.DateTimeField(auto_now=True, null=True)
    cover = models.FileField(upload_to='cover/', default='')
    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_table'
    
    def __str__(self):
        return self.title + ' | ' + str(self.pk)


