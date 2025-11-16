from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
import random
from .models import BestTime

DIFFICULTY_SETTINGS = {
    'easy': {'rows': 9, 'cols': 9, 'mines': 10},
    'medium': {'rows': 16, 'cols': 16, 'mines': 40},
    'hard': {'rows': 16, 'cols': 30, 'mines': 99},
}

def index(request):
    """難易度選択画面"""
    best_times = {}
    for difficulty in ['easy', 'medium', 'hard']:
        best = BestTime.objects.filter(difficulty=difficulty).first()
        best_times[difficulty] = best.time_seconds if best else None
    
    return render(request, 'mine/index.html', {'best_times': best_times})

def game(request, difficulty):
    """ゲーム画面"""
    if difficulty not in DIFFICULTY_SETTINGS:
        difficulty = 'easy'
    
    settings = DIFFICULTY_SETTINGS[difficulty]
    best_time = BestTime.objects.filter(difficulty=difficulty).first()
    
    context = {
        'difficulty': difficulty,
        'rows': settings['rows'],
        'cols': settings['cols'],
        'mines': settings['mines'],
        'best_time': best_time.time_seconds if best_time else None,
    }
    
    return render(request, 'mine/game.html', context)

@require_http_methods(["POST"])
def save_time(request):
    """クリア時間を保存"""
    try:
        data = json.loads(request.body)
        difficulty = data.get('difficulty')
        time_seconds = data.get('time_seconds')
        
        if difficulty not in DIFFICULTY_SETTINGS:
            return JsonResponse({'error': '無効な難易度です'}, status=400)
        
        # ベストタイムの取得
        best_time = BestTime.objects.filter(difficulty=difficulty).first()
        is_new_record = False
        
        # 新記録の場合のみ保存
        if not best_time or time_seconds < best_time.time_seconds:
            BestTime.objects.create(
                difficulty=difficulty,
                time_seconds=time_seconds
            )
            is_new_record = True
        
        return JsonResponse({
            'success': True,
            'is_new_record': is_new_record,
            'best_time': time_seconds if is_new_record else (best_time.time_seconds if best_time else None)
        })
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)