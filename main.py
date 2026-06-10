# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 21021 조정호
# 프로젝트 주제: 영양소 분석 및 맞춤형 가상 식단 권장 프로그램



# ==========================================
# 1. 데이터 저장 공간 (2차원 리스트)
# ==========================================
food_data = [
    ['닭가슴살', 165, 0, 31, 3],
    ['고구마', 128, 32, 1, 0],
    ['현미밥', 150, 33, 3, 1],
    ['연어구이', 200, 0, 25, 11],
    ['계란후라이', 90, 0, 7, 6],
    ['바나나', 93, 24, 1, 0]
]

# ==========================================
# 2. 기능별 함수 선언 정의 (def)
# ==========================================

def display_food_list(foods):
    """전체 식품 목록을 보여주는 함수"""
    print("\n--- [가상 식품 영양 성분 표] ---")
    for food in foods:
        print(f"음식명: {food[0]} | 칼로리: {food[1]}kcal | 탄수화물: {food[2]}g | 단백질: {food[3]}g | 지방: {food[4]}g")

def filter_menu(foods, choice):
    """사용자가 선택한 목적(1 또는 2)에 맞게 음식을 골라내는 함수"""
    selected_foods = []
    for food in foods:
        carbs = food[2]
        protein = food[3]
        
        if choice == "1":    # 다이어트 선택 시 단백질 20g 이상
            if protein >= 20:
                selected_foods.append(food)
        elif choice == "2":  # 벌크업 선택 시 탄수화물 30g 이상
            if carbs >= 30:
                selected_foods.append(food)
                
    return selected_foods

# ==========================================
# 3. 실제 프로그램이 실행되는 부분 (Main 흐름)
# ==========================================

# (1) 전체 음식 목록 보여주기 함수 호출
display_food_list(food_data)

print("\n==================================")
print("가상 식단 추천 프로그램에 오신 것을 환영합니다!")
print("1: 다이어트 (고단백 추천)")
print("2: 벌크업 (고탄수화물 추천)")
print("==================================")

# (2) 사용자 입력 받기
user_choice = input("원하는 식단 목적의 번호를 입력하세요 (1 또는 2): ")

# (3) 필터링 함수를 호출해서 결과 받기
recommend_recipe = filter_menu(food_data, user_choice)

# (4) 최종 결과 화면에 출력하기
if not recommend_recipe:
    print("\n[알림] 올바른 번호를 입력하지 않았거나 조건에 맞는 음식을 찾지 못했습니다.")
else:
    print("\n★ 맞춤형 가상 추천 식단 결과 ★")
    for item in recommend_recipe:
        print(f"- {item[0]} (탄수화물:{item[2]}g, 단백질:{item[3]}g)")