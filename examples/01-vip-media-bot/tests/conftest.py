from __future__ import annotations

from collections.abc import AsyncGenerator, AsyncIterator
from unittest.mock import AsyncMock, MagicMock

import pytest_asyncio
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.models.base import Base
from app.models.payment import Payment  # noqa: F401
from app.models.subscription import Subscription  # noqa: F401
from app.models.user import User  # noqa: F401


@pytest_asyncio.fixture
async def session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    factory = async_sessionmaker(engine, expire_on_commit=False)
    async with factory() as s:
        yield s
    await engine.dispose()


@pytest_asyncio.fixture
async def redis_mock() -> AsyncIterator[MagicMock]:
    redis = MagicMock()
    redis.get = AsyncMock(return_value=None)
    redis.set = AsyncMock(return_value=True)
    yield redis


@pytest_asyncio.fixture
async def bot_mock() -> AsyncIterator[MagicMock]:
    bot = MagicMock()
    bot.get_chat_member = AsyncMock()
    bot.create_invoice_link = AsyncMock(return_value="https://t.me/invoice/abc123")
    yield bot
