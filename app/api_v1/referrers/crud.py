# нужен объект сессии через который будем запрашивать данные из БД
from sqlalchemy.ext.asyncio import AsyncSession

from app.api_v1.referrers.schemas import ReferrerCreate, Referrer


async def create_referrer(
    session: AsyncSession,
    referrer_in: ReferrerCreate,
) -> Referrer:
    referrer = Referrer(**referrer_in.model_dump())
    session.add(referrer)

    await session.commit()  # т.к взаимодействие с БД асинхронное, то здесь будет await
    await session.refresh(referrer)
    # Может пригодиться обновл-е объекта перед return, т.к expire_on_commit=False. Объект будет в том состоянии, в
    # котором его сохранили. В синхронной алхимии по умолчанию все св-ва сгорают когда делаем коммит, а потом когда
    # к нему обращаемся, то объект запрашивается заново. Т.к запрос из БД - это асинхронное взаимодействие, то запрос
    # не может автоматически пройти и будет ошибка, поэтому либо обновляем вручную, либо работаем с неактуальными
    # данными. Данные могут стать неактуальными, когда при сохранении объекта в БД происходят изменения.

    return referrer
