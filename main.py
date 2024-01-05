from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,FileResponse
import plot,gf,gf2
import numpy as np
#import pandas as pd

app = FastAPI()

plot.plot1()
gf.gf1()
result=gf2.values()
print(list(result))
result = [np.array(sublist).tolist() for sublist in result]

class Year(BaseModel):
    year: int

@app.post("/sendyear")
async def submit_year(year: Year):
    index=year.year
    print(index)
    #print(result[index])
    return {"message": [result[0][index],result[1][index],result[2][index],result[3][index]]}

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # List of image paths
    image_paths = [
        "upload/predicted_rates_graph1.png",
        "upload/predicted_rates_graph1.png",
        "upload/predicted_rates_graph3.png",
        "upload/predicted_rates_graph4.png",
        "upload/main.png",
    ]

    # Render the HTML template and pass the list of image paths
    return templates.TemplateResponse("index.html", {"request": request, "image_paths": image_paths})

@app.get("/get_image/{image_name}")
async def get_image(image_name: str):
    # Path to the image inside the upload directory
    image_path = f"upload/{image_name}"
    return FileResponse(image_path, media_type="image/jpeg")