A1 = {
    "機構組織架構": ["組織架構", "組織機構", "行政組織"],
    "業務執掌": ["業務", "職掌", "權責"],
    "工作流程": ["工作流程", "作業程序"],
    "緊急事件": ["緊急事件", "災害事件", "應變措施"],
    "聯繫": ["聯繫", "溝通", "協調"],
    "防火衛教": ["防火", "火災", "消防設施"],
    "吸菸及情緒不穩住民之防範措施": ["吸菸", "情緒不穩", "暴力事件", "自殺"],
    "危險物品保管": ["危險物品", "保管", "儲存"],
    "工作人員權益": ["勞動法令", "勞動條件", "勞動安全"],
    "差假制度": ["休假", "請假", "出勤"],
    "教育訓練": ["教育訓練", "培訓課程", "學習計畫"],
    "薪資給付": ["薪資", "給付", "津貼"],
    "退休撫恤": ["退休", "撫恤", "退職"],
    "申訴制度": ["申訴", "申訴管道", "申訴程序"],
    "考核獎勵制度": ["考核", "獎勵", "評鑑"],
    "勞健保": ["勞工健保", "健康檢查", "醫療保險"],
    "身心健康": ["身心健康", "心理輔導", "職業病防治"]
}


import json

with open('keywords/A1', 'w', encoding='utf-8') as f:
    json.dump(A1, f, ensure_ascii=False, indent=4)
