# from asyncio import current_task
#
# from sqlalchemy.ext.asyncio import (
#     create_async_engine,  # функция для управления операциями сохранения объектов, сопоставленных с ORM
#     async_sessionmaker,  # асинхронный класс-построитель Session
#     async_scoped_session,
#     AsyncSession,
# )
#
# from app.core.config import settings
#
#
# # движок для взаимодействия с БД, описание подключения к БД
# class DBHelper:
#     def __init__(self, url: str, echo: bool = False):
#         self.engine = create_async_engine(url=url, echo=echo)  # движок
#         self.session_factory = async_sessionmaker(
#             bind=self.engine,  # привязывает сессию бд к движку, который применяется для установки подключения
#             autoflush=False,
#             autocommit=False,
#             expire_on_commit=False,
#         )
#         # autoflush - подготовка к коммиту. При True автоматически вызывается Session.flush() записывающий все изменения
#         # expire_on_commit - авто удаление инфы о текущих объектах и сессии
#
#     # определение зависимости для получения актуальной сессии
#     def get_scoped_session(self):
#         session = async_scoped_session(
#             session_factory=self.session_factory,
#             scopefunc=current_task,  # указываем правила для получения текущего пространства, которым ограничена сессия
#         )
#
#         return session
#
#     # метод создающий сессию для каждого запроса. Объявили объект через который будем работать с асинх-й БД
#     async def session_dependency(self) -> AsyncSession:
#         async with self.session_factory() as s:
#             yield s  # чтобы сессия не закрылась при покидании контекста, отдаем ее
#             await s.close()
#
#     async def scoped_session_dependency(self) -> AsyncSession:
#         session = self.get_scoped_session()
#         yield session
#         await session.close()
#
#
# db_helper = DBHelper(
#     url=settings.db_url,
#     echo=settings.db_echo,
# )
