from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Expense, Balance
import json
from django.db.models import F


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            mobile_number=data.get('mobile_number')
        )
        return JsonResponse({'message': 'User created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def add_expense(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        amount = data.get('amount')
        expense_type = data.get('expense_type')
        participants = data.get('participants')
        
        if expense_type == 'EQUAL':
            num_participants = len(participants)
            split_amount = round(amount / num_participants, 2)

            for participant in participants:
                expense = Expense.objects.create(
                    user_id=user_id,
                    amount=split_amount,
                    expense_type=expense_type,
                    participants_data={participant: split_amount}
                )
                
                balance = Balance.objects.create(
                    user_id=user_id,
                    with_user_id=participant,
                    amount=split_amount
                )

        elif expense_type == 'EXACT':
            total_share = sum(participants.values())
            if total_share != amount:
                return JsonResponse({'error': 'Total share does not match the expense amount'}, status=400)
            for participant, share in participants.items():
                expense = Expense.objects.create(
                    user_id=user_id,
                    amount=share,
                    expense_type=expense_type,
                    participants_data={participant: share}
                )
                
                balance = Balance.objects.create(
                    user_id=user_id,
                    with_user_id=participant,
                    amount=share
                )
                
        elif expense_type == 'PERCENT':
            total_percent = sum(participants.values())
            if total_percent != 100:
                return JsonResponse({'error': 'Total percentage does not equal 100'}, status=400)
            for participant, percent in participants.items():
                share = round((percent / 100) * amount, 2)
                expense = Expense.objects.create(
                    user_id=user_id,
                    amount=share,
                    expense_type=expense_type,
                    participants_data={participant: share}
                )
                
                balance = Balance.objects.create(
                    user_id=user_id,
                    with_user_id=participant,
                    amount=share
                )
        
        return JsonResponse({'message': 'Expense added successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_user_expenses(request, user_id):
    user = User.objects.get(pk=user_id)
    expenses = Expense.objects.filter(user=user)
    expense_data = [{'amount': expense.amount, 'expense_type': expense.expense_type, 'participants_data': expense.participants_data} for expense in expenses]
    return JsonResponse(expense_data, safe=False)

def get_user_balances(request, user_id):
    balances_data = list(
        Balance.objects
        .filter(with_user_id=user_id)
        .annotate(expense_created_by=F('user_id__name'), expense_owed_by=F('with_user_id__name'))
        .values('expense_created_by', 'expense_owed_by', 'amount')
    )
    return JsonResponse(balances_data, safe=False)
