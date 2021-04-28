from django.db import models
from django.urls import reverse


# Курс має мати наступні атрибути:
# * Назва
# * Дата початку
# * Дата закінчення
# * Кількість лекцій


class Course(models.Model):
    """
    Model representing a course
    """
    title = models.CharField(max_length=255, verbose_name='Название курса', help_text="Введите название курса")
    start_date = models.DateField(verbose_name='Начало курса', help_text="Укажите дату начала курса")
    end_date = models.DateField(verbose_name='Конец курса', help_text="Укажите дату окончания курса")
    number_of_lectures = models.PositiveIntegerField(max_length=3, verbose_name='Количество лекций', help_text='Укажите количество лекций')
    description = models.TextField(verbose_name='Описание курса', help_text='Добавьте описание курса')

    # Methods
    def __str__(self):
        # String for representing the Model object.
        return self.title

    def get_absolute_url(self):
        # Returns the url to access a particular course instance.
        return reverse('course_detail', args=[str(self.id)])