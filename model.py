def get_ai_suggestion(income, expense):
    if income == 0:
        return "Please enter income"
    
    savings = income - expense
    percent = (expense / income) * 100

    if percent > 80:
        return f"High spending! You spent {percent:.0f}%. Savings only Rs.{savings}. Try to cut 20% on food/entertainment."
    elif percent > 50:
        return f"Balanced. You spent {percent:.0f}%. Savings Rs.{savings}. Good, invest Rs.{savings/2:.0f} in SIP."
    else:
        return f"Excellent! You spent only {percent:.0f}%. Savings Rs.{savings}. You are financially smart!"
