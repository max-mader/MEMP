import unittest
from create_memp import extract_first_paragraph, formulate_memp, generate_bullet_points

class TestCreateMEMP(unittest.TestCase):
    def test_extract_first_paragraph(self):
        response = "To generate creative images using AI tools, it's crucial to provide detailed, vivid descriptions and specify the desired style or influence. Understanding the capabilities and limitations of the specific AI tool you're using is also important, as different tools may require different approaches for optimal results."
        expected_first_paragraph = "To generate creative images using AI tools, it's crucial to provide detailed, vivid descriptions and specify the desired style or influence."
        first_paragraph = extract_first_paragraph(response)
        self.assertEqual(first_paragraph, expected_first_paragraph)

    def test_formulate_memp(self):
        first_paragraph = "To generate creative images using AI tools, it's crucial to provide detailed, vivid descriptions and specify the desired style or influence."
        expected_memp = "Given the importance of detailed descriptions and specifying styles for optimal results in creative image generation, how can one leverage specific AI tool capabilities effectively?"
        memp = formulate_memp(first_paragraph)
        self.assertEqual(memp, expected_memp)

    def test_generate_bullet_points(self):
        first_paragraph = "To generate creative images using AI tools, it's crucial to provide detailed, vivid descriptions and specify the desired style or influence."
        expected_bullet_points = [
            "Incorporates the model's emphasis on detailed, vivid descriptions and style specification.",
            "Highlights the need for understanding AI tool capabilities to enhance creative outcomes.",
            "Acts as a refined query that aligns with the model's perceived optimal approach."
        ]
        bullet_points = generate_bullet_points(first_paragraph)
        self.assertEqual(bullet_points, expected_bullet_points)

if __name__ == '__main__':
    unittest.main()