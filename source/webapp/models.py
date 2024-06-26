from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class ToDo(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False, verbose_name="Описание")
    description_detail = models.TextField(max_length=500, null=True, blank=True, verbose_name="Подробное описание")
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name="Статус", default="new",
                              choices=status_choices)
    date_completion = models.DateField(null=True, blank=True, verbose_name="Дата выполнения")

    def __str__(self):
        return f"{self.description} {self.date_completion} {self.status} {self.description_detail}"

    class Meta:
        db_table = 'todo_lists'
        verbose_name = "Cписок задач"
        verbose_name_plural = "Списки задач"
