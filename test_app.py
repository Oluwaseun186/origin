import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Now import app
from app import TaskManager
import pytest

class TestTaskManager:
    def test_add_task(self):
        manager = TaskManager()
        manager.add_task("Test task")
        assert len(manager.tasks) == 1
        assert manager.tasks[0]["task"] == "Test task"
        assert manager.tasks[0]["completed"] == False

    def test_complete_task(self):
        manager = TaskManager()
        manager.add_task("Test task")
        manager.complete_task(0)
        assert manager.tasks[0]["completed"] == True

    def test_delete_task(self):
        manager = TaskManager()
        manager.add_task("Test task")
        manager.delete_task(0)
        assert len(manager.tasks) == 0

if __name__ == "__main__":
    pytest.main()
