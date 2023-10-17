from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Numbers(BaseModel):
      num1: float
      num2: float
@app.post('/сложение')
def add(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {'результат': result}
@app.post('/вычитание')
def subtract(numbers: Numbers):
    result = numbers.num1 - numbers.num2
    return {'результат': result}
@app.post('/умножение')
def multiply(numbers: Numbers):
    result = numbers.num1 * numbers.num2
    return {'результат': result}
@app.post('/деление')
def divide(numbers: Numbers):
    if numbers.num2 == 0:
        return {'error':'You can not divide by zero' }
    result = numbers.num1 / numbers.num2
    return {'результат': result}