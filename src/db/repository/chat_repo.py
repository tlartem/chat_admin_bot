from db.interface import IChatRepo


class ChatRepo(IChatRepo):
    def __init__(self, session) -> None:
        self.session = session

    async def add_new_chat(self, chat_id: int, admin_id: int) -> None: ...

    async def find_chats_by_user(self, user_id: int) -> list[int]:
        # MOC
        return [-1002296805867]
