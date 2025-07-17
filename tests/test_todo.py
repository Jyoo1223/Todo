

import unittest
from todo_logic import add_task, remove_task

class TestTodoLogic(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        tasks = add_task(tasks, "Task 1")
        print(f"Tasks after adding 1: {tasks}")
        self.assertEqual(tasks, ["Task 1"])

        tasks = add_task(tasks, "")
        print(f"Tasks after adding to empty string: {tasks}")
        self.assertEqual(tasks, ["Task 1"])

    def test_remove_task(self):
        tasks = ["Task 1", "Task 2"]
        tasks = remove_task(tasks, 0)
        print(f"Tasks after removing: {tasks}")
        self.assertEqual(tasks, ["Task 2"])

        tasks = remove_task(tasks, 5)
        print(f"Tasks after remove at invalid index 5: {tasks}")
        self.assertEqual(tasks, ["Task 2"])

if __name__ == "__main__":
    unittest.main()
