from fastapi import APIRouter

router = APIRouter()

@router.get('/t')
async def test():
    return JSONResponse({
        "message" : "welcome Bro!"
    })