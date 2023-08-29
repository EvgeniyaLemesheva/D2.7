# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment
user1 = User.objects.create_user(username='user1', password='password1')
user2 = User.objects.create_user(username='user2', password='password2')
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)
category1 = Category.objects.create(name='Sport')
category2 = Category.objects.create(name='Political')
category3 = Category.objects.create(name='Education')
category4 = Category.objects.create(name='Technology')
post1 = Post.objects.create(author=author1, post_type='article', title='Заголовок статьи 1', content='Содержание статьи 1')
post2 = Post.objects.create(author=author2, post_type='article', title='Заголовок статьи 2', content='Содержание статьи 2')
post3 = Post.objects.create(author=author1, post_type='news', title='Заголовок новости', content='Содержание новости')
post1.categories.add(category1, category2)
post2.categories.add(category3, category4)
post3.categories.add(category2, category4)
comment1 = Comment.objects.create(post=post1, user=user1, text='Комментарий к статье 1')
comment2 = Comment.objects.create(post=post2, user=user2, text='Комментарий к статье 2')
comment3 = Comment.objects.create(post=post3, user=user1, text='Комментарий к новости')
comment4 = Comment.objects.create(post=post1, user=user2, text='Второй комментарий к статье 1')
post1.like()
post2.dislike()
comment1.like()
comment2.dislike()
author1.update_rating()
author2.update_rating()
best_author = Author.objects.order_by('-rating').first()
print(f'Лучший пользователь: {best_author.user.username}, рейтинг: {best_author.rating}')
best_post = Post.objects.order_by('-rating').first()
print(f'Дата: {best_post.created_at}')
print(f'Автор: {best_post.author.user.username}')
print(f'Рейтинг: {best_post.rating}')
print(f'Заголовок: {best_post.title}')
print(f'Превью: {best_post.preview()}')
comments_to_best_post = Comment.objects.filter(post=best_post)
for comment in comments_to_best_post:
    print(f'Дата: {comment.created_at}')
    print(f'Пользователь: {comment.user.username}')
    print(f'Рейтинг: {comment.rating}')
    print(f'Текст: {comment.text}')



