from unittest import TestCase

from t_d_list.models import Tag, Task


class ModelsTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertTrue(isinstance(tag, Tag))
        self.assertEqual(tag.str(), tag.name)

    def test_task_creation(self):
        task = Task.objects.create(content="Test Content",
                                   deadline="2024-03-10 12:00")
        self.assertTrue(isinstance(task, Task))
        self.assertEqual(task.str(), f"Content: {task.content}")
