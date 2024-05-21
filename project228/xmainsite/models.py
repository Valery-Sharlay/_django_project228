from django.db import models
from django.urls import reverse


# def translit_to_eng(s: str) -> str:
#     d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
#          'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
#          'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
#          'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
#          'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}
#
#     return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(pc_pub=PcBase.PubStatus.PUBLISHED)


class PcBase(models.Model):
    class PubStatus(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    pc_model = models.CharField(max_length=55, blank=False, verbose_name='Модель *')
    pc_cpu = models.CharField(max_length=55, blank=True, verbose_name='Процессор')
    pc_disk_size = models.CharField(max_length=25, blank=True, verbose_name='Объем диска')
    pc_type = models.ForeignKey('PcType', on_delete=models.PROTECT,
                                related_name='pctypes')
    pc_about = models.TextField(blank=True, verbose_name='Описание')
    pc_date_add = models.DateField(auto_now_add=True, verbose_name='Время добавления')
    pc_date_update = models.DateField(auto_now=True, verbose_name="Время изменения")
    pc_pub = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), PubStatus.choices)),
                                 default=PubStatus.DRAFT, verbose_name='Статус Публикации')
    pc_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
                                 blank=True, null=True, verbose_name='Фото')
    pc_slug = models.SlugField(max_length=255, blank=False, unique=True, db_index=True, verbose_name='Slug URL *')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.pc_model

    class Meta:
        ordering = ['-pc_date_add']
        indexes = [models.Index(fields=['-pc_date_add'])]

    def get_absolute_url(self):
        # return reverse('pc_about', kwargs={'pc_slug': self.pc_slug})
        return reverse('pcabout', kwargs={'pc_slug': self.pc_slug})


class PcType(models.Model):
    pctype_name = models.CharField(max_length=100, db_index=True)
    pctype_slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.pctype_name

    def get_absolute_url(self):
        return reverse('pctype', kwargs={'pctype_slug': self.pctype_slug})
