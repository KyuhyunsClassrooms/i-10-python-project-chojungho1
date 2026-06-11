# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 21021 조정호
# 프로젝트 주제: 영양소 분석 및 맞춤형 가상 식단 권장 프로그램


food_data = [
    ['닭가슴살', 165, 0, 31, 3],
    ['고구마', 128, 32, 1, 0],
    ['현미밥', 150, 33, 3, 1],
    ['연어구이', 200, 0, 25, 11],
    ['계란후라이', 90, 0, 7, 6],
    ['바나나', 93, 24, 1, 0]
]

def display_food_list(foods):
    
    print("\n--- [가상 식품 영양 성분 표] ---")
    for food in foods:
        print(f"음식명: {food[0]} | 칼로리: {food[1]}kcal | 탄수화물: {food[2]}g | 단백질: {food[3]}g | 지방: {food[4]}g")

def filter_menu(foods, choice):
  
    selected_foods = []
    for food in foods:
        carbs = food[2]
        protein = food[3]
        
        if choice == "1":    
            if protein >= 20:
                selected_foods.append(food)
        elif choice == "2":  
            if carbs >= 30:
                selected_foods.append(food)
                
    return selected_foods

display_food_list(food_data)

print("\n==================================")
print("가상 식단 추천 프로그램에 오신 것을 환영합니다!")
print("1: 다이어트 (고단백 추천)")
print("2: 벌크업 (고탄수화물 추천)")
print("==================================")

user_choice = input("원하는 식단 목적의 번호를 입력하세요 (1 또는 2): ")

recommend_recipe = filter_menu(food_data, user_choice)

if not recommend_recipe:
    print("\n[알림] 올바른 번호를 입력하지 않았거나 조건에 맞는 음식을 찾지 못했습니다.")
else:
    print("\n★ 맞춤형 가상 추천 식단 결과 ★")
    for item in recommend_recipe:
        print(f"- {item[0]} (탄수화물:{item[2]}g, 단백질:{item[3]}g)")

        display_food_list(food_data)

print("\n==================================")
print(" 가상 맞춤형 헬스케어 식단 프로그램 ")
print("==================================")

user_weight = float(input("가상 사용자의 체중(kg)을 입력하세요: "))
user_activity = input("가상 사용자의 활동량을 선택하세요 (1:낮음 / 2:보통 / 3:높음): ")

my_limit_calories = calculate_recommended_calories(user_weight, user_activity)
print(f"\n[분석 결과] 가상 사용자의 하루 권장 칼로리는 {my_limit_calories}kcal 입니다.")

meal_limit = my_limit_calories / 3
print(f"[안내] 한 끼 권장 제한 칼로리는 약 {meal_limit:.1f}kcal 입니다.")

print("\n1: 다이어트 (고단백 추천)")
print("2: 벌크업 (고탄수화물 추천)")
user_choice = input("원하는 식단 목적의 번호를 입력하세요 (1 또는 2): ")

recommend_recipe = filter_menu(food_data, user_choice, meal_limit)

if not recommend_recipe:
    print("\n[알림] 조건(한 끼 제한 칼로리 및 영양소 규칙)에 맞는 음식을 찾지 못했습니다.")
else:
    print(f"\n★ 한 끼 {meal_limit:.1f}kcal 이하 맞춤형 가상 추천 식단 ★")
    for item in recommend_recipe:
        print(f"- {item[0]} (칼로리:{item[1]}kcal | 탄수화물:{item[2]}g, 단백질:{item[3]}g)")