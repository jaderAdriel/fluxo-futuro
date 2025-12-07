from django.shortcuts import render
from django.db.models import Sum
from datetime import date
from apps.finance.models import Transaction
from apps.events.models import Event
from apps.meetings.models import Meeting

def index(request):
    today = date.today()

    income = Transaction.objects.filter(type="IN")
    expenses = Transaction.objects.filter(type="OUT")

    total_income = income.aggregate(total=Sum("amount"))["total"] or 0
    total_expenses = expenses.aggregate(total=Sum("amount"))["total"] or 0
    balance = total_income - total_expenses

    amount_events_this_month = Event.objects.count()
    amount_next_events = Event.objects.filter(date__gt=today)
    amount_meetings_this_month = Meeting.objects.filter(
        date__year=today.year,
        date__month=today.month
    )

    last_transactions = Transaction.objects.order_by("-date")[:6]
    next_meetings = Meeting.objects.filter(date__gte=today).order_by("date")[:6]

    context = {
        'income': income,
        'expenses': expenses,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
        'amount_next_events': amount_next_events,
        'amount_events_this_month': amount_events_this_month,
        'amount_meetings_this_month': amount_meetings_this_month,
        'last_transactions': last_transactions,
        'next_meetings': next_meetings,
    }

    return render(request, 'dashboard.html', context)
