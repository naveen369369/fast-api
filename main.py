from fastapi import FastAPI ,UploadFile,Query ,File
from pydantic import BaseModel ,Field
from typing import Optional ,List

app=FastAPI()

   #Using GET

@app.get("/display")
def view (place:str = Query(min_length=3,max_length=50,regex="^[a-zA-Z]+$")
          ,name:str  = Query(min_length=1,max_length=1,regex="^[a-zA-Z]+$")):
    result=[]
    for e in employee:
      if e['place'].lower()==place.lower() or e['name'][0].lower()==name.lower():
         result.append(e)

    if result:
       return result
    else:
     return "xxx Not having xxx"
    
 # Using POST

class items(BaseModel):
    name: str =  Field(min_length=3,max_length=50,pattern="^[a-zA-Z]+$")
    age: int = Field(gt=18,lt=35)
    status: Optional[bool] = None



@app.post("/fileUpload")
async def fileupload(fileUp: List[UploadFile]=File(...)):
    result=[]
    for f in fileUp:

     text= await f.read()

     try:
        text_p=text.decode("utf-8")[:200]

     except:
        text_p="No Data Found"

     result.append({
        "File Name ":f.filename,
        "File Type ":f.content_type,
        "File Size ":len(text),
        "Text ":text_p
    })
    return result



@app.post('/display')
def view(data:items):
    return f"message: Items Received : {data}"

employee=[{'id':101,'name':'naveen','place':'Karur'},
          {'id':102,'name':'Guna','place':'Chennai'},
          {'id':103,'name':'Prakash','place':'Dubai'},
          {'id':104,'name':'priya','place':'Karur'},
          {'id':106,'name':'nakesh','place':'Karur'},
          {'id':107,'name':'ashwin','place':'Karur'},
          ]
    
@app.post("/fedback/")
def feed(name:str,age:int,gender:str,depart:str):
    return f' "Name ":{name}, "Age ":{age},"Gender ":{gender},"Department":{depart} '

