from fastapi import FastAPI, HTTPException
from models import ProductCreate, ProductUpdate
from database import supabase

app = FastAPI()

# python -m uvicorn main:app --reload

@app.get("/")
def home () :
    return {"message": "First FastAPI+SupaBase Project"}

@app.post("/product")
def create_product(product : ProductCreate):
    try:
        res =supabase.table("products").insert(
            product.dict()
        ).execute() 
        
        return {
            "message": "Product created successfully",
            "product": res.data[0]
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/products")   
def getProducts():
    res = supabase.table("products").select("*").execute()
    return res.data     

@app.get("/product/{id}")
def getProductById(id : int):
    res = supabase.table("products").select("*").eq("id",id).execute()
    return res.data[0]

@app.get("/getPrice")
def getTotalPrice():
    res = supabase.table("products").select("price").execute()
    lt = []
    for i in res.data:
        lt.append(i["price"])
    return sum(lt)
