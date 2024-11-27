import unittest
from app import start

class TestChessBot(unittest.TestCase):
    def test_start_message(self):
        update_mock = type('MockUpdate', (), {"effective_user": type('MockUser', (), {"id": 123, "username": "test_user"})})()
        context_mock = type('MockContext', (), {"bot": None})()

        async def test_coroutine():
            await start(update_mock, context_mock)

        # Проверяем, чтобы стартовая функция не вызывала ошибок
        try:
            import asyncio
            asyncio.run(test_coroutine())
        except Exception as e:
            self.fail(f"Test failed: {e}")

if __name__ == '__main__':
    unittest.main()
