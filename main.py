from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
import uvicorn

from deps.session import get_session
from services.user import get_user_by_id, user_is_exists
from services.order import add_order, get_order_by_id, get_user_orders
from models.scheme import OrderOutputScheme, UserOutputScheme, OrderInputScheme

app = FastAPI()


class NotFound(HTTPException):  # В реальном проекте стоит отправлять локацию поля, где возникла ошибка, как делает это делает fastapi при помощи pydantic
    def __init__(self, *args, **kwargs):
        return super().__init__(status_code=404, detail="Not Found", *args, **kwargs)


@app.get("/user/{user_id}/", response_model=UserOutputScheme)
async def get_user_detail(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user_by_id(session, user_id)
    if not user:
        raise NotFound()
    return user


@app.get("/user/{user_id}/orders/", response_model=List[OrderOutputScheme])
async def get_user_order_history(user_id: int, session: AsyncSession = Depends(get_session)):
    orders = await get_user_orders(session, user_id)
    if not orders:
        if await user_is_exists(session, user_id):
            raise NotFound()
    return orders


@app.post("/orders/", response_model=OrderOutputScheme)
async def create_order(order: OrderInputScheme, session: AsyncSession = Depends(get_session)):
    order_in_db = await add_order(
        session,
        order.user_id,
        [item.dict() for item in order.items]
    )
    try:
        await session.commit()
    except IntegrityError:
        raise NotFound()

    order_joined = await get_order_by_id(session, order_in_db.id)
    return order_joined


@app.get("/orders/{order_id}/", response_model=OrderOutputScheme)
async def get_order_detail(order_id: int, session: AsyncSession = Depends(get_session)):
    order = await get_order_by_id(session, order_id)
    if not order:
        raise NotFound()
    return order

if __name__ == '__main__':
    uvicorn.run("main:app", port=1111, host='127.0.0.1', reload=True)
