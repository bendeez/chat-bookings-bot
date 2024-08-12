from app.tools.base_service import BaseService
from app.chat.models import Chat_Messages, Chat_Sessions
from app.chat.enums import ChatsAttributes, SessionAttributes
from app.tools.enums import DatabaseQueryOrder


class ChatService(BaseService):
    async def get_all_chat_logs(
        self,
        order: DatabaseQueryOrder,
        order_by: ChatsAttributes,
        limit: int = 100,
        offset: int = 0,
    ):
        chat_logs = await self.transaction.get_all(
            model=Chat_Messages,
            order_by=getattr(Chat_Messages, order_by.value),
            order=order,
            offset=offset,
            limit=limit,
        )
        return chat_logs

    async def get_chat_sessions(
        self,
        order: DatabaseQueryOrder,
        order_by: SessionAttributes,
        limit: int = 100,
        offset: int = 0,
    ):
        chat_sessions = await self.transaction.get_all(
            model=Chat_Sessions,
            limit=limit,
            offset=offset,
            order_by=getattr(Chat_Sessions, order_by.value),
            order=order,
        )
        return chat_sessions

    async def get_chat_logs_by_session_id(
        self,
        order: DatabaseQueryOrder,
        order_by: ChatsAttributes,
        session_id: str,
        limit: int = 100,
        offset: int = 0,
    ):
        chat_logs = await self.transaction.get_all(
            model=Chat_Messages,
            order_by=getattr(Chat_Messages, order_by.value),
            order=order,
            limit=limit,
            offset=offset,
            filter={Chat_Messages.session_id: session_id},
        )
        return chat_logs
