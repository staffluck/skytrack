from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException

from deps.session import get_session
from services.user import get_user_by_id
from models.scheme import UserOutputScheme

app = FastAPI()


class NotFound(HTTPException):
    def __init__(self, *args, **kwargs):
        return super().__init__(status_code=404, detail="Not Found", *args, **kwargs)


@app.get("/user/{user_id}/", response_model=UserOutputScheme)
async def get_user_detail(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user_by_id(session, user_id)
    if not user:
        raise NotFound()
    return user

if __name__ == '__main__':
    uvicorn.run("main:app", port=1111, host='127.0.0.1', reload=True)
