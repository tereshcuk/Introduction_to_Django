import pytest
from django.test import Client
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course

# def test_example():
#     assert True, "Just test example"

@pytest.fixture
def client():
    return Client()
    # return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    
    return factory  

# проверка получения первого курса (retrieve-логика):
@pytest.mark.django_db
def test_receipt_first_course(client, course_factory):
    
    # Arrange — готовим данные     
    сourse_name = 'физика'
    course = course_factory(id = 1, name=сourse_name)    
    
    # Act — совершаем действие, которое хотим протестировать
    response  = client.get('/api/v1/courses/' , {'id': 1}, content_type='application/json')        
    assert response.status_code==200    
    data = response.json()       
    assert data[0]['name']== сourse_name
    

@pytest.mark.django_db
def test_checking_list_courses(client, course_factory):
    # Arrange — готовим данные
    quantity=10      
    course = course_factory(_quantity = quantity)    
    
    # Act — совершаем действие, которое хотим протестировать
    response  = client.get('/api/v1/courses/')        
    
    # Assert — проверяем результат    
    assert response.status_code==200
    data = response.json()
    assert len(data) == len(course)
   
   
@pytest.mark.django_db   
def test_filtering_course_list(course_factory):
    # Arrange — готовим данные
    course_1 = course_factory(id=1, name='Физика')
    course_2 = course_factory(id=2, name='Математика')
    course_3 = course_factory(id=3, name='Химия')
             
    # Act — совершаем действие, которое хотим протестировать     
    my_curs_id = Course.objects.get(id = course_2.id)    
    my_curs_name = Course.objects.get(name = course_3.name)      
    
    # Assert — проверяем результат    
    assert my_curs_id.id==course_2.id
    assert my_curs_id.id==2
    
    assert my_curs_name.name==course_3.name
    assert my_curs_name.name== 'Химия'
    
    
@pytest.mark.django_db    
def test_course_creation(client):
    
    # Arrange — готовим данные
    my_data ={
        "id": 1,
        "name": "Физика",
        "students": []
       }
             
    # Act — совершаем действие, которое хотим протестировать     
    response  = client.post('/api/v1/courses/' , my_data, content_type='application/json')  
    
    # Assert — проверяем результат 
    assert response.status_code==201 
    
    
@pytest.mark.django_db    
def test_course_updates(client, course_factory):
    
    # Arrange — готовим данные
    my_id = 1
    course = course_factory(id=my_id, name='Физика')    
    my_data ={
        "id": 1,
        "name": "Математика",
        "students": []
       }
             
    # Act — совершаем действие, которое хотим протестировать     
    response  = client.patch(f'/api/v1/courses/{my_id}/', my_data, content_type='application/json')  
    
    # Assert — проверяем результат 
    assert response.status_code==200
    
@pytest.mark.django_db    
def test_course_delete(client, course_factory):
    
    # Arrange — готовим данные
    my_id = 1
    course = course_factory(id=my_id, name='Физика')

    
    # my_data = {'id': 1, 'name': 'Математика'}
             
    # Act — совершаем действие, которое хотим протестировать     
    response  = client.delete(f'/api/v1/courses/{my_id}/')  
    
    # Assert — проверяем результат 
    assert response.status_code==204             
    
        
           
    
    
    
 
        
        
        