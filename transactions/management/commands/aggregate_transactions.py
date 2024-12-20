import time
from django.core.management.base import BaseCommand

from transactions.models import TransactionSummary


class Command(BaseCommand):
    help = ("""Using this command will aggregate transaction summaries and save them to transaction_summary collection.
    depending on amount of volume of Transactions it might take a while . . . """)

    def handle(self, *args, **kwargs):
        start_time = time.time()
        TransactionSummary.update_transaction_summary()
        end_time = time.time()
        self.stdout.write(self.style.SUCCESS(f'task successfully completed in {end_time-start_time}s 🎉'))
