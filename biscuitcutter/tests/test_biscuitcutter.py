import os
import shutil
import tempfile
import unittest
from unittest.mock import patch

# Import your script. Ensure the file is named biscuitcutter.py 
# and is in the same directory, or adjust the import path accordingly.
from biscuitcutter import biscuitcutter

class TestBiscuitcutterSmoke(unittest.TestCase):
    def setUp(self):
        """Set up a temporary directory and ensure a template.zip exists."""
        # Create a temporary directory to act as our output_dir
        self.test_dir = tempfile.mkdtemp()
        
        # Locate where biscuitcutter expects template.zip to be
        self.module_dir = os.path.dirname(os.path.abspath(biscuitcutter.__file__))
        self.zip_path = os.path.join(self.module_dir, 'template.zip')
        
        # If template.zip doesn't exist in the CI environment, generate a stub for testing
        self.created_dummy_zip = False
        if not os.path.exists(self.zip_path):
            biscuitcutter._create_stub_zip(self.zip_path, biscuitcutter.TEMPLATE_PLACEHOLDER_REPO)
            self.created_dummy_zip = True

    def tearDown(self):
        """Clean up the temporary directory and dummy zip after the test runs."""
        shutil.rmtree(self.test_dir)
        
        # Only delete the zip if we created it during this test
        if self.created_dummy_zip and os.path.exists(self.zip_path):
            os.remove(self.zip_path)

    @patch('builtins.input')
    def test_smoke_scaffold_repo(self, mock_input):
        """Test the end-to-end scaffolding process without human interaction."""
        
        # 1. Define the simulated user inputs
        repo_name = "ci_test_repo"
        author = "CI Runner"
        email = "ci@example.com"
        github = "ci_user"
        
        # Map the mock inputs to the exact sequence biscuitcutter prompts for
        mock_input.side_effect = [
            repo_name,      # Repository / package name
            author,         # Author full name
            email,          # Author e-mail
            github,         # GitHub username
            self.test_dir,  # Parent directory
        ]

        # 2. Execute the main CLI flow
        biscuitcutter.main()

        # 3. Assertions & Validations
        expected_repo_path = os.path.join(self.test_dir, repo_name)
        
        # Verify the root directory was created
        self.assertTrue(
            os.path.exists(expected_repo_path), 
            "Smoke test failed: Repository directory was not created."
        )

        # Verify directory and file renaming logic worked (_rename_paths)
        expected_py_file = os.path.join(expected_repo_path, repo_name, f"{repo_name}.py")
        self.assertTrue(
            os.path.exists(expected_py_file), 
            f"Smoke test failed: File/Folder renaming failed. Missing {expected_py_file}"
        )

        # Verify content replacement logic worked (_rename_in_tree)
        readme_path = os.path.join(expected_repo_path, "README.md")
        self.assertTrue(
            os.path.exists(readme_path), 
            "Smoke test failed: README.md was not extracted."
        )
        
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn(
                repo_name, content, 
                "Smoke test failed: Placeholder in README.md was not replaced with the repo name."
            )
            self.assertNotIn(
                biscuitcutter.TEMPLATE_PLACEHOLDER_REPO, content, 
                "Smoke test failed: Original placeholder still exists in README.md."
            )

if __name__ == "__main__":
    unittest.main()