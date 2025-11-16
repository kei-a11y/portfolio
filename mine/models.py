from django.db import models

class BestTime(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', '初級 (9x9, 10個)'),
        ('medium', '中級 (16x16, 40個)'),
        ('hard', '上級 (16x30, 99個)'),
    ]
    
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    time_seconds = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['difficulty', 'time_seconds']
    
    def __str__(self):
        return f"{self.get_difficulty_display()} - {self.time_seconds}秒"