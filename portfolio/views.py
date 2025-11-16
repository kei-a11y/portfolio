from django.shortcuts import render

def game_select(request):
    """ゲーム選択画面"""
    return render(request, 'game_select.html')