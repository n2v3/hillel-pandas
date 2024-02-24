from dataclasses import dataclass
import random
from datetime import datetime, timedelta
from typing import List

import faker

fake = faker.Faker('uk_UA')


@dataclass
class RestaurantReview:
    id: int
    restaurant_name: str
    reviewer_name: str
    review_text: str
    rating: int
    date_of_visit: str
    location: str


def generate_restaurant_reviews(num_reviews=500) -> List[RestaurantReview]:
    restaurant_reviews = []

    end_date = datetime.now()
    start_date = end_date - timedelta(days=365 * 2)

    custom_word_list = [
        "Буфет", "Пʼяна вишня", "Пузата хата",
        "Львівська майстерня", "Сто років тому вперед", "Shoco",
        "Sowa", "Копальня кави", "Львівська мануфактура кави",
        "Друзі", "Колос", "Реберня", "Всі свої",
        "Домашка", "Штрудель",
    ]
    custom_review_phrases = [
        "Дуже смачна кухня та привітний персонал.",
        "Чудова атмосфера та швидке обслуговування.",
        "Рекомендую це місце для гарного вечора",
        "Смачні страви за доступною ціною.",
        "Приємна музика та оригінальний інтер'єр.",
        "Не вражений обслуговуванням та якістю їжі.",
        "Завжди свіжі продукти та широкий вибір страв.",
        "Веселе місце для зустрічей та вечірок.",
        "Швидке приготування та гарний вигляд страв.",
        "Невідповідний сервіс та дорогі ціни на меню."
    ]

    for i in range(num_reviews):
        gender = fake.random_int(min=0, max=1)
        first_name = fake.first_name_male() if gender == 1 else fake.first_name_female()
        last_name = fake.last_name()

        review = RestaurantReview(
            id=i,
            restaurant_name=fake.word(ext_word_list=custom_word_list),
            reviewer_name=f'{first_name} {last_name}',
            review_text=fake.random_element(elements=custom_review_phrases),
            rating=random.randint(1, 5),
            date_of_visit=fake.date_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d'),
            location=fake.city_name()
        )
        restaurant_reviews.append(review)

    # For the 1% of random reviews, set the rating value to 0
    for review in random.sample(restaurant_reviews, k=int(len(restaurant_reviews) * 0.01)):
        review.rating = 0

    return restaurant_reviews


def save_restaurant_reviews_to_csv(restaurant_reviews: List[RestaurantReview]):
    with open('restaurant_reviews.csv', 'w') as f:
        f.write('id,restaurant_name,reviewer_name,review_text,rating,date_of_visit,location\n')

        for review in restaurant_reviews:
            f.write(
                f'{review.id},{review.restaurant_name},{review.reviewer_name},{review.review_text},{review.rating},{review.date_of_visit},{review.location}\n')


if __name__ == '__main__':
    restaurant_reviews = generate_restaurant_reviews()
    save_restaurant_reviews_to_csv(restaurant_reviews)
