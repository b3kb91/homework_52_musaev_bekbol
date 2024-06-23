from django.db import models


class ToDo(models.Model):
    description = models.TextField(max_length=500, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name="Статус", default="new")
    date_completion = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="Дата выполнения")

    def __str__(self):
        return self.description


    class Meta:
        db_table = 'todo_lists'
        verbose_name = "Cписок задач"
        verbose_name_plural = "Списки задач"