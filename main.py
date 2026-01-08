#!/usr/bin/env python3
"""
Точка входа для Railway
"""
import sys
import os

# Добавляем текущую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Импортируем основной скрипт
    from rotenberg_bot import RotenbergBot, generate_session
    import asyncio
    import logging
    
    logging.basicConfig(level=logging.INFO)
    
    async def main():
        # Если есть аргумент для генерации сессии
        if len(sys.argv) > 1 and sys.argv[1] == "--generate-session":
            await generate_session()
        else:
            bot = RotenbergBot()
            await bot.start()
    
    if __name__ == "__main__":
        asyncio.run(main())
        
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    print("Убедитесь, что файл rotenberg_bot.py находится в той же директории")
    sys.exit(1)
except Exception as e:
    print(f"❌ Критическая ошибка: {e}")
    sys.exit(1)
