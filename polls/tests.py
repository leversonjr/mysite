import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuetionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        ''' Was_published_recently () retorna False para perguntas cujas pub_date está no futuro'''

        time = timezone.now()+datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

